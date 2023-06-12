import os.path
from dataclasses import dataclass
from generalsmodbuilder.util import JsonFile
from generalsmodbuilder import util


@dataclass(init=False)
class Folders:
    absReleaseUnpackedDir: str
    absReleaseDir: str
    absBuildDir: str

    def __init__(self):
        self.absReleaseUnpackedDir = None
        self.absReleaseDir = None
        self.absBuildDir = None

    def Normalize(self) -> None:
        self.absReleaseUnpackedDir = os.path.normpath(self.absReleaseUnpackedDir)
        self.absReleaseDir = os.path.normpath(self.absReleaseDir)
        self.absBuildDir = os.path.normpath(self.absBuildDir)

    def VerifyTypes(self) -> None:
        util.VerifyType(self.absReleaseUnpackedDir, str, "Folders.absReleaseUnpackedDir")
        util.VerifyType(self.absReleaseDir, str, "Folders.absReleaseDir")
        util.VerifyType(self.absBuildDir, str, "Folders.absBuildDir")

    def VerifyValues(self) -> None:
        util.Verify(util.IsValidPathName(self.absReleaseUnpackedDir), f"Folders.absReleaseUnpackedDir '{self.absReleaseUnpackedDir}' is not a valid path name")
        util.Verify(util.IsValidPathName(self.absReleaseDir), f"Folders.absReleaseDir '{self.absReleaseDir}' is not a valid path name")
        util.Verify(util.IsValidPathName(self.absBuildDir), f"Folders.absBuildDir '{self.absBuildDir}' is not a valid path name")


def MakeFoldersFromJsons(jsonFiles: list[JsonFile]) -> Folders:
    folders = Folders()

    for jsonFile in jsonFiles:
        jsonDir: str = util.GetAbsSmartFileDir(jsonFile.path)
        jFolders: dict = jsonFile.data.get("folders")

        if jFolders:
            folders.absReleaseUnpackedDir = util.JoinPathIfValid(folders.absReleaseUnpackedDir, jsonDir, jFolders.get("releaseUnpackedDir"))
            folders.absReleaseDir = util.JoinPathIfValid(folders.absReleaseDir, jsonDir, jFolders.get("releaseDir"))
            folders.absBuildDir = util.JoinPathIfValid(folders.absBuildDir, jsonDir, jFolders.get("buildDir"))

    folders.VerifyTypes()
    folders.Normalize()
    folders.VerifyValues()
    return folders
