import importlib
import shutil
import subprocess
import os
import platform
import sys
from argparse import ArgumentParser
from generalsmodbuilder.__version__ import VERSIONSTR
from generalsmodbuilder import util
from glob import glob
from typing import Union


def WriteFile(path: str, data: bytes) -> None:
    if len(data) > 0:
        print(f"Write file '{path}'")
        with open(path, 'wb') as f:
            written: int = f.write(data)
            assert(written == len(data))


def __GenerateHashFiles(file: str) -> None:
    if os.path.isfile(file):
        hashDir: str = os.path.join(util.GetAbsFileDir(file), "hashes")
        hashFile: str = os.path.join(hashDir, util.GetFileName(file))
        os.makedirs(hashDir, exist_ok=True)

        md5: str = util.GetFileMd5(file)
        sha256: str = util.GetFileSha256(file)
        size: str = util.GetFileSize(file)

        WriteFile(hashFile + ".md5", str.encode(md5))
        WriteFile(hashFile + ".sha256", str.encode(sha256))
        WriteFile(hashFile + ".size", str.encode(str(size)))


def GenerateHashFiles(files: Union[str, list[str]]) -> None:
    if isinstance(files, str):
        __GenerateHashFiles(files)
    elif isinstance(files, list):
        for file in files:
            __GenerateHashFiles(file)


def ChangeDir(dir: str) -> None:
    print(f"chdir '{dir}'")
    os.chdir(dir)


class PyPackage:
    absWhl: str

    def __init__(self):
        self.absWhl = None

    def AbsDir(self) -> str:
        return os.path.dirname(self.absWhl)

    def AbsWhl(self) -> str:
        return self.absWhl

    def VerifyTypes(self) -> None:
        if self.absWhl != None:
            util.VerifyType(self.absWhl, str, "PyPackage.absWhl")

    def VerifyValues(self) -> None:
        if self.absWhl != None:
            util.Verify(os.path.isfile(self.AbsWhl()), f"PyPackage.absWhl '{self.AbsWhl()}' is not a valid file")

    def Normalize(self) -> None:
        if self.absWhl != None:
            self.absWhl = os.path.normpath(self.absWhl)


class BuildSetup:
    absVenvDir: str
    absVenvExe: str
    packages: list[PyPackage]
    pipInstalls: list[str]

    def __init__(self):
        self.absVenvDir = None
        self.absVenvExe = None
        self.packages = list[PyPackage]()
        self.pipInstalls = list[str]()

    def VerifyTypes(self) -> None:
        util.VerifyType(self.absVenvDir, str, "BuildSetup.absVenvDir")
        util.VerifyType(self.absVenvExe, str, "BuildSetup.absVenvExe")
        util.VerifyType(self.packages, list, "BuildSetup.packages")
        util.VerifyType(self.pipInstalls, list, "BuildSetup.pipInstalls")
        for package in self.packages:
            util.VerifyType(package, PyPackage, "BuildSetup.packages")
            package.VerifyTypes()
        for name in self.pipInstalls:
            util.VerifyType(name, str, "BuildSetup.pipInstalls")

    def VerifyValues(self) -> None:
        for package in self.packages:
            package.VerifyValues()

    def Normalize(self) -> None:
        self.absVenvDir = os.path.normpath(self.absVenvDir)
        self.absVenvExe = os.path.normpath(self.absVenvExe)
        for package in self.packages:
            package.Normalize()


class BuildStep:
    absDir: str
    name: str
    setup: BuildSetup
    config: dict

    def __init__(self):
        self.absDir = None
        self.name = None
        self.setup = None
        self.config = dict()

    def MakeAbsPath(self, relPath: str) -> str:
        util.VerifyType(relPath, str, "relPath")
        path: str = os.path.join(self.absDir, relPath)
        path = os.path.normpath(path)
        return path

    def VerifyTypes(self) -> None:
        util.VerifyType(self.absDir, str, "BuildStep.absDir")
        util.VerifyType(self.name, str, "BuildStep.name")
        util.VerifyType(self.setup, BuildSetup, "BuildSetup.setup")
        util.VerifyType(self.config, dict, "BuildSetup.config")
        self.setup.VerifyTypes()

    def VerifyValues(self) -> None:
        util.Verify(os.path.isdir(self.absDir), f"BuildStep.absDir '{self.absDir}' is not an valid path")
        util.Verify(self.name, "BuildStep.name must not be empty")
        self.setup.VerifyValues()

    def Normalize(self) -> None:
        self.setup.Normalize()


BuildStepsT = list[BuildStep]


def __MakeBuildJsonPath() -> str:
    return os.path.join(util.GetAbsFileDir(__file__), "build.json")


def __MakeBuildSetupFromDict(jSetup: dict, absDir: str) -> BuildSetup:
    buildSetup = BuildSetup()
    buildSetup.pipInstalls = jSetup.get("pipInstalls")
    platfrm: str = sys.platform.lower()
    machine: str = platform.machine().lower()
    jPlatform: dict = jSetup.get(platfrm)

    if jPlatform:
        buildSetup.absVenvDir = util.JoinPathIfValid(None, absDir, jPlatform.get("venvDir"))
        buildSetup.absVenvExe = util.JoinPathIfValid(None, absDir, jPlatform.get("venvExe"))
        jMachine: dict = jPlatform.get(machine)

        if jMachine:
            jPackages: list[str] = jMachine.get("packages")

            if jPackages:
                jPackage: str
                for jPackage in jPackages:
                    package = PyPackage()
                    package.absWhl = util.JoinPathIfValid(None, absDir, jPackage)
                    buildSetup.packages.append(package)

    return buildSetup


def __MakeBuildStepFromDict(jStep: dict, absDir: str) -> BuildStep:
    buildStep = BuildStep()
    buildStep.absDir = absDir
    buildStep.name = jStep.get("name")
    buildStep.config = jStep.get("config")
    jSetup: dict = jStep.get("setup")
    if jSetup:
        buildStep.setup = __MakeBuildSetupFromDict(jSetup, absDir)

    return buildStep


def __MakeBuildStepsFromJson(jsonFile: util.JsonFile) -> BuildStepsT:
    buildStep: BuildStep
    buildSteps = BuildStepsT()
    jBuild: dict = jsonFile.data.get("build")

    if jBuild:
        jsonDir: str = os.path.dirname(jsonFile.path)
        jSteps: list = jBuild.get("steps")
        jStep: dict

        if jSteps:
            for jStep in jSteps:
                buildStep = __MakeBuildStepFromDict(jStep, jsonDir)
                buildSteps.append(buildStep)

    for buildStep in buildSteps:
        buildStep.VerifyTypes()
        buildStep.Normalize()
        buildStep.VerifyValues()

    return buildSteps


def __Run(exec: str, *args) -> None:
    strArgs: list[str] = [exec]
    for arg in args:
        if str(arg):
            strArgs.append(str(arg))
    subprocess.run(args=strArgs, check=True)


def __RunAndCapture(exec: str, *args) -> str:
    strArgs: list[str] = [exec]
    for arg in args:
        if str(arg):
            strArgs.append(str(arg))
    outputBytes: bytes = subprocess.run(args=strArgs, check=True, capture_output=True).stdout
    outputStr: str = outputBytes.decode(sys.stdout.encoding)
    outputStr = outputStr.strip("\r\n")
    return outputStr


def __CreateVenv(buildStep: BuildStep) -> None:
    print(f"Create venv for '{buildStep.name}' at '{buildStep.setup.absVenvDir}' with '{sys.executable}' ...")
    __Run(sys.executable, "-m", "venv", buildStep.setup.absVenvDir)


def __InstallPackages(buildStep: BuildStep) -> None:
    print(f"Install packages for '{buildStep.name}' ...")
    package: PyPackage
    name: str

    for package in buildStep.setup.packages:
        __Run(buildStep.setup.absVenvExe, "-m", "pip", "install", package.AbsWhl(), "--no-index", "--find-links", package.AbsDir())

    for name in buildStep.setup.pipInstalls:
        __Run(buildStep.setup.absVenvExe, "-m", "pip", "install", name)


def __RunPoetry(buildStep: BuildStep) -> None:
    print(f"Run {buildStep.name} ...")

    workDir: str = os.getcwd()
    projDir: str = buildStep.MakeAbsPath(buildStep.config.get("projDir"))

    ChangeDir(projDir)

    try:
        # There is a bug in Poetry where it will not install packages into the virtual env,
        # if the virtual env was created freshly during "poetry install" command.
        # To trigger virtual env first, run innocent "poetry run python -V" here.
        __Run(buildStep.setup.absVenvExe, "-m", "poetry", "run", "python", "-V")
        # Install packages into Poetry's virtual env.
        __Run(buildStep.setup.absVenvExe, "-m", "poetry", "install")
        # Get virtual env path created by poetry.
        venvDir: str = __RunAndCapture(buildStep.setup.absVenvExe, "-m", "poetry", "env", "info", "--path")
        print(f"Poetry created venv '{venvDir}'")
    finally:
        ChangeDir(workDir)


def __RunPyInstaller(buildStep: BuildStep) -> None:
    print(f"Run {buildStep.name} ...")

    config: dict = buildStep.config

    workDir: str = os.getcwd()
    exeName: str = config.get("exeName")
    codeDir: str = buildStep.MakeAbsPath(config.get("codeDir"))
    codeFile: str = config.get("codeFile")
    distDir: str = buildStep.MakeAbsPath(config.get("distDir"))
    buildDir: str = buildStep.MakeAbsPath(config.get("buildDir"))
    makeArchive: bool = config.get("makeArchive")
    archiveDir: str = buildStep.MakeAbsPath(config.get("archiveDir"))
    rawImportDirs: list[str] = config.get("importDirs")
    rawDataFiles: list[dict] = config.get("dataFiles")
    pathsArgs = list[str]()
    addDataArgs = list[str]()

    rawImportDir: str
    for rawImportDir in rawImportDirs:
        dir: str = buildStep.MakeAbsPath(rawImportDir)
        pathsArgs.append("--paths")
        pathsArgs.append(dir)

    rawDataFile: dict
    for rawDataFile in rawDataFiles:
        src: str = buildStep.MakeAbsPath(rawDataFile.get("src"))
        dst: str = os.path.normpath(rawDataFile.get("dst"))
        addDataArgs.append("--add-data")
        addDataArgs.append(f"{src}{os.pathsep}{dst}")

    ChangeDir(codeDir)

    try:
        __Run(buildStep.setup.absVenvExe, "-m", "PyInstaller", codeFile,
            "--name", exeName,
            "--distpath", distDir,
            "--workpath", buildDir,
            "--specpath", buildDir,
            "--clean",
            "--onedir",
            "--noconfirm",
            *pathsArgs,
            *addDataArgs)
    finally:
        ChangeDir(workDir)

    postDeleteFiles: list[str] = config.get("postDeleteFiles")
    if postDeleteFiles:
        for file in postDeleteFiles:
            absFile: str = buildStep.MakeAbsPath(file)
            if "*" in absFile and not os.path.isfile(absFile):
                globFiles: list[str] = glob(absFile, recursive=True)
                for globFile in globFiles:
                    print(f"Delete '{globFile}'")
                    util.DeleteFileOrDir(globFile)
            else:
                print(f"Delete '{absFile}'")
                util.DeleteFileOrDir(absFile)

    if makeArchive:
        outBaseName: str = exeName + "_v" + VERSIONSTR
        __BuildArchives(inDir=distDir, outDir=archiveDir, outBaseName=outBaseName)


def __BuildArchives(inDir: str, outDir: str, outBaseName: str) -> None:
    print(f"Create archives in '{outDir}' ...")

    os.makedirs(outDir, exist_ok=True)

    absBaseName = os.path.join(outDir, outBaseName)
    x7z: str = os.path.join(util.GetAbsFileDir(__file__), "windows", "7z.exe")

    if os.name == "nt" and os.path.isfile(x7z):
        x7zInDir: str = os.path.join(inDir, "*")
        util.DeleteFileOrDir(absBaseName + ".7z")
        util.DeleteFileOrDir(absBaseName + ".zip")
        __Run(x7z, "a", "-t7z", "-mx9", absBaseName + ".7z", x7zInDir)
        __Run(x7z, "a", "-tzip", "-mx9", absBaseName + ".zip", x7zInDir)
        GenerateHashFiles(absBaseName + ".7z")
        GenerateHashFiles(absBaseName + ".zip")
    else:
        shutil.make_archive(base_name=absBaseName, format="zip", root_dir=inDir)
        shutil.make_archive(base_name=absBaseName, format="gztar", root_dir=inDir)
        GenerateHashFiles(absBaseName + ".zip")
        GenerateHashFiles(absBaseName + ".gztar")


def ProcessStep(buildStep: BuildStep) -> None:
    __CreateVenv(buildStep)
    __InstallPackages(buildStep)

    if buildStep.name == "poetry":
        __RunPoetry(buildStep)
    elif buildStep.name == "PyInstaller":
        __RunPyInstaller(buildStep)


def Main(args=None) -> None:
    print(f"Generals Mod Builder v{VERSIONSTR} venv setup and build")

    timer = util.Timer()

    parser = ArgumentParser()
    parser.add_argument('-b', '--build-definition-file', type=str, default=None, help='The build definition json file.')

    args, unknownargs = parser.parse_known_args(args=args)

    buildDefinitionFile: str = args.build_definition_file
    if buildDefinitionFile:
        buildDefinitionFile = os.path.normpath(buildDefinitionFile)
    else:
        buildDefinitionFile = __MakeBuildJsonPath()

    buildJson = util.JsonFile(buildDefinitionFile)
    buildSteps: BuildStepsT = __MakeBuildStepsFromJson(buildJson)
    buildStep: BuildStep

    for buildStep in buildSteps:
        ProcessStep(buildStep)

    print(f"Generals Mod Builder v{VERSIONSTR} venv setup and build completed in {timer.GetElapsedSecondsString()} s")


if __name__ == "__main__":
    Main()
