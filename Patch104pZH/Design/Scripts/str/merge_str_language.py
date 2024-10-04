from pathlib import Path
import os


def build_abs_path(relative_path: str) -> Path:
    dir: str = os.path.dirname(os.path.realpath(__file__))
    return Path(dir).joinpath(relative_path).absolute()


def startswith_nocase(s: str, startswith: str) -> bool:
    return s.lower().startswith(startswith.lower())


def run():
    generals_str_statusquo = build_abs_path("../../../GameFilesEdited/Data/generals.str.old") # manually create a copy of the source file
    #generals_str_upgrade = build_abs_path("data/ukrainian_zh_by_yarpik/generals.str")
    #generals_str_upgrade = build_abs_path("data/ukrainian_zh_by_yarpik_windstalker_edit_1/generals.str")
    generals_str_upgrade = build_abs_path("data/ukrainian_zh_by_yarpik_windstalker_edit_2/generals.str")
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

    upgrade_language = "UK:"
    is_in_label_block = False
    label_name = ""

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
            pass
        elif not is_in_label_block:
            assert not startswith_nocase(line, "End")
            assert ":" in line
            is_in_label_block = True
            label_name = line
        elif startswith_nocase(line, "End"):
            is_in_label_block = False
        elif line.startswith(upgrade_language):
            index = upgrade_label_index_map.get(label_name, -1)
            if index >= 0:
                upgrade_line = upgrade_lines[index + 1].strip()
                skip = False

                # Ingore all placeholder strings starting with single star (*)
                # because they are untouched original English texts
                # but can slightly mismatch with patched English strings:
                # UK: "*You have requested funds from your Ally"
                if line[4] != "\"":
                    skip = True
                #if line.startswith("UK: \"<Red Guard speaking>"):
                #    skip = True
                #elif line.startswith("UK: \"<'EVA' speaking>"):
                #    skip = True
                #elif line.startswith("UK: \"<AutoFerry Capt. speaking>"):
                #    skip = True
                elif line.startswith("UK: \"*") and line[6] != '*':
                    skip = True

                if not skip:
                    line = f'{upgrade_language} {upgrade_line}'

        new_lines.append(line)

    with open(generals_str_new, mode="w", encoding="utf-8") as file:
        for line in new_lines:
            file.write(line)
            file.write("\n")

    pass


if __name__ == "__main__":
    run()
