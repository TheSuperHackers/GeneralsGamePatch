import os
import subprocess
import sys
import time
import types
import winreg
import json
import hashlib
import pickle
import shutil
from copy import copy
from typing import Any, Callable, Union


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


PERFORMANCE_TIMER_THRESHOLD = 0.01


def Verify(condition: bool, message: str = "") -> None:
    if not condition:
        raise AssertionError(message)


def VerifyType(obj: object, expectedType: type | types.UnionType, objName: str) -> None:
    if not isinstance(obj, expectedType):
        raise AssertionError(f'Object "{objName}" is type:{type(obj).__name__} but should be type:{expectedType.__name__}')


def GetCheckedOptional(dictionary: dict, key: str, expectedTypeIfExists: type | types.UnionType) -> Any:
    value: Any = dictionary.get(key)
    if value != None:
        VerifyType(value, expectedTypeIfExists, key)
    return value


def GetCheckedMandatory(dictionary: dict, key: str, expectedType: type | types.UnionType) -> Any:
    value: Any = dictionary.get(key)
    VerifyType(value, expectedType, key)
    return value


def pprint(obj: Any) -> None:
    try:
        # Is imported here because it is not part of standard Python.
        from beeprint import pp as beeprintpp
        beeprintpp(
            obj,
            max_depth=10,
            dict_ordered_key_enable=False,
            instance_repr_enable=False,
            list_in_line=False,
            tuple_in_line=False,
            string_break_enable=False)
    except ImportError:
        pass


def LoadPickle(path: str) -> Any:
    print(f"Read pickle {path} ...")
    timer = Timer()
    data: Any = None
    with open(path, "rb") as rfile:
        data = pickle.load(rfile)
    if timer.GetElapsedSeconds() > PERFORMANCE_TIMER_THRESHOLD:
        print(f"Read pickle {path} completed in {timer.GetElapsedSecondsString()} s")
    return data


def SavePickle(path: str, data: Any) -> None:
    print(f"Write pickle {path} ...")
    timer = Timer()
    MakeDirsForFile(path)
    with open(path, "wb") as wfile:
        pickle.dump(data, wfile, protocol=pickle.HIGHEST_PROTOCOL)
    if timer.GetElapsedSeconds() > PERFORMANCE_TIMER_THRESHOLD:
        print(f"Write pickle {path} completed in {timer.GetElapsedSecondsString()} s")


def ReadJson(path: str) -> dict:
    print(f"Read json {path} ...")
    timer = Timer()
    data: dict = None
    with open(path, "rb") as rfile:
        text = rfile.read()
        data = json.loads(text)
    if timer.GetElapsedSeconds() > PERFORMANCE_TIMER_THRESHOLD:
        print(f"Read json {path} completed in {timer.GetElapsedSecondsString()} s")
    return data


def ReadYaml(path: str) -> dict:
    # Is imported here because it is not part of standard Python.
    from yaml import safe_load
    print(f"Read yaml {path} ...")
    timer = Timer()
    data: dict = None
    with open(path, "rb") as rfile:
        text = rfile.read()
        data = safe_load(text)
    if timer.GetElapsedSeconds() > PERFORMANCE_TIMER_THRESHOLD:
        print(f"Read yaml {path} completed in {timer.GetElapsedSecondsString()} s")
    return data


class JsonFile:
    path: str
    data: dict

    def __init__(self, path: str):
        self.path = os.path.normpath(path)
        self.data = ReadJson(path)
        self.VerifyTypes()

    def VerifyTypes(self) -> None:
        VerifyType(self.path, str, "JsonFile.path")
        VerifyType(self.data, dict, "JsonFile.data")


class YamlFile:
    path: str
    data: dict

    def __init__(self, path: str):
        self.path = os.path.normpath(path)
        self.data = ReadYaml(path)
        self.VerifyTypes()

    def VerifyTypes(self) -> None:
        VerifyType(self.path, str, "YamlFile.path")
        VerifyType(self.data, dict, "YamlFile.data")


def GetRegKeyValue(path, root=winreg.HKEY_LOCAL_MACHINE) -> Union[int, str, None]:
    path, name = str.split(path, sep=':')
    try:
        with winreg.OpenKey(root, path, 0, winreg.KEY_READ|winreg.KEY_WOW64_32KEY) as key:
            valuePair = winreg.QueryValueEx(key, name)
            if valuePair:
                print(f"Get registry key {path} : {name} as '{valuePair[0]}'")
                return valuePair[0]
            return None
    except OSError:
        return None


def SetRegKeyValue(path: str, value: Union[int, str], root=winreg.HKEY_LOCAL_MACHINE, regtype=None) -> bool:
    try:
        path, name = str.split(path, sep=':')
        with winreg.OpenKey(root, path, 0, winreg.KEY_WRITE|winreg.KEY_READ|winreg.KEY_WOW64_32KEY) as key:
            if regtype == None:
                regtype = winreg.QueryValueEx(key, name)[1]
            if regtype == None:
                if isinstance(value, int):
                    regtype = winreg.REG_DWORD
                else:
                    regtype = winreg.REG_SZ
            if regtype == winreg.REG_SZ:
                value = str(value)
            winreg.SetValueEx(key, name, 0, regtype, value)
            print(f"Set registry key {path} : {name} to '{value}'")
            return True
    except OSError:
        return False


def GetSubdirsAndFilesRecursively(dir: str) -> tuple[list, list]:
    subdirs, files = [], []

    if os.path.isdir(dir):
        for f in os.scandir(dir):
            if f.is_dir():
                subdirs.append(f.path)
            elif f.is_file():
                files.append(f.path)

    for subdir in list(subdirs):
        rsubdirs, rfiles = GetSubdirsAndFilesRecursively(subdir)
        subdirs.extend(rsubdirs)
        files.extend(rfiles)

    return subdirs, files


def GetAbsFileDir(file: str) -> str:
    fdir: str
    fdir = os.path.dirname(file)
    fdir = os.path.abspath(fdir)
    return fdir


g_isFrozen: bool = getattr(sys, 'frozen', False)

def GetAbsSmartFileDir(file: str) -> str:
    # If this code is frozen and the given file is part of it, then use the executable file dir.
    fileDir: str = GetAbsFileDir(file)
    if g_isFrozen:
        thisDir = os.path.dirname(__file__)
        if fileDir.startswith(thisDir):
            return os.path.dirname(sys.executable)
    return fileDir


g_appDir: str = GetAbsSmartFileDir(__file__)


def GetAbsFileDirs(file: str, absStopPath: str = "") -> list[str]:
    absStopPath = os.path.normpath(absStopPath)
    paths: list[str] = list()
    path1: str = GetAbsFileDir(file)
    path2: str = ""
    while path1 != absStopPath and path2 != path1:
        path2 = path1
        paths.append(path2)
        path1 = os.path.normpath(os.path.join(path2, ".."))
    return paths


def GetFileName(filepath: str) -> str:
    path, file = os.path.split(filepath)
    return file


def GetFileNameNoExt(filepath: str) -> str:
    path, file = os.path.split(filepath)
    name, ext = os.path.splitext(file)
    return name


def GetFileExt(filepath: str) -> str:
    path, ext = os.path.splitext(filepath)
    if ext and ext[0] == '.':
        ext = ext[1:]
    return ext


def GetFileDir(filepath: str) -> str:
    path, file = os.path.split(filepath)
    return path


def GetFileDirAndName(filepath: str) -> str:
    path, ext = os.path.splitext(filepath)
    return path


def HasFileExt(file: str, expectedExt: str) -> bool:
    fileExt: str = GetFileExt(file)
    return fileExt.lower() == expectedExt.lower()


def HasAnyFileExt(file: str, expectedExtList: list[str]) -> bool:
    ext: str
    for ext in expectedExtList:
        if HasFileExt(file, ext):
            return True
    return False


def CreateRelPaths(paths: list[str], start: str) -> list[str]:
    relPaths = copy(paths)
    for i in range(len(relPaths)):
        relPaths[i] = os.path.relpath(path=relPaths[i], start=start)
    return relPaths


def MakeDirsForFile(file: str) -> None:
    os.makedirs(GetAbsFileDir(file), exist_ok=True)


# This implementation is
# - about 25% faster than testing os.path.islink, os.path.isfile before unlink or remove.
# - about 10% faster than unlink with a new pathlib.Path instance.
def DeleteFile(path: str) -> bool:
    """
    Delete file or symlink.
    """
    try:
        os.unlink(path)
        return True
    except OSError:
        pass
    try:
        os.remove(path)
        return True
    except OSError:
        pass
    return False


def DeleteFileOrDir(path: str) -> bool:
    """
    Delete file, symlink or directory tree.
    """
    try:
        os.unlink(path)
        return True
    except OSError:
        pass
    try:
        os.remove(path)
        return True
    except OSError:
        pass
    try:
        shutil.rmtree(path)
        return True
    except OSError:
        pass
    return False


def DeleteDir(path: str) -> bool:
    """
    Delete directory tree.
    """
    try:
        shutil.rmtree(path)
        return True
    except OSError:
        pass
    return False


def DeleteEmptyDir(path: str) -> bool:
    """
    Delete directory tree.
    """
    try:
        os.rmdir(path)
        return True
    except OSError:
        pass
    return False


def JoinPathIfValid(default: Any, *paths: str) -> Any:
    for path in paths:
        if not path or not isinstance(path, str):
            return default
    return os.path.join(*paths)


def GetFileSize(path: str) -> str:
    return os.path.getsize(path)


def GetFileMd5(path: str) -> str:
    return GetFileHash(path, hashlib.md5)


def GetFileSha256(path: str) -> str:
    return GetFileHash(path, hashlib.sha256)


g_fileHashCount: int = 0

def ResetFileHashCount() -> None:
    global g_fileHashCount
    g_fileHashCount = 0


def GetFileHash(path: str, hashFunc: Callable) -> str:
    BUF_SIZE = 1024 * 64
    hashStr: str = ""
    try:
        timer = Timer()
        with open(path, "rb", buffering=BUF_SIZE) as rfile:
            hashObj: hashlib._Hash = hashFunc()
            for chunk in iter(lambda: rfile.read(BUF_SIZE), b""):
                hashObj.update(chunk)
            hashStr = hashObj.hexdigest()

            global g_fileHashCount
            g_fileHashCount += 1
            print(f"Hashed ({g_fileHashCount}) {path} as {hashStr} in {timer.GetElapsedSecondsString()} s")
    except:
        pass
    return hashStr


def GetFileModifiedTime(path: str) -> float:
    try:
        return os.path.getmtime(path)
    except OSError:
        return 0.0


if sys.platform == 'win32':
    g_disallowedPathChars = set("<>\"|?*/")
else:
    g_disallowedPathChars = set()

def IsValidPathName(pathname: str) -> bool:
    s = set(pathname)
    for c in g_disallowedPathChars:
        if c in s:
            return False
    return True


def RunProcess(args) -> bool:
    subprocess.run(args=args, check=True)
    return True
