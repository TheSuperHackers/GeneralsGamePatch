from enum import Enum, auto
from pathlib import Path
import os


def build_abs_path(relative_path: str) -> Path:
    dir: str = os.path.dirname(os.path.realpath(__file__))
    return Path(dir).joinpath(relative_path).absolute()


def startswith_nocase(s: str, startswith: str) -> bool:
    return s.lower().startswith(startswith.lower())


class Language(Enum):
    Void = auto
    Chinese = auto


def run():
    generals_str = build_abs_path("../../../GameFilesEdited/Data/generals.str")
    assert generals_str.is_file()

    generals_str_lines: list[str]

    with open(generals_str, mode="r", encoding="utf-8") as file:
        generals_str_lines = file.readlines()

    zh_lines: list[str] = []

    for index, line in enumerate(generals_str_lines):
        if line.startswith("//"):
            continue

        if startswith_nocase(line, "ZH:"):
            sentence = line[3:]
            if ':' in sentence or '.' in sentence or '!' in sentence or '?' in sentence:
                zh_lines.append(f"line {index}: {line}")

    out_path = build_abs_path("generated")
    out_path.mkdir(exist_ok=True)
    out_file = build_abs_path("generated/zh_wrong_symbols.txt")
    with open(out_file, mode="w", encoding="utf-8") as file:
        for line in zh_lines:
            file.write(line)


if __name__ == "__main__":
    run()
