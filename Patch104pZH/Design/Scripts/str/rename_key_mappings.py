from pathlib import Path
import os


def build_abs_path(relative_path: str) -> Path:
    dir: str = os.path.dirname(os.path.realpath(__file__))
    return Path(dir).joinpath(relative_path).absolute()


def startswith_nocase(s: str, startswith: str) -> bool:
    return s.lower().startswith(startswith.lower())


def classic_intext_key_to_new_key(line: str) -> str:
    new_line = ""
    iqub: int = line.find('"')
    iamp: int = line.find('&', iqub)

    if startswith_nocase(line, "ZH"):
        colon = "："
    else:
        colon = ": "

    if iamp < 0:
        return new_line

    line_colon_word = line[iamp-len(colon):iamp]
    line_2_word = line[iamp-2:iamp]
    line_1_word = line[iamp-1]

    if line_colon_word != colon and line_2_word != "! " and line_1_word != '(' and line_1_word != '[' and line_1_word != '（':
        ique: int = line.rfind('"')
        assert ique > iamp
        key: str = line[iamp+1]
        new_line = line[:iamp]
        new_line += line[iamp+1:ique]
        if new_line[-1] != '!':
            new_line += colon
        new_line += "&" + key.upper()
        new_line += line[ique:]

    return new_line


def classic_trailing_key_to_new_key(line: str) -> str:
    new_line = ""
    iqub: int = line.find('"')
    iamp: int = line.find('&', iqub)

    if startswith_nocase(line, "ZH"):
        colon = '：'
    else:
        colon = ': '

    if iamp >= 0 and (line[iamp-1] == '(' or line[iamp-1] == '[' or line[iamp-1] == '（'):
        ique: int = line.rfind('"')
        assert ique > iamp
        key: str = line[iamp+1]
        new_line = line[:iamp-1].strip(" ")
        new_line += line[iamp+3:ique]
        if new_line[-1] != '!':
            new_line += colon
        new_line += "&" + key.upper()
        new_line += line[ique:]

    return new_line


def change_leading_chars(line: str, before: str, after: str) -> str:
    new_line = ""
    iqub: int = line.find('"')
    iamp: int = line.find('&', iqub)

    if iamp >= 0 and line[iamp-len(before):iamp] == before:
        new_line = line[:iamp-len(before)] + after + line[iamp:]

    return new_line


def run():
    generals_str = build_abs_path("../../../GameFilesEdited/Data/generals.str.old") # manually create a copy of the source file
    generals_str_new = build_abs_path("../../../GameFilesEdited/Data/generals.str")

    assert generals_str.is_file()

    generals_str_lines: list[str]

    with open(generals_str, mode="r", encoding="utf-8") as file:
        generals_str_lines = file.readlines()

    is_key_string = False

    for index, line in enumerate(generals_str_lines):
        if line.startswith("//"):
            continue

        if startswith_nocase(line, "CONTROLBAR:") or startswith_nocase(line, "UPGRADE:"):
            is_key_string = True
            continue

        if startswith_nocase(line, "End"):
            is_key_string = False
            continue

        if not is_key_string:
            continue

        new_line = classic_intext_key_to_new_key(line)
        if new_line:
            generals_str_lines[index] = new_line
            continue

        new_line = classic_trailing_key_to_new_key(line)
        if new_line:
            generals_str_lines[index] = new_line
            continue

        if startswith_nocase(line, "ZH"):
            new_line = change_leading_chars(line, ": ", "：")
            if new_line:
                generals_str_lines[index] = new_line
                continue

    with open(generals_str_new, mode="w", encoding="utf-8") as file:
        for line in generals_str_lines:
            file.write(line)


if __name__ == "__main__":
    run()
