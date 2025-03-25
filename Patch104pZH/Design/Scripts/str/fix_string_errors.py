from pathlib import Path
import os


def build_abs_path(relative_path: str) -> Path:
    dir: str = os.path.dirname(os.path.realpath(__file__))
    return Path(dir).joinpath(relative_path).absolute()


def startswith_nocase(s: str, startswith: str) -> bool:
    return s.lower().startswith(startswith.lower())


def run():
    generals_str = build_abs_path("../../../GameFilesEdited/Data/generals.str.old") # manually create a copy of the source file
    generals_str_new = build_abs_path("../../../GameFilesEdited/Data/generals.str")

    assert generals_str.is_file()

    generals_str_lines: list[str]

    with open(generals_str, mode="r", encoding="utf-8") as file:
        generals_str_lines = file.readlines()

    is_dialogevent = False

    for index, line in enumerate(generals_str_lines):
        if line.startswith("//"):
            continue

        if startswith_nocase(line, "DIALOGEVENT:"):
            is_dialogevent = True
            continue

        if startswith_nocase(line, "End"):
            is_dialogevent = False
            continue

        if is_dialogevent and (
            startswith_nocase(line, "US: \"") or
            startswith_nocase(line, "DE: \"") or
            startswith_nocase(line, "FR: \"") or
            startswith_nocase(line, "BP: \"") or
            startswith_nocase(line, "PL: \"") or
            startswith_nocase(line, "RU: \"") or
            startswith_nocase(line, "UK: \"") or
            startswith_nocase(line, "SV: \"")):
            if line[5:6] != "*":
                new_line = line[:5] + "*" + line[5:]
                generals_str_lines[index] = new_line

        if is_dialogevent and (
            startswith_nocase(line, "KO: \"") or
            startswith_nocase(line, "ES: \"") or
            startswith_nocase(line, "IT: \"") or
            startswith_nocase(line, "ZH: \"")):
            if line[5:6] == "*":
                continue
            if line[5:7] != "\\n":
                new_line = line[:5] + "\\n" + line[5:]
                generals_str_lines[index] = new_line

    with open(generals_str_new, mode="w", encoding="utf-8") as file:
        for line in generals_str_lines:
            file.write(line)


if __name__ == "__main__":
    run()
