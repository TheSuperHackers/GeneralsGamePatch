import itertools
from pathlib import Path

files = itertools.chain(
    Path("../Patch104pZH/GameFilesOriginal").glob("**/*.ini"),
    Path("../Patch104pZH/GameFilesEdited").glob("**/*.ini"),
    Path("../Patch104pZH/GameFilesTest").glob("**/*.ini"),
)

for file in files:
    with open(file, "r") as f:
        lines = [ line.rstrip(" \t\r\n") for line in f ]

    with open(file, "w", encoding="utf-8", newline="\n") as f:
        for line in lines:
            f.write(line + "\n")
