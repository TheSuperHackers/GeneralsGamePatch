from pathlib import Path
import os


def build_abs_path(relative_path: str) -> Path:
    dir: str = os.path.dirname(os.path.realpath(__file__))
    return Path(dir).joinpath(relative_path).absolute()


def startswith_nocase(s: str, startswith: str) -> bool:
    return s.lower().startswith(startswith.lower())


def run():
    generals_str_statusquo = build_abs_path("../../../GameFilesEdited/Data/generals.str.statusquo") # manually create a copy of the source file
    generals_str_upgrade = build_abs_path("../../../GameFilesEdited/Data/generals.str.upgrade")
    generals_str_new = build_abs_path("../../../GameFilesEdited/Data/generals.str")

    assert generals_str_statusquo.is_file()
    assert generals_str_upgrade.is_file()

    statusquo_lines: list[str]
    upgrade_lines: list[str]
    new_lines = list[str]()

    with open(generals_str_statusquo, mode="r", encoding="utf-8") as file:
        statusquo_lines = file.readlines()

    with open(generals_str_upgrade, mode="r", encoding="utf-8") as file:
        upgrade_lines = file.readlines()

    #upgrade_languages = ["US:", "DE:", "FR:", "ES:", "IT:", "KO:", "ZH:", "BP:", "PL:", "RU", "AR", "UK", "SV"]
    upgrade_languages = ["US:", "DE:", "FR:", "ES:", "IT:", "KO:", "ZH:", "BP:", "PL:", "RU", "SV"]
    is_in_label_block = False
    label_name = ""
    sub_label_name = ""

    upgrade_label_index_map = dict[str, int]()

    for index, line in enumerate(upgrade_lines):
        line = line.strip()
        if not line:
            pass
        elif line.startswith("//"):
            pass
        elif not is_in_label_block:
            assert not startswith_nocase(line, "End")
            assert ":" in line
            is_in_label_block = True
            upgrade_label_index_map[line] = index
        elif startswith_nocase(line, "End"):
            is_in_label_block = False

    for line in statusquo_lines:
        line = line.strip()
        if not line:
            pass
        elif line.startswith("//"):
            if line == "//patch104p-core-begin" or line == "//patch104p-optional-begin":
                # Begin of sub label block.
                sub_label_name = line
            elif line == "//patch104p-core-end" or line == "//patch104p-optional-end":
                # End of sub label block.
                sub_label_name = ""
            pass
        elif not is_in_label_block:
            assert not startswith_nocase(line, "End")
            assert ":" in line
            is_in_label_block = True
            label_name = line
        elif startswith_nocase(line, "End"):
            is_in_label_block = False
            sub_label_name = ""
        else:
            upgrade_language = ""
            for language in upgrade_languages:
                if line.startswith(language):
                    upgrade_language = language
                    break

            if upgrade_language:
                index = upgrade_label_index_map.get(label_name, -1)
                if index >= 0:
                    upgrade_line = ""
                    upgrade_index = index + 1
                    upgrade_sub_label_name = ""

                    while upgrade_index < len(upgrade_lines):
                        upgrade_line_search = upgrade_lines[upgrade_index].strip()
                        if startswith_nocase(upgrade_line_search, "End"):
                            break
                        if upgrade_line_search.startswith("//"):
                            if upgrade_line_search == "//patch104p-core-begin" or upgrade_line_search == "//patch104p-optional-begin":
                                # Begin of sub label block.
                                upgrade_sub_label_name = upgrade_line_search
                            elif upgrade_line_search == "//patch104p-core-end" or upgrade_line_search == "//patch104p-optional-end":
                                # End of sub label block.
                                upgrade_sub_label_name = ""
                            pass
                        if upgrade_line_search.startswith(upgrade_language) and sub_label_name == upgrade_sub_label_name:
                            upgrade_line = upgrade_line_search
                            break
                        upgrade_index += 1

                    if upgrade_line:
                        skip = False
                        if line[4] != "\"":
                            skip = True
                        if not skip:
                            line = upgrade_line

        new_lines.append(line)

    with open(generals_str_new, mode="w", encoding="utf-8") as file:
        for line in new_lines:
            file.write(line)
            file.write("\n")

    pass


if __name__ == "__main__":
    run()
