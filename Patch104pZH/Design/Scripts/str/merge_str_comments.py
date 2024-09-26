from pathlib import Path
import os


def build_abs_path(relative_path: str) -> Path:
    dir: str = os.path.dirname(os.path.realpath(__file__))
    return Path(dir).joinpath(relative_path).absolute()


def startswith_nocase(s: str, startswith: str) -> bool:
    return s.lower().startswith(startswith.lower())


def run():
    generals_str_statusquo = build_abs_path("../../../GameFilesEdited/Data/generals.str.old") # manually create a copy of the source file
    generals_str_dev = build_abs_path("data/english_dev_comments/Generals.str")
    generals_str_new = build_abs_path("../../../GameFilesEdited/Data/generals.str")

    assert generals_str_statusquo.is_file()
    assert generals_str_dev.is_file()

    statusquo_lines: list[str]
    dev_lines: list[str]
    new_lines = list[str]()

    with open(generals_str_statusquo, mode="r", encoding="utf-8") as file:
        statusquo_lines = file.readlines()

    with open(generals_str_dev, mode="r", encoding="cp1252") as file:
        dev_lines = file.readlines()

    label_names = {
        'LETTER:',
        'Color:',
        'ERROR:',
        'GUI:',
        'QM:',
        'MESSAGE:',
        'LOSE:',
        'MSG:',
        'SCRIPT:',
        'MapTransfer:',
        'Map:',
        'Mouse:',
        'FTP:',
        'ThingTemplate:',
        'CAMPAIGN:',
        'UPGRADE:',
        'TOOLTIP:',
        'OBJECT:',
        'Buddy:',
        'LABEL:',
        'MOTD:',
        'DIALOGEVENT:',
        'KEYBOARD:',
        'RADAR:',
        'Version:',
        'LAN:',
        'SIDE:',
        'Team:',
        'MD_GLA05-MilitaryBriefing:',
        'Chat:',
        'GC_CHINABOSS:',
        'Audio:',
        'CONTROLBAR:',
        'SCIENCE:',
        'CREDITS:',
        'DOZER:',
        'MDGLA03:',
        'NUMBER:',
        'TOOTIP:',
        'ACADEMY:',
        'LOAD:',
        'INI:',
        'WOL:',
        'HELP:',
        'MAP:',
        'GENERIC:',
        'Network:',
        'MDGLA02:' }

    dev_label_index_map = dict[str, int]()

    for index, line in enumerate(dev_lines):
        line = line.strip()
        for label_name in label_names:
            if line.startswith(label_name):
                assert index >= 0
                dev_label_index_map[line] = index

    for statusquo_line in statusquo_lines:
        statusquo_line = statusquo_line.strip()
        statusquo_label_name: str = ""

        for label_name in label_names:
            if statusquo_line.startswith(label_name):
                statusquo_label_name = statusquo_line
                break

        if statusquo_label_name:
            dev_index = dev_label_index_map.get(statusquo_label_name, -1)
            if dev_index >= 0:
                # Iterate backwards and find previous End
                begin = dev_index
                while begin > 0:
                    begin -= 1
                    dev_line = dev_lines[begin].strip()
                    if startswith_nocase(dev_line, "End"):
                        break
                # Iterate forward and find next End
                dev_lines_end = len(dev_lines)
                end = dev_index
                while end < dev_lines_end - 1:
                    end += 1
                    dev_line = dev_lines[end].strip()
                    if startswith_nocase(dev_line, "End"):
                        break
                # Iterate forward to label and collect comments
                for i in range(begin + 1, end):
                    dev_line = dev_lines[i].strip()
                    if dev_line.startswith("//"):
                        if dev_line == "//context:":
                            continue
                        if dev_line == "// context:":
                            continue
                        if dev_line == "//comment:":
                            continue
                        if dev_line == "// comment:":
                            continue
                        new_lines.append(dev_line)
                        continue

        new_lines.append(statusquo_line)

    with open(generals_str_new, mode="w", encoding="utf-8") as file:
        for line in new_lines:
            file.write(line)
            file.write("\n")

    pass


if __name__ == "__main__":
    run()
