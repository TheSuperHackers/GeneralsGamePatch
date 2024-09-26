from pathlib import Path
import os


def build_abs_path(relative_path: str) -> Path:
    dir: str = os.path.dirname(os.path.realpath(__file__))
    return Path(dir).joinpath(relative_path).absolute()


def startswith_nocase(s: str, startswith: str) -> bool:
    return s.lower().startswith(startswith.lower())


def run():
    generals_str_with_ea_comments = build_abs_path("Generals.str")
    generals_str = build_abs_path("../../../GameFilesEdited/Data/generals.str.old") # manually create a copy of the source file
    generals_str_new = build_abs_path("../../../GameFilesEdited/Data/generals.str")

    assert generals_str.is_file()

    generals_str_with_ea_comments_lines: list[str]
    generals_str_lines: list[str]
    new_lines = list[str]()

    with open(generals_str, mode="r", encoding="utf-8") as file:
        generals_str_lines = file.readlines()

    with open(generals_str_with_ea_comments, mode="r", encoding="cp1252") as file:
        generals_str_with_ea_comments_lines = file.readlines()

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

    src_label_index_map = dict[str, int]()

    for src_index, src_line in enumerate(generals_str_with_ea_comments_lines):
        src_line = src_line.strip()
        for label_name in label_names:
            if src_line.startswith(label_name):
                assert src_index >= 0
                src_label_index_map[src_line] = src_index

    for dst_line in generals_str_lines:
        dst_line = dst_line.strip()
        dst_label_name: str = ""

        for label_name in label_names:
            if dst_line.startswith(label_name):
                dst_label_name = dst_line
                break

        if dst_label_name:
            src_index = src_label_index_map.get(dst_label_name)
            if src_index:
                # Iterate backwards and find previous End
                begin = src_index
                while begin > 0:
                    begin -= 1
                    line = generals_str_with_ea_comments_lines[begin].strip()
                    if startswith_nocase(line, "End"):
                        break
                # Iterate forward and find next End
                file_end = len(generals_str_with_ea_comments_lines)
                end = src_index
                while end < file_end:
                    end += 1
                    line = generals_str_with_ea_comments_lines[end].strip()
                    if startswith_nocase(line, "End"):
                        break
                # Iterate forward to label and collect comments
                for i in range(begin + 1, end):
                    comment = generals_str_with_ea_comments_lines[i].strip()
                    if comment.startswith("//"):
                        if comment == "//context:":
                            continue
                        if comment == "// context:":
                            continue
                        if comment == "//comment:":
                            continue
                        if comment == "// comment:":
                            continue
                        new_lines.append(comment)
                        continue

        new_lines.append(dst_line)

    with open(generals_str_new, mode="w", encoding="utf-8") as file:
        for line in new_lines:
            file.write(line)
            file.write("\n")

    pass


if __name__ == "__main__":
    run()
