import itertools
from pathlib import Path

paths = itertools.chain(
    Path("..").rglob("*.ini"),
)

for path in paths:
    with open(path, "r", encoding="utf-8") as file:
        lines = [ line.rstrip(" \t\r\n") for line in file ]

    with open(path, "w", encoding="utf-8", newline="\n") as file:
        for line in lines:
            file.write(line + "\n")
