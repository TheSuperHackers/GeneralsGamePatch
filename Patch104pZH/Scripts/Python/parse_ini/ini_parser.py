import shlex
from pathlib import Path
from pprint import pprint

import syntax
from syntax import Draw, ModuleTemplate

root = Path("../../../GameFilesEdited/Data/ini")
# file = root / "Default/Object.ini"
# file = root / "Object/CivilianUnit.ini"
# file = root / "Object/AmericaInfantry.ini"
# file = root / "Object/AirforceGeneral.ini"
# file = root / "Object/SuperWeaponGeneral.ini"
# file = root / "Object/LaserGeneral.ini"
# file = root / "Object/ChinaInfantry.ini"
# file = root / "Object/InfantryGeneral.ini"  # @todo, cont
# file = root / "CommandButton.ini"
# file = root / "CommandSet.ini"
# file = root / "Default/Object.ini"
# file = root / "Crate.ini"
# file = root / "Object/DemoGeneral.ini"
# file = root / "Object/AmericaInfantry.ini"


def tokenize(stream):
    for lineno, line in enumerate(stream.readlines(), 1):
        lexer = shlex.shlex(line)
        lexer.commenters = [";", "//"]
        lexer.wordchars += ".:%-"
        lexer.whitespace += "="

        if tokens := list(lexer):
            yield lineno, line, tokens


class IniFile(ModuleTemplate):
    token = "File"
    CommandButton = syntax.CommandButton
    CommandSet = syntax.CommandSet
    Object = syntax.Object
    ObjectReskin = Object
    CrateData = syntax.CrateData

    @classmethod
    def read(cls, file):
        stream = open(file, "r")

        context = []
        _, ini = IniFile(context)

        for lineno, line, tokens in tokenize(stream):
            try:
                context[-1].parse(context, tokens)
            except Exception as exc:
                exc.add_note(f"    Context: {context}")
                exc.add_note(f"    Tokens: {tokens}")
                exc.add_note(f"    File: {file.name}  Line {lineno}:")
                exc.add_note(line)
                raise exc
        return ini
