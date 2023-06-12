import certifi
import http.client
import os
import os.path
import ssl
import urllib.request
import zipfile
from enum import Enum, auto
from dataclasses import dataclass
from generalsmodbuilder import util
from generalsmodbuilder.util import JsonFile
from generalsmodbuilder.data.common import ParamsT, VerifyParamsType
from generalsmodbuilder.build.common import ParamsToArgs


class InstallResultCode(Enum):
    Ok = auto()
    NoInstall = auto()
    SizeMismatch = auto()
    HashMismatch = auto()
    HttpError = auto()
    CallError = auto()


@dataclass
class InstallResult:
    code: InstallResultCode
    httpCode: int

    def Ok(self) -> bool:
        return self.code == InstallResultCode.Ok


@dataclass(init=False)
class ToolCallInstruction:
    absCall: str
    callArgs: ParamsT


    def __init__(self):
        self.absCall = ""
        self.callArgs = ParamsT


    def Normalize(self) -> None:
        if self.absCall:
            self.absCall = os.path.normpath(self.absCall)


    def VerifyTypes(self) -> None:
        util.VerifyType(self.absCall, str, "ToolCallInstruction.absCall")
        VerifyParamsType(self.callArgs, "ToolCallInstruction.callArgs")


    def VerifyValues(self) -> None:
        if self.absCall:
            util.Verify(util.IsValidPathName(self.absCall), f"ToolCallInstruction.absCall '{self.absCall}' is not a valid file name")


@dataclass(init=False)
class ToolFile:
    url: str
    absTarget: str
    absExtractDir: str
    md5: str
    sha256: str
    size: int
    callInstructions: list[ToolCallInstruction]
    runnable: bool
    autoDeleteAfterInstall: bool
    skipIfRunnableExists: bool
    isInstalledCached: bool


    def __init__(self):
        self.url = ""
        self.absTarget = None
        self.absExtractDir = ""
        self.md5 = ""
        self.sha256 = ""
        self.size = -1
        self.callInstructions = list[ToolCallInstruction]()
        self.runnable = False
        self.autoDeleteAfterInstall = False
        self.skipIfRunnableExists = False
        self.isInstalledCached = False


    def Normalize(self) -> None:
        if self.absTarget:
            self.absTarget = os.path.normpath(self.absTarget)
        if self.absExtractDir:
            self.absExtractDir = os.path.normpath(self.absExtractDir)
        for instruction in self.callInstructions:
            instruction.Normalize()


    def VerifyTypes(self) -> None:
        util.VerifyType(self.url, str, "ToolFile.url")
        util.VerifyType(self.absTarget, str, "ToolFile.absTarget")
        util.VerifyType(self.absExtractDir, str, "ToolFile.absExtractDir")
        util.VerifyType(self.md5, str, "ToolFile.md5")
        util.VerifyType(self.sha256, str, "ToolFile.sha256")
        util.VerifyType(self.size, int, "ToolFile.size")
        util.VerifyType(self.callInstructions, list, "ToolFile.callInstructions")
        util.VerifyType(self.runnable, bool, "ToolFile.runnable")
        util.VerifyType(self.autoDeleteAfterInstall, bool, "ToolFile.autoDeleteAfterInstall")
        util.VerifyType(self.skipIfRunnableExists, bool, "ToolFile.skipIfRunnableExists")
        for instruction in self.callInstructions:
            instruction.VerifyTypes()


    def VerifyValues(self) -> None:
        # TODO Verify url format?
        util.Verify(util.IsValidPathName(self.absTarget), f"ToolFile.absTarget '{self.absTarget}' is not a valid file name")
        if self.absExtractDir:
            util.Verify(util.IsValidPathName(self.absExtractDir), f"ToolFile.absExtractDir '{self.absExtractDir}' is not a valid file name")
        for instruction in self.callInstructions:
            instruction.VerifyValues()


    def VerifyInstall(self) -> None:
        util.Verify(os.path.isfile(self.absTarget), f"ToolFile.absTarget file '{self.absTarget}' does not exist")
        if self.md5:
            actual: str = util.GetFileMd5(self.absTarget)
            util.Verify(self.md5 == actual, f"ToolFile.md5 '{self.md5}' does not match md5 '{actual}' of target file '{self.absTarget}'")
        if self.sha256:
            actual: str = util.GetFileSha256(self.absTarget)
            util.Verify(self.md5 == actual, f"ToolFile.sha256 '{self.md5}' does not match sha256 '{actual}' of target file '{self.absTarget}'")
        if self.size >= 0:
            actual: int = util.GetFileSize(self.absTarget)
            util.Verify(self.size == actual, f"ToolFile.size '{self.size}' does not match size '{actual}' of target file '{self.absTarget}'")


    def HashOk(self) -> bool:
        md5Ok = (not self.md5 or self.md5 == util.GetFileMd5(self.absTarget))
        shaOk = (not self.sha256 or self.sha256 == util.GetFileSha256(self.absTarget))
        return md5Ok and shaOk


    def SizeOk(self) -> bool:
        return self.size < 0 or self.size == util.GetFileSize(self.absTarget)


    def IsInstalled(self) -> bool:
        if self.isInstalledCached:
            return True
        self.isInstalledCached = os.path.isfile(self.absTarget) and self.SizeOk() and self.HashOk()
        return self.isInstalledCached


    def Install(self) -> InstallResult:
        result = InstallResult(InstallResultCode.Ok, 0)

        if not self.IsInstalled():
            result = InstallResult(InstallResultCode.NoInstall, 0)

        if not result.Ok():
            if self.url:
                print(f"Downloading from '{self.url}' ...")
                response: http.client.HTTPResponse
                cafile: str = certifi.where()
                print(f"Using cafile '{cafile}'")
                context: ssl.SSLContext = ssl.create_default_context(cafile=cafile)
                with urllib.request.urlopen(self.url, context=context) as response:
                    if response.code == 200:
                        sizeOk: bool = self.size < 0
                        len: str = response.headers['Content-Length']

                        if not sizeOk:
                            sizeOk = len and int(len) == self.size

                        if sizeOk:
                            size = int(len) if len else self.size
                            print(f"Downloading {int(size / 1024)} kb to '{self.absTarget}' ...")
                            util.MakeDirsForFile(self.absTarget)
                            ToolFile.DownloadToFile(response, self.absTarget)
                            if self.IsInstalled():
                                result = InstallResult(InstallResultCode.Ok, response.code)
                            elif not self.SizeOk():
                                result = InstallResult(InstallResultCode.SizeMismatch, response.code)
                            elif not self.HashOk():
                                result = InstallResult(InstallResultCode.HashMismatch, response.code)
                        else:
                            result = InstallResult(InstallResultCode.SizeMismatch, response.code)
                    else:
                        result = InstallResult(InstallResultCode.HttpError, response.code)

        if result.Ok():
            if self.absExtractDir:
                os.makedirs(self.absExtractDir, exist_ok=True)
                if util.HasFileExt(self.absTarget, "zip"):
                    with zipfile.ZipFile(self.absTarget, "r") as zfile:
                        zfile.extractall(self.absExtractDir)

        if result.Ok():
            instruction: ToolCallInstruction
            for instruction in self.callInstructions:
                if instruction.absCall:
                    args: list[str] = [instruction.absCall]
                    args.extend(ParamsToArgs(instruction.callArgs))
                    if not util.RunProcess(args):
                        result = InstallResult(InstallResultCode.CallError, 0)

        if result.Ok():
            if self.autoDeleteAfterInstall:
                util.DeleteFile(self.absTarget)

        return result


    @staticmethod
    def DownloadToFile(response: http.client.HTTPResponse, absTarget: str) -> None:
        BUF_SIZE = 1024 * 64
        with open(absTarget, 'wb', buffering=BUF_SIZE) as wfile:
            fullbuf = bytearray(BUF_SIZE)
            while True:
                readsize: int = response.readinto(fullbuf)
                if readsize == 0:
                    break
                if readsize != BUF_SIZE:
                    readbuf: bytearray = fullbuf[:readsize]
                    wfile.write(readbuf)
                    break
                else:
                    wfile.write(fullbuf)


@dataclass(init=False)
class Tool:
    name: str
    files: list[ToolFile]
    version: float
    versionStr: str


    def __init__(self):
        self.name = None
        self.files = list[ToolFile]()
        self.version = 0.0
        self.versionStr = ""


    def Normalize(self) -> None:
        for file in self.files:
            file.Normalize()


    def VerifyTypes(self) -> None:
        util.VerifyType(self.name, str, "Tool.name")
        util.VerifyType(self.version, float, "Tool.version")
        util.VerifyType(self.versionStr, str, "Tool.versionStr")
        util.VerifyType(self.files, list, "Tool.files")
        for file in self.files:
            file.VerifyTypes()


    def VerifyValues(self) -> None:
        util.Verify(self.GetExecutable() != None, "Tool.files contains no runnable file")
        for file in self.files:
            file.VerifyValues()


    def VerifyInstall(self) -> None:
        for file in self.files:
            file.VerifyInstall()


    def GetExecutable(self) -> str:
        file: ToolFile
        for file in self.files:
            if file.runnable:
                return file.absTarget
        return None


    def Install(self) -> bool:
        file: ToolFile
        success: bool = True
        runnablesInstalled: int = 0

        for file in self.files:
            if file.runnable and file.IsInstalled():
                runnablesInstalled += 1

        for file in self.files:
            if file.skipIfRunnableExists and runnablesInstalled > 0:
                continue
            result: InstallResult = file.Install()
            if result.Ok():
                print(f"Tool '{self.name} {self.versionStr}' file '{file.absTarget}' is installed")
                if file.absExtractDir:
                    print(f"File '{file.absTarget}' is extracted to '{file.absExtractDir}'")
            else:
                msg: str = f"Tool '{self.name} {self.versionStr}' file '{file.absTarget}' was not installed"
                if result.code == InstallResultCode.SizeMismatch:
                    msg += " - Size mismatch was detected"
                elif result.code == InstallResultCode.HashMismatch:
                    msg += " - Hash mismatch was detected"
                elif result.code == InstallResultCode.HttpError:
                    msg += " - Http returned error code {result.httpCode}"
                elif result.code == InstallResultCode.CallError:
                    msg += " - Error on call instruction"
                raise RuntimeError(msg)

        return success




ToolsT = dict[str, Tool]


def __ProcessAliases(thing: str | ParamsT, aliases: dict) -> str | ParamsT:
    if isinstance(aliases, dict):

        if isinstance(thing, str):
            for aliasKey, aliasVal in aliases.items():
                thing = thing.replace(aliasKey, aliasVal)

        if isinstance(thing, dict):
            for thingKey, thingVal in thing.items():
                for aliasKey, aliasVal in aliases.items():
                    thingVal = thingVal.replace(aliasKey, aliasVal)
                thing[thingKey] = thingVal

    return thing


def __MakeToolFileFromDict(jFile: dict, rootDir: str, aliases: dict) -> ToolFile:
    toolFile = ToolFile()

    toolFile.url = jFile.get("url", toolFile.url)
    toolFile.absTarget = util.JoinPathIfValid(None, rootDir, jFile.get("target"))
    toolFile.absExtractDir = util.JoinPathIfValid(toolFile.absExtractDir, rootDir, jFile.get("extractDir"))
    toolFile.md5 = jFile.get("md5", toolFile.md5)
    toolFile.sha256 = jFile.get("sha256", toolFile.sha256)
    toolFile.size = jFile.get("size", toolFile.size)
    jCallList: list = jFile.get("callList", None)
    toolFile.runnable = jFile.get("runnable", toolFile.runnable)
    toolFile.autoDeleteAfterInstall = jFile.get("autoDeleteAfterInstall", toolFile.autoDeleteAfterInstall)
    toolFile.skipIfRunnableExists = jFile.get("skipIfRunnableExists", toolFile.skipIfRunnableExists)

    toolFile.absTarget = __ProcessAliases(toolFile.absTarget, aliases)
    toolFile.absExtractDir = __ProcessAliases(toolFile.absExtractDir, aliases)

    if jCallList is not None:
        toolFile.callInstructions.clear()
        jCall: dict
        for jCall in jCallList:
            instruction = ToolCallInstruction()
            instruction.absCall = util.JoinPathIfValid(instruction.absCall, rootDir,jCall.get("call", instruction.absCall))
            instruction.callArgs = jCall.get("callArgs", instruction.callArgs)
            instruction.absCall = __ProcessAliases(instruction.absCall, aliases)
            instruction.callArgs = __ProcessAliases(instruction.callArgs, aliases)
            toolFile.callInstructions.append(instruction)

    return toolFile


def __MakeToolFromDict(jTool: dict, rootDir: str, jVersion: int, aliases: dict) -> Tool:
    tool = Tool()
    tool.name = jTool.get("name")
    if jVersion <= 1:
        tool.version = jTool.get("version", tool.version)
    else:
        tool.versionStr = jTool.get("version", tool.versionStr)

    jFiles: dict = jTool.get("files")
    if jFiles:
        jFile: dict
        for jFile in jFiles:
            toolFile = __MakeToolFileFromDict(jFile, rootDir, aliases)
            tool.files.append(toolFile)

    return tool


def MakeToolsFromJsons(jsonFiles: list[JsonFile], rootDir: str=None) -> ToolsT:
    tools = ToolsT()
    tool: Tool

    for jsonFile in jsonFiles:
        jTools: dict = jsonFile.data.get("tools")
        if jTools:
            LATEST_VERSION = 2
            jVersion: int = jTools.get("version", LATEST_VERSION)
            jsonDir: str = util.GetAbsSmartFileDir(jsonFile.path)
            if not rootDir:
                rootDir = jsonDir
            aliases: dict = {
                "{THIS_DIR}": jsonDir,
                "{ROOT_DIR}": rootDir
            }
            if jAliases := jTools.get("aliases"):
                aliases.update(jAliases)
            jList: dict = jTools.get("list")
            if jList:
                jTool: dict
                for jTool in jList:
                    tool = __MakeToolFromDict(jTool, rootDir, jVersion, aliases)
                    tools[tool.name] = tool

    for tool in tools.values():
        tool.VerifyTypes()
        tool.Normalize()
        tool.VerifyValues()

    return tools


def InstallTools(tools: ToolsT) -> bool:
    tool: Tool
    success: bool = True
    for tool in tools.values():
        if not tool.Install():
            success = False
    return success
