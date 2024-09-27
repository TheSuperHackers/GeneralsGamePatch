import os
from copy import copy
from pathlib import Path


class StringEntry:
    key: str
    text: str

    def __init__(self) -> None:
        self.key = ""
        self.text = ""


class StringMultiEntry:
    name: str
    lang_string: dict[str, StringEntry]

    def __init__(self) -> None:
        self.name = ""
        self.lang_string = dict()


def build_abs_path(relative_path: str) -> Path:
    dir: str = os.path.dirname(os.path.realpath(__file__))
    return Path(dir).joinpath(relative_path).absolute()


def startswith_nocase(s: str, startswith: str) -> bool:
    return s.lower().startswith(startswith.lower())


def read_multi_string_entries(generals_str: Path, *categories: tuple[str, ...]) -> list[StringMultiEntry]:
    entries: list[StringMultiEntry] = []

    with open(generals_str, encoding="utf-8") as file:
        lines = file.readlines()
        entry = StringMultiEntry()
        skip = False

        for line in lines:
            line = line.strip()

            if line.startswith("//patch104p-optional-begin"):
                skip = True
                continue
            if line.startswith("//patch104p-optional-end"):
                skip = False
                continue

            if skip:
                continue

            if line.startswith("//") or line.startswith("\\"):
                continue

            done = False
            for category in categories:
                if startswith_nocase(line, category):
                    entry = StringMultiEntry()
                    value_str = line.strip()
                    entry.name = value_str
                    done = True
                    continue

            if done:
                continue

            if entry.name and len(line) > 3 and line[2] == ":":
                key_value_pair: list[str] = line.split(" ", 1)
                if len(key_value_pair) != 2:
                    continue
                lang_code = key_value_pair[0].strip().strip(":")
                value_str = key_value_pair[1].strip().strip("\"")
                entrylite = StringEntry()
                entrylite.text = value_str
                key_index = entrylite.text.find("&")
                if key_index >= 0:
                    entrylite.key = entrylite.text[key_index+1:key_index+2]
                entry.lang_string[lang_code] = entrylite
                continue

            if entry.name and startswith_nocase(line, "End"):
                entries.append(copy(entry))
                entry = StringMultiEntry()
                continue

    return entries


def find_missing_keys(multi_strings: list[StringMultiEntry]) -> None:
    out_txt_path = build_abs_path(f"generated/key_missing.txt")
    with open(out_txt_path, "w", encoding="utf-8") as txt_file:
        multi_string: StringMultiEntry
        for multi_string in multi_strings:
            lang_code: str
            string: StringEntry
            has_key = False

            for string in multi_string.lang_string.values():
                if string.key:
                    has_key = True
                    break

            if has_key:
                for lang_code, string in multi_string.lang_string.items():
                    if lang_code == "AR":
                        continue # Ignore Arabic for now because it has no key mappings at all.
                    if not string.key:
                        txt_file.write(f"{multi_string.name} : {lang_code}: \"{string.text}\"")
                        txt_file.write("\n")


def run():
    generals_str = build_abs_path("../../../GameFilesEdited/Data/generals.str")
    assert generals_str.is_file()

    out_path = build_abs_path("generated")
    out_path.mkdir(exist_ok=True)

    multi_strings: list[StringMultiEntry] = read_multi_string_entries(generals_str, "CONTROLBAR:", "UPGRADE:")

    find_missing_keys(multi_strings)


if __name__ == "__main__":
    run()
