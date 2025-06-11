from copy import copy
from enum import Enum, auto
from pathlib import Path
import os
import time


class Timer:
    start: float
    elapsed: float

    def __init__(self):
        self.start: float = time.time()
        self.elapsed: float = 0.0

    def Start(self) -> None:
        self.elapsed = 0.0
        self.start = time.time()

    def Finish(self) -> None:
        self.elapsed = time.time() - self.start

    def GetElapsedSeconds(self) -> float:
        if self.elapsed != 0.0:
            return self.elapsed
        else:
            return time.time() - self.start

    def GetElapsedSecondsString(self) -> str:
        elapsed = self.GetElapsedSeconds()
        return str.format("{:.3f}", elapsed)


class StringEntry:
    name: str
    key: str
    text: str

    def __init__(self) -> None:
        self.clear()

    def clear(self) -> None:
        self.name = ""
        self.key = ""
        self.text = ""


class CommandMapCategory(Enum):
    UNKNOWN = auto()
    CONTROL = auto()
    SELECTION = auto()

    @staticmethod
    def from_str(label: str):
        upperlabel = label.upper()
        for category in CommandMapCategory:
            if upperlabel == category.name:
                return category
        return CommandMapCategory.UNKNOWN


class CommandMapModifier(Enum):
    UNKNOWN = auto()
    NONE = auto()

    @staticmethod
    def from_str(label: str):
        upperlabel = label.upper()
        for modifier in CommandMapModifier:
            if upperlabel == modifier.name:
                return modifier
        return CommandMapModifier.UNKNOWN


class CommandMapUseableIn(Enum):
    UNKNOWN = auto()
    GAME = auto()

    @staticmethod
    def from_str(label: str):
        upperlabel = label.upper()
        for modifier in CommandMapUseableIn:
            if upperlabel == modifier.name:
                return modifier
        return CommandMapUseableIn.UNKNOWN


class CommandMap:
    name: str
    key: str
    category: CommandMapCategory
    modifier: CommandMapModifier
    useable_in: CommandMapUseableIn

    def __init__(self) -> None:
        self.clear()

    def clear(self) -> None:
        self.name = ""
        self.key = ""
        self.category = CommandMapCategory.UNKNOWN
        self.modifier = CommandMapModifier.UNKNOWN
        self.useable_in = CommandMapUseableIn.UNKNOWN



class CommandButton:
    name: str
    text_string: StringEntry
    descript_string: StringEntry

    def __init__(self) -> None:
        self.clear()

    def clear(self) -> None:
        self.name = ""
        self.text_string = None
        self.descript_string = None


class CommandSet:
    name: str
    buttons: list[CommandButton]
    is_unit: bool

    def __init__(self) -> None:
        self.clear()

    def clear(self) -> None:
        self.name = ""
        self.buttons = [None] * 18
        self.is_unit = False


def startswith_nocase(s: str, startswith: str) -> bool:
    return s.lower().startswith(startswith.lower())


def named_list_to_dict(l: list) -> dict:
    dictionary: dict = {}
    for element in l:
        dictionary[element.name] = element
    return dictionary


def build_abs_path(relative_path: str) -> Path:
    dir: str = os.path.dirname(os.path.realpath(__file__))
    return Path(dir).joinpath(relative_path).absolute()


def read_command_map_entries(
        command_map_ini: Path,
        category: CommandMapCategory,
        modifier: CommandMapModifier,
        useable_in: CommandMapUseableIn) -> list[CommandMap]:

    entries: list[CommandMap] = []

    with open(command_map_ini, encoding="ascii") as file:
        lines = file.readlines()
        entry = CommandMap()

        for line in lines:
            line = line.strip().split(";", 1)[0]

            if startswith_nocase(line, "CommandMap"):
                entry.clear()
                key_value_pair: list[str] = line.split(" ", 1)
                if len(key_value_pair) != 2:
                    continue
                value_str = key_value_pair[1].strip()
                entry.name = value_str

            elif entry.name and startswith_nocase(line, "Category"):
                key_value_pair: list[str] = line.split("=", 1)
                if len(key_value_pair) != 2:
                    continue
                value_str = key_value_pair[1].strip()
                entry.category = CommandMapCategory.from_str(value_str)

            elif entry.name and startswith_nocase(line, "Modifiers"):
                key_value_pair: list[str] = line.split("=", 1)
                if len(key_value_pair) < 2:
                    continue
                value_str = key_value_pair[1].strip()
                entry.modifier = CommandMapModifier.from_str(value_str)

            elif entry.name and startswith_nocase(line, "UseableIn"):
                key_value_pair: list[str] = line.split("=", 1)
                if len(key_value_pair) != 2:
                    continue
                value_str = key_value_pair[1].strip()
                entry.useable_in = CommandMapUseableIn.from_str(value_str)

            elif entry.name and startswith_nocase(line, "Key"):
                key_value_pair: list[str] = line.split("=", 1)
                if len(key_value_pair) != 2:
                    continue
                value_str = key_value_pair[1].strip()
                if startswith_nocase(value_str, "KEY_"):
                    value_str = value_str[4:]
                entry.key = value_str

            elif entry.name and startswith_nocase(line, "End"):
                if entry.category == category and entry.modifier == modifier and entry.useable_in == useable_in:
                    entries.append(copy(entry))
                entry.clear()

    return entries


def read_string_entries(generals_str: Path, lang_code: str, category: str, requires_key=False) -> list[StringEntry]:
    entries: list[StringEntry] = []

    with open(generals_str, encoding="utf-8") as file:
        lines = file.readlines()
        entry = StringEntry()
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

            if startswith_nocase(line, category):
                entry.clear()
                value_str = line.strip()
                entry.name = value_str

            elif entry.name and startswith_nocase(line, lang_code + ":"):
                key_value_pair: list[str] = line.split(" ", 1)
                if len(key_value_pair) != 2:
                    continue
                value_str = key_value_pair[1].strip().strip("\"")
                entry.text = value_str
                key_index = entry.text.find("&")
                if key_index >= 0:
                    entry.key = entry.text[key_index+1:key_index+2]

            elif entry.name and startswith_nocase(line, "End"):
                if not (requires_key and not entry.key):
                    entries.append(copy(entry))
                entry.clear()

    return entries


def read_command_button_entries(command_button_ini: Path, strings: list[StringEntry]) -> list[CommandButton]:
    entries: list[CommandButton] = []

    with open(command_button_ini, encoding="ascii") as file:
        strings_dict: dict[str, StringEntry] = named_list_to_dict(strings)
        lines = file.readlines()
        entry = CommandButton()

        for line in lines:
            line = line.strip().split(";", 1)[0]

            if startswith_nocase(line, "CommandButton"):
                entry.clear()
                key_value_pair: list[str] = line.split(" ", 1)
                if len(key_value_pair) != 2:
                    continue
                value_str = key_value_pair[1].strip()
                entry.name = value_str

            elif entry.name and startswith_nocase(line, "TextLabel"):
                key_value_pair: list[str] = line.split("=", 1)
                if len(key_value_pair) != 2:
                    continue
                value_str = key_value_pair[1].strip()
                entry.text_string = strings_dict.get(value_str)
                if entry.text_string == None:
                    raise RuntimeError(f"{entry.name} references unrecognized string {value_str}")

            elif entry.name and startswith_nocase(line, "DescriptLabel"):
                key_value_pair: list[str] = line.split("=", 1)
                if len(key_value_pair) != 2:
                    continue
                value_str = key_value_pair[1].strip()
                entry.descript_string = strings_dict.get(value_str)
                if entry.descript_string == None:
                    raise RuntimeError(f"{entry.name} references unrecognized string {value_str}")

            elif entry.name and startswith_nocase(line, "End"):
                entries.append(copy(entry))
                entry.clear()

    return entries


def read_command_set_entries(
        command_button_ini: Path,
        command_buttons: list[CommandButton]
        ) -> list[CommandSet]:

    entries: list[CommandSet] = []

    with open(command_button_ini, encoding="ascii") as file:
        command_buttons_dict: dict[str, StringEntry] = named_list_to_dict(command_buttons)
        lines = file.readlines()
        entry = CommandSet()
        skip = False

        for line in lines:
            line = line.strip()

            if startswith_nocase(line, ";patch104p-optional-begin"):
                skip = True
                continue
            elif startswith_nocase(line, ";patch104p-optional-end"):
                skip = False
                continue

            if skip:
                continue

            line = line.split(";", 1)[0]

            if startswith_nocase(line, "CommandSet"):
                entry.clear()
                key_value_pair: list[str] = line.split(" ", 1)
                if len(key_value_pair) != 2:
                    continue
                value_str = key_value_pair[1].strip()
                entry.name = value_str

            elif entry.name and line and line[0].isdigit():
                key_value_pair: list[str] = line.split("=", 1)
                if len(key_value_pair) != 2:
                    continue
                digit_str = key_value_pair[0].strip()
                value_str = key_value_pair[1].strip()
                entry.buttons[int(digit_str)] = command_buttons_dict.get(value_str)
                if entry.buttons[int(digit_str)] == None:
                    raise RuntimeError(f"{entry.name} references unrecognized button {value_str}")

            elif entry.name and startswith_nocase(line, "End"):
                # Try to determine whether or not this is for a unit. Perhaps not 100% accurate.
                if "Infantry" in entry.name:
                    entry.is_unit = True
                elif "Vehicle" in entry.name:
                    entry.is_unit = True
                elif "Jet" in entry.name:
                    entry.is_unit = True
                elif "ChinaTank" in entry.name:
                    entry.is_unit = True
                elif "AmericaTank" in entry.name:
                    entry.is_unit = True
                elif "GLATank" in entry.name:
                    entry.is_unit = True
                elif "Dozer" in entry.name:
                    entry.is_unit = True
                elif "Worker" in entry.name:
                    entry.is_unit = True
                elif "Truck" in entry.name:
                    entry.is_unit = True
                else:
                    button: CommandButton
                    for button in entry.buttons:
                        if button == None:
                            continue
                        if button.name == "Command_Guard":
                            entry.is_unit = True
                            break
                        if button.name == "Command_GuardFlyingUnitsOnly":
                            entry.is_unit = True
                            break
                        if button.name == "Command_AttackMove":
                            entry.is_unit = True
                            break
                        if button.name == "Command_EmptyCrawler":
                            entry.is_unit = True
                            break

                entries.append(copy(entry))
                entry.clear()

    return entries


def dump_command_sets(
        command_sets: list[CommandSet],
        control_command_maps: list[CommandMap],
        selection_command_maps: list[CommandMap],
        lang_code: str) -> None:

    lang_lower: str = lang_code.lower()

    out_txt_path: Path = build_abs_path(f"generated/commandsets_unit.txt")
    with open(out_txt_path, "w", encoding="utf-8") as txt_file:
        command_set: CommandSet
        for command_set in command_sets:
            if command_set.is_unit:
                txt_file.write(command_set.name)
                txt_file.write("\n")

    out_txt_path: Path = build_abs_path(f"generated/commandsets_not_unit.txt")
    with open(out_txt_path, "w", encoding="utf-8") as txt_file:
        command_set: CommandSet
        for command_set in command_sets:
            if not command_set.is_unit:
                txt_file.write(command_set.name)
                txt_file.write("\n")

    out_txt_path: Path = build_abs_path(f"generated/{lang_lower}_commandsets.txt")
    with open(out_txt_path, "w", encoding="utf-8") as txt_file:
        command_set: CommandSet
        command_map: CommandMap
        command_button: CommandButton
        button_idx: int
        keys: set[str] = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}

        for command_set in command_sets:
            txt_file.write(f"CommandSet {command_set.name}\n")
            consumed_keys = set[str]()

            for button_idx, command_button in enumerate(command_set.buttons):
                if command_button and command_button.text_string:
                    txt_file.write(f"  {button_idx} = {command_button.name} : {command_button.text_string.name} \"{command_button.text_string.text}\"\n")
                    consumed_keys.add(command_button.text_string.key.upper())

            for command_map in selection_command_maps:
                if command_map.name == "SELECT_MATCHING_UNITS" and not command_set.is_unit:
                    continue
                if len(command_map.key) != 1:
                    continue
                txt_file.write(f"  CommandMap {command_map.name} : \"{command_map.key}\"\n")
                consumed_keys.add(command_map.key.upper())

            if command_set.is_unit:
                for command_map in control_command_maps:
                    if len(command_map.key) != 1:
                        continue
                    txt_file.write(f"  CommandMap {command_map.name} : \"{command_map.key}\"\n")
                    consumed_keys.add(command_map.key.upper())

            available_keys: set[str] = keys.difference(consumed_keys)
            available_keys_list: list[str] = list(available_keys)
            available_keys_list.sort()
            txt_file.write("    Available keys: ")
            for key in available_keys_list:
                txt_file.write(f"{key}, ")

            txt_file.write("\n")
            txt_file.write("End\n")
            txt_file.write("\n")


def find_invalid_keys(
        strings: list[StringEntry],
        lang_code: str) -> None:

    out_txt_path = build_abs_path(f"generated/{lang_code.lower()}_key_invalid.txt")
    with open(out_txt_path, "w", encoding="utf-8") as txt_file:
        string: StringEntry
        for string in strings:
            if string.key:
                if not (string.key.isalpha() and string.key.isascii()):
                    txt_file.write(f"{string.name} : \"{string.text}\"")
                    txt_file.write("\n")


def find_duplicate_keys(
        strings: list[StringEntry],
        lang_code: str) -> None:

    out_txt_path = build_abs_path(f"generated/{lang_code.lower()}_key_duplicate.txt")
    with open(out_txt_path, "w", encoding="utf-8") as txt_file:
        string: StringEntry
        for string in strings:
            if string.text.count('&') >= 2:
                txt_file.write(f"{string.name} : \"{string.text}\"")
                txt_file.write("\n")


def find_conflicts(
        command_sets: list[CommandSet],
        control_command_maps: list[CommandMap],
        selection_command_maps: list[CommandMap],
        lang_code: str) -> None:

    lang_lower: str = lang_code.lower()
    out_txt_path: Path = build_abs_path(f"generated/{lang_lower}_key_conflict.txt")

    with open(out_txt_path, "w", encoding="utf-8") as txt_file:
        command_set: CommandSet
        command_map: CommandMap
        command_button_1: CommandButton
        command_button_2: CommandButton
        conflict_count = 0

        for command_set in command_sets:
            button_count: int = len(command_set.buttons)
            for button_1_idx in range(button_count):
                command_button_1 = command_set.buttons[button_1_idx]

                if command_button_1 and command_button_1.text_string and command_button_1.text_string.key:
                    for button_2_idx in range(button_1_idx + 1, button_count):
                        command_button_2 = command_set.buttons[button_2_idx]

                        if command_button_2 and command_button_2.text_string and command_button_2.text_string.key:
                            if command_button_1.text_string.key.upper() == command_button_2.text_string.key.upper():
                                txt_file.write(f"{command_set.name} has key conflict with\n")
                                txt_file.write(f"  {button_1_idx} = {command_button_1.name} : {command_button_1.text_string.name} \"{command_button_1.text_string.text}\"\n")
                                txt_file.write(f"  {button_2_idx} = {command_button_2.name} : {command_button_2.text_string.name} \"{command_button_2.text_string.text}\"\n")
                                txt_file.write("\n")
                                conflict_count += 1

                    for command_map in selection_command_maps:
                        if command_button_1.text_string.key.upper() == command_map.key.upper():
                            if command_map.name == "SELECT_MATCHING_UNITS" and not command_set.is_unit:
                                continue
                            txt_file.write(f"{command_set.name} has key conflict with\n")
                            txt_file.write(f"  CommandMap {command_map.name} : \"{command_map.key}\"\n")
                            txt_file.write(f"  {button_1_idx} = {command_button_1.name} : {command_button_1.text_string.name} \"{command_button_1.text_string.text}\"\n")
                            txt_file.write("\n")
                            conflict_count += 1

                    if command_set.is_unit:
                        for command_map in control_command_maps:
                            if command_button_1.text_string.key.upper() == command_map.key.upper():
                                if command_map.name == "STOP" and command_button_1.name == "Command_Stop":
                                    continue
                                txt_file.write(f"{command_set.name} has key conflict with\n")
                                txt_file.write(f"  CommandMap {command_map.name} : \"{command_map.key}\"\n")
                                txt_file.write(f"  {button_1_idx} = {command_button_1.name} : {command_button_1.text_string.name} \"{command_button_1.text_string.text}\"\n")
                                txt_file.write("\n")
                                conflict_count += 1

        if conflict_count > 0:
            txt_file.write(f"{conflict_count} conflicts found")
            txt_file.write("\n")


def find_with(
        generals_str: Path,
        command_set_ini: Path,
        command_button_ini: Path,
        command_map_ini: Path,
        lang_code: str) -> None:

    out_path = build_abs_path("generated")
    out_path.mkdir(exist_ok=True)

    control_command_maps: list[CommandMap] = read_command_map_entries(command_map_ini, CommandMapCategory.CONTROL, CommandMapModifier.NONE, CommandMapUseableIn.GAME)
    selection_command_maps: list[CommandMap] = read_command_map_entries(command_map_ini, CommandMapCategory.SELECTION, CommandMapModifier.NONE, CommandMapUseableIn.GAME)

    strings: list[StringEntry] = []
    strings.extend(read_string_entries(generals_str, lang_code, "CONTROLBAR:", requires_key=False))
    strings.extend(read_string_entries(generals_str, lang_code, "UPGRADE:", requires_key=False))

    find_invalid_keys(strings, lang_code)
    find_duplicate_keys(strings, lang_code)

    strings.extend(read_string_entries(generals_str, lang_code, "OBJECT:", requires_key=False))
    strings.extend(read_string_entries(generals_str, lang_code, "GUI:", requires_key=False))

    command_buttons: list[CommandButton] = read_command_button_entries(command_button_ini, strings)
    command_sets: list[CommandSet] = read_command_set_entries(command_set_ini, command_buttons)

    dump_command_sets(command_sets, control_command_maps, selection_command_maps, lang_code)
    find_conflicts(command_sets, control_command_maps, selection_command_maps, lang_code)


def run():
    timer = Timer()

    generals_str = build_abs_path("../../../GameFilesEdited/Data/generals.str")
    command_set_ini = build_abs_path("../../../GameFilesEdited/Data/INI/CommandSet.ini")
    command_button_ini = build_abs_path("../../../GameFilesEdited/Data/INI/CommandButton.ini")
    us_command_map_ini = build_abs_path("../../../GameFilesEdited/Data/English/CommandMap.ini")
    de_command_map_ini = build_abs_path("../../../GameFilesEdited/Data/German/CommandMap.ini")
    fr_command_map_ini = build_abs_path("../../../GameFilesEdited/Data/French/CommandMap.ini")
    es_command_map_ini = build_abs_path("../../../GameFilesEdited/Data/Spanish/CommandMap.ini")
    it_command_map_ini = build_abs_path("../../../GameFilesEdited/Data/Italian/CommandMap.ini")
    ko_command_map_ini = build_abs_path("../../../GameFilesEdited/Data/Korean/CommandMap.ini")
    zh_command_map_ini = build_abs_path("../../../GameFilesEdited/Data/Chinese/CommandMap.ini")
    bp_command_map_ini = build_abs_path("../../../GameFilesEdited/Data/Brazilian/CommandMap.ini")
    pl_command_map_ini = build_abs_path("../../../GameFilesEdited/Data/Polish/CommandMap.ini")
    ru_command_map_ini = build_abs_path("../../../GameFilesEdited/Data/Russian/CommandMap.ini")
    ar_command_map_ini = build_abs_path("../../../GameFilesEdited/Data/Arabic/CommandMap.ini")
    uk_command_map_ini = build_abs_path("../../../GameFilesEdited/Data/Ukrainian/CommandMap.ini")
    sv_command_map_ini = build_abs_path("../../../GameFilesEdited/Data/Swedish/CommandMap.ini")

    assert generals_str.is_file()
    assert command_set_ini.is_file()
    assert command_button_ini.is_file()
    assert us_command_map_ini.is_file()
    assert de_command_map_ini.is_file()
    assert fr_command_map_ini.is_file()
    assert es_command_map_ini.is_file()
    assert it_command_map_ini.is_file()
    assert ko_command_map_ini.is_file()
    assert zh_command_map_ini.is_file()
    assert bp_command_map_ini.is_file()
    assert pl_command_map_ini.is_file()
    assert ru_command_map_ini.is_file()
    assert ar_command_map_ini.is_file()
    assert uk_command_map_ini.is_file()
    assert sv_command_map_ini.is_file()

    find_with(generals_str, command_set_ini, command_button_ini, us_command_map_ini, "US")
    find_with(generals_str, command_set_ini, command_button_ini, de_command_map_ini, "DE")
    find_with(generals_str, command_set_ini, command_button_ini, fr_command_map_ini, "FR")
    find_with(generals_str, command_set_ini, command_button_ini, es_command_map_ini, "ES")
    find_with(generals_str, command_set_ini, command_button_ini, it_command_map_ini, "IT")
    find_with(generals_str, command_set_ini, command_button_ini, ko_command_map_ini, "KO")
    find_with(generals_str, command_set_ini, command_button_ini, zh_command_map_ini, "ZH")
    find_with(generals_str, command_set_ini, command_button_ini, bp_command_map_ini, "BP")
    find_with(generals_str, command_set_ini, command_button_ini, pl_command_map_ini, "PL")
    find_with(generals_str, command_set_ini, command_button_ini, ru_command_map_ini, "RU")
    find_with(generals_str, command_set_ini, command_button_ini, ar_command_map_ini, "AR")
    find_with(generals_str, command_set_ini, command_button_ini, uk_command_map_ini, "UK")
    find_with(generals_str, command_set_ini, command_button_ini, sv_command_map_ini, "SV")

    print(f"Finished in {timer.GetElapsedSecondsString()} s")


if __name__ == "__main__":
    run()
