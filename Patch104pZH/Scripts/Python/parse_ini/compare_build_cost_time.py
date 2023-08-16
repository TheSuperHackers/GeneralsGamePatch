import json
from pathlib import Path

from ini_parser import IniFile, root

command_buttons = IniFile.read(root / "CommandButton.ini")

buildable_units = {
    button["Object"]
    for button_name, button in command_buttons.items()
    if button["Command"] == "UNIT_BUILD"
}

print(json.dumps({
    obj_name: f'${obj["BuildCost"]} @ {obj["BuildTime"]} seconds'
    for path in root.glob("Object/*.ini")
    for obj_name, obj in IniFile.read(path).items()
    if obj_name in buildable_units
}, indent=4))

root_original = Path("../../../GameFilesOriginalZH/Data/ini")

print(json.dumps({
    obj_name: f'${obj["BuildCost"]} @ {obj["BuildTime"]} seconds'
    for path in root_original.glob("Object/*.ini")
    for obj_name, obj in IniFile.read(path).items()
    if obj_name in buildable_units
}, indent=4))
