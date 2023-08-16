import json
from pathlib import Path
from pprint import pprint

from ini_parser import IniFile, root

vgla = IniFile.read(root / "Object/GLAVehicle.ini")
demogen = IniFile.read(root / "Object/DemoGeneral.ini")

print(json.dumps(vgla["GLAVehicleQuadCannon"].as_dict(), indent=4))
print(json.dumps(demogen["Demo_GLAVehicleQuadCannon"].as_dict(), indent=4))
