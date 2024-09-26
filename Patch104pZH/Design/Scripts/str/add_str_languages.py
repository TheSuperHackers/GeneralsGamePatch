from pathlib import Path
import os


def build_abs_path(relative_path: str) -> Path:
    dir: str = os.path.dirname(os.path.realpath(__file__))
    return Path(dir).joinpath(relative_path).absolute()


g_expected_languages = [
    "US:",
    "DE:",
    "FR:",
    "ES:",
    "IT:",
    "KO:",
    "ZH:",
    "BP:",
    "PL:",
    "RU:",
    "AR:",
    "UK:"
]

class LanguageSelector:
    is_in_label_block: bool
    is_in_sub_label_block: bool
    is_pure_sub_label_block: bool
    label_language_index: int
    sub_label_language_index: int
    sub_label_language_count: int
    text: str


def get_expected_language(ls: LanguageSelector) -> str:
    if ls.is_in_sub_label_block:
        if ls.sub_label_language_index < len(g_expected_languages):
            return g_expected_languages[ls.sub_label_language_index]
    elif ls.is_in_label_block:
        if ls.label_language_index < len(g_expected_languages):
            return g_expected_languages[ls.label_language_index]
    return ""


def add_new_languages(out_lines: list[str], next_line: str, ls: LanguageSelector) -> None:
    while True:
        expected_language = get_expected_language(ls)
        if not expected_language or next_line.startswith(expected_language):
            break
        out_lines.append(f'{expected_language} {ls.text}')
        if ls.is_in_sub_label_block:
            ls.sub_label_language_index += 1
            ls.sub_label_language_count += 1
        else:
            ls.label_language_index += 1


def run():
    generals_str = build_abs_path("../../../GameFilesEdited/Data/generals.str.old") # manually create a copy of the source file
    generals_str_export = build_abs_path("../../../GameFilesEdited/Data/generals.str")

    assert generals_str.is_file()

    generals_str_lines: list[str]
    new_lines = list[str]()

    with open(generals_str, mode="r", encoding="utf-8") as file:
        generals_str_lines = file.readlines()

    ls = LanguageSelector()
    ls.is_in_label_block = False
    ls.is_in_sub_label_block = False
    ls.is_pure_sub_label_block = False
    ls.label_language_index = 0
    ls.sub_label_language_index = 0
    ls.sub_label_language_count = 0
    ls.text = ""

    for dst_line in generals_str_lines:
        dst_line = dst_line.strip()

        if not dst_line:
            pass
        elif not ls.is_in_label_block:
            if dst_line.startswith("//"):
                pass
            # Find begin or end of label block
            elif dst_line.lower() == "end":
                ls.is_in_label_block = False
            else:
                assert ":" in dst_line
                ls.is_in_label_block = True
                ls.label_language_index = 0
        else:
            # Process label block
            dst_line_lower = dst_line.lower()

            if dst_line.startswith("US:"):
                # Takes US text as starting text for the new language string.
                ls.text = dst_line[4:]

            if dst_line_lower == "end":
                # End of label block.
                # Add remaining missing languages if applicable.
                add_new_languages(new_lines, dst_line, ls)
                ls.is_in_label_block = False

            elif dst_line.startswith("//"):
                if dst_line == "//patch104p-core-begin" or dst_line == "//patch104p-optional-begin":
                    # Begin of sub label block.
                    ls.is_in_sub_label_block = True
                    ls.sub_label_language_index = ls.label_language_index
                    ls.sub_label_language_count = 0
                    if ls.label_language_index == 0:
                        ls.is_pure_sub_label_block = True
                    else:
                        ls.is_pure_sub_label_block = False

                elif dst_line == "//patch104p-core-end" or dst_line == "//patch104p-optional-end":
                    assert ls.is_in_sub_label_block == True
                    # End of sub label block.
                    if ls.is_pure_sub_label_block:
                        # Add remaining missing languages if applicable.
                        add_new_languages(new_lines, dst_line, ls)

                    if dst_line == "//patch104p-optional-end":
                        ls.label_language_index += ls.sub_label_language_count
                    ls.is_in_sub_label_block = False

            else:
                # Add remaining missing languages if applicable.
                add_new_languages(new_lines, dst_line, ls)

                expected_language = get_expected_language(ls)
                if expected_language:
                    assert dst_line.startswith(expected_language)
                    if ls.is_in_sub_label_block:
                        ls.sub_label_language_index += 1
                        ls.sub_label_language_count += 1
                    else:
                        ls.label_language_index += 1

        new_lines.append(dst_line)

    with open(generals_str_export, mode="w", encoding="utf-8") as file:
        for line in new_lines:
            file.write(line)
            file.write("\n")

    pass


if __name__ == "__main__":
    run()
