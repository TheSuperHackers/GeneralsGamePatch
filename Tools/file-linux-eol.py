import itertools
from pathlib import Path

paths = itertools.chain(
    Path("..").rglob("*.bat"),
    Path("..").rglob("*.css"),
    Path("..").rglob("*.csv"),
    Path("..").rglob("*.html"),
    Path("..").rglob("*.gitattributes"),
    Path("..").rglob("*.gitignore"),
    Path("..").rglob("*.ini"),
    Path("..").rglob("*.json"),
    Path("..").rglob("*.md"),
    Path("..").rglob("*.py"),
    Path("..").rglob("*.str"),
    Path("..").rglob("*.txt"),
    Path("..").rglob("*.wnd"),
    Path("..").rglob("LICENSE"),
)

for path in paths:
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except UnicodeDecodeError:
        with open(path, "r", encoding="windows-1252") as file:
            lines = file.readlines()

    with open(path, "w", encoding="utf-8", newline="\n") as file:
        for line in lines:
            file.write(line)
