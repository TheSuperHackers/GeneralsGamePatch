import json

from ini_parser import IniFile, root

# vgla = IniFile.read(root / "Object/GLAVehicle.ini")
# print(json.dumps(vgla["GLAVehicleQuadCannon"].as_dict(), indent=4))


print(json.dumps({
    obj_name: obj.as_dict()
    for path in root.glob("Object/*.ini")
    for obj_name, obj in IniFile.read(path).items()
    if "INFANTRY" in obj["KindOf"]
}, indent=4))
