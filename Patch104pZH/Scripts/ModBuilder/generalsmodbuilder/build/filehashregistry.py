import csv
import io
import os
import zipfile
from dataclasses import dataclass
from typing import Any
from generalsmodbuilder import util


@dataclass
class FileHash:
    relFile: str
    size: int
    md5: str
    sha256: str

    def GetAsList(self) -> list[Any]:
        return [self.relFile, self.size, self.md5, self.sha256]

    @staticmethod
    def GetRowNameList() -> list[str]:
        return ["relPath", "size", "md5", "sha256"]


FileHashDictT = dict[str, FileHash]


class FileHashRegistry:
    fileHashes: FileHashDictT
    lowerPath: bool
    posixPath: bool
    encoding: str


    def __init__(self):
        self.fileHashes = FileHashDictT()
        self.lowerPath = True
        self.posixPath = True
        self.encoding = "ascii"


    def __ProcessPath(self, path: str) -> str:
        if self.lowerPath:
            path = path.lower()

        if self.posixPath:
            path = path.replace("\\", "/")
        else:
            path = path.replace("/", "\\")

        return path


    def Clear(self) -> None:
        self.fileHashes.clear()


    def Merge(self, other: Any) -> None:
        self.fileHashes.update(other.fileHashes)


    def AddFile(self, relFile: str, size: int = 0, md5: str = "", sha256: str = "") -> None:
        relFile = self.__ProcessPath(relFile)
        self.fileHashes[relFile] = FileHash(
            relFile=relFile,
            size=size,
            md5=md5,
            sha256=sha256)


    def FindFile(self, relFile: str) -> FileHash | None:
        relFile = self.__ProcessPath(relFile)
        return self.fileHashes.get(relFile)


    def SaveRegistry(self, path: str, name: str) -> bool:
        print(f"Save File Hash Registry {path} {name}")

        if not self.fileHashes:
            return False
        filePath: str = os.path.join(path, name + ".csv")
        with open(filePath, "w", encoding=self.encoding, newline="") as file:
            writer: csv.DictWriter = csv.writer(file, lineterminator="\n")
            writer.writerow(FileHash.GetRowNameList())
            for value in self.fileHashes.values():
                writer.writerow(value.GetAsList())
        return True


    def __ParseRegistry(self, file: Any) -> None:
        reader: csv.DictReader = csv.reader(file, lineterminator="\n")
        rowExpected = FileHash.GetRowNameList()
        row0 = next(reader)
        util.Verify(row0[:len(rowExpected)] == rowExpected, "Registry")
        for row in reader:
            self.AddFile(row[0], int(row[1]), row[2], row[3])


    def LoadRegistry(self, path: str, name: str) -> bool:
        print(f"Load File Hash Registry {name}")

        filePath: str = os.path.join(path, name + ".zip")
        try:
            with zipfile.ZipFile(filePath) as zipf:
                print(f"Reading {filePath}")
                self.Clear()
                for zipinfo in zipf.infolist():
                    print(f"Reading {zipinfo.filename} in archive")
                    with zipf.open(zipinfo, "r") as file:
                        textFile = io.TextIOWrapper(file, encoding=self.encoding)
                        self.__ParseRegistry(textFile)
            return bool(self.fileHashes)
        except OSError:
            pass

        filePath = os.path.join(path, name + ".csv")
        try:
            with open(filePath, "r", encoding=self.encoding) as file:
                print(f"Reading {filePath}")
                self.Clear()
                self.__ParseRegistry(file)
            return bool(self.fileHashes)
        except OSError:
            pass

        return False
