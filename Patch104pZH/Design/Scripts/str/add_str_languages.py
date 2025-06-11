from pathlib import Path
import os


def build_abs_path(relative_path: str) -> Path:
    dir: str = os.path.dirname(os.path.realpath(__file__))
    return Path(dir).joinpath(relative_path).absolute()


def startswith_nocase(s: str, startswith: str) -> bool:
    return s.lower().startswith(startswith.lower())


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
    "UK:",
    "SV:"
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
    generals_str_statusquo = build_abs_path("../../../GameFilesEdited/Data/generals.str.old") # manually create a copy of the source file
    generals_str_new = build_abs_path("../../../GameFilesEdited/Data/generals.str")

    assert generals_str_statusquo.is_file()

    statusquo_lines: list[str]
    new_lines = list[str]()

    with open(generals_str_statusquo, mode="r", encoding="utf-8") as file:
        statusquo_lines = file.readlines()

    ls = LanguageSelector()
    ls.is_in_label_block = False
    ls.is_in_sub_label_block = False
    ls.is_pure_sub_label_block = False
    ls.label_language_index = 0
    ls.sub_label_language_index = 0
    ls.sub_label_language_count = 0
    ls.text = ""

    for line in statusquo_lines:
        line = line.strip()

        if not line:
            pass
        elif not ls.is_in_label_block:
            if line.startswith("//"):
                pass
            else:
                assert not startswith_nocase(line, "End")
                assert ":" in line
                ls.is_in_label_block = True
                ls.label_language_index = 0
        else:
            # Process label block

            if line.startswith("US:"):
                # Takes US text as starting text for the new language string.
                ls.text = line[4:]

            if startswith_nocase(line, "End"):
                # End of label block.
                # Add remaining missing languages if applicable.
                add_new_languages(new_lines, line, ls)
                ls.is_in_label_block = False

            elif line.startswith("//"):
                if line == "//patch104p-core-begin" or line == "//patch104p-optional-begin":
                    # Begin of sub label block.
                    ls.is_in_sub_label_block = True
                    ls.sub_label_language_index = ls.label_language_index
                    ls.sub_label_language_count = 0
                    if ls.label_language_index == 0:
                        ls.is_pure_sub_label_block = True
                    else:
                        ls.is_pure_sub_label_block = False

                elif line == "//patch104p-core-end" or line == "//patch104p-optional-end":
                    assert ls.is_in_sub_label_block == True
                    # End of sub label block.
                    if ls.is_pure_sub_label_block:
                        # Add remaining missing languages if applicable.
                        add_new_languages(new_lines, line, ls)

                    if line == "//patch104p-optional-end":
                        ls.label_language_index += ls.sub_label_language_count
                    ls.is_in_sub_label_block = False

            else:
                # Add remaining missing languages if applicable.
                add_new_languages(new_lines, line, ls)

                expected_language = get_expected_language(ls)
                if expected_language:
                    assert line.startswith(expected_language)
                    if ls.is_in_sub_label_block:
                        ls.sub_label_language_index += 1
                        ls.sub_label_language_count += 1
                    else:
                        ls.label_language_index += 1

        new_lines.append(line)

    with open(generals_str_new, mode="w", encoding="utf-8") as file:
        for line in new_lines:
            file.write(line)
            file.write("\n")

    pass


if __name__ == "__main__":
    run()
