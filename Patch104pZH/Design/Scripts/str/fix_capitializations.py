from pathlib import Path
import os


def build_abs_path(relative_path: str) -> Path:
    dir: str = os.path.dirname(os.path.realpath(__file__))
    return Path(dir).joinpath(relative_path).absolute()


def startswith_nocase(s: str, startswith: str) -> bool:
    return s.lower().startswith(startswith.lower())


def run():
    generals_str = build_abs_path("../../../GameFilesEdited/Data/generals.str")

    assert generals_str.is_file()

    generals_str_lines: list[str]

    with open(generals_str, mode="r", encoding="utf-8") as file:
        generals_str_lines = file.readlines()

    search_words = [
        "// context: ",
        "// comment:"]

    for index, line in enumerate(generals_str_lines):
        for word in search_words:
            i = len(word)
            if line.startswith(word) and line[i].islower():
                generals_str_lines[index] = line[:i] + line[i].upper() + line[i+1:]
                pass

    with open(generals_str, mode="w", encoding="utf-8") as file:
        for line in generals_str_lines:
            file.write(line)

if __name__ == "__main__":
    run()
