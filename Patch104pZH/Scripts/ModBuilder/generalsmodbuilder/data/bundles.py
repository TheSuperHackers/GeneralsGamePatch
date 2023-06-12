import os
import zlib
from copy import copy
from glob import glob
from dataclasses import dataclass
from enum import Enum, auto
from typing import Union
from generalsmodbuilder.data.common import ParamsT, VerifyParamsType
from generalsmodbuilder.util import JsonFile
from generalsmodbuilder import util


class BundleEventType(Enum):
    OnPreBuild = auto()
    OnBuild = auto()
    OnPostBuild = auto()
    OnRelease = auto()
    OnInstall = auto()
    OnRun = auto()
    OnUninstall = auto()
    OnStartBuildRawBundleItem = auto()
    OnStartBuildBigBundleItem = auto()
    OnStartBuildRawBundlePack = auto()
    OnStartBuildReleaseBundlePack = auto()
    OnStartBuildInstallBundlePack = auto()
    OnFinishBuildRawBundleItem = auto()
    OnFinishBuildBigBundleItem = auto()
    OnFinishBuildRawBundlePack = auto()
    OnFinishBuildReleaseBundlePack = auto()
    OnFinishBuildInstallBundlePack = auto()


def GetJsonBundleEventName(type: BundleEventType) -> str:
    return type.name[:1].lower() + type.name[1:]


@dataclass(init=False)
class BundleEvent:
    type: BundleEventType
    absScript: str
    funcName: str
    kwargs: dict

    def __init__(self):
        self.type = None
        self.absScript = None
        self.funcName = "OnEvent"
        self.kwargs = dict()

    def GetScriptDir(self) -> str:
        return os.path.dirname(self.absScript)

    def GetScriptName(self) -> str:
        base: str = os.path.basename(self.absScript)
        name, ext = os.path.splitext(base)
        return name

    def VerifyTypes(self) -> None:
        util.VerifyType(self.type, BundleEventType, "BundleEvent.type")
        util.VerifyType(self.absScript, str, "BundleEvent.absScript")
        util.VerifyType(self.funcName, str, "BundleEvent.functionName")
        util.VerifyType(self.kwargs, dict, "BundleEvent.kwargs")

    def VerifyValues(self) -> None:
        util.Verify(os.path.isfile(self.absScript), f"BundleEvent.absScript '{self.absScript}' is not a valid file")
        util.Verify(len(self.funcName) > 0, "BundleEvent.functionName cannot be empty")

    def Normalize(self) -> None:
        self.absScript = os.path.normpath(self.absScript)


BundleEventsT = dict[BundleEventType, BundleEvent]


@dataclass(init=False)
class BundleRegistryDefinition:
    paths: list[str]
    crc32: int

    def __init__(self, paths: list[str]):
        if paths:
            self.paths = paths
            self.__VerifyTypes()
            self.__Normalize()
            self.__VerifyValues()
            pathsStr = "".join(self.paths)
            pathsBytes = bytes(pathsStr, encoding="utf-8")
            self.crc32 = zlib.crc32(pathsBytes)
        else:
            self.paths = None
            self.crc32 = 0

    def __VerifyTypes(self) -> None:
        util.VerifyType(self.paths, list, "BundleFileHashRegistry.paths")
        for path in self.paths:
            util.VerifyType(path, str, "BundleFileHashRegistry.paths.value")

    def __VerifyValues(self) -> None:
        for path in self.paths:
            util.Verify(os.path.isfile(path), f"BundleFileHashRegistry.paths.value '{path}' is not a valid file")

    def __Normalize(self) -> None:
        for index, path in enumerate(self.paths):
            self.paths[index] = os.path.normpath(path)


@dataclass(init=False)
class BundleFile:
    absSourceFile: str
    relTargetFile: str
    params: ParamsT
    registryDef: BundleRegistryDefinition

    def __init__(self):
        self.absSourceFile = None
        self.relTargetFile = None
        self.params = None
        self.registryDef = None

    def VerifyTypes(self) -> None:
        util.VerifyType(self.absSourceFile, str, "BundleFile.absSourceFile")
        util.VerifyType(self.relTargetFile, str, "BundleFile.relTargetFile")
        VerifyParamsType(self.params, "BundleFile.params")
        util.VerifyType(self.registryDef, Union[BundleRegistryDefinition, None], "BundleFile.registry")

    def VerifyValues(self) -> None:
        # self.absSourceFile is already verified in ResolveWildcards function.
        util.Verify(util.IsValidPathName(self.relTargetFile), f"BundleFile.relTargetFile '{self.relTargetFile}' is not a valid file name")
        util.Verify(not os.path.isabs(self.relTargetFile), f"BundleFile.relTargetFile '{self.relTargetFile}' is not a relative path")

    def Normalize(self) -> None:
        self.absSourceFile = os.path.normpath(self.absSourceFile)
        self.relTargetFile = os.path.normpath(self.relTargetFile)


@dataclass(init=False)
class BundleItem:
    name: str
    files: list[BundleFile]
    namePrefix: str
    nameSuffix: str
    isBig: bool
    bigSuffix: str
    setGameLanguageOnInstall: str
    events: BundleEventsT

    def __init__(self):
        self.name = None
        self.files = list[BundleFile]()
        self.namePrefix = ""
        self.nameSuffix = ""
        self.isBig = True
        self.bigSuffix = ""
        self.setGameLanguageOnInstall = ""
        self.events = BundleEventsT()

    def VerifyTypes(self) -> None:
        util.VerifyType(self.name, str, "BundleItem.name")
        util.VerifyType(self.files, list, "BundleItem.files")
        util.VerifyType(self.namePrefix, str, "BundleItem.namePrefix")
        util.VerifyType(self.nameSuffix, str, "BundleItem.nameSuffix")
        util.VerifyType(self.isBig, bool, "BundleItem.isBig")
        util.VerifyType(self.bigSuffix, str, "BundleItem.bigSuffix")
        util.VerifyType(self.setGameLanguageOnInstall, str, "BundleItem.setGameLanguageOnInstall")
        util.VerifyType(self.events, dict, "BundleItem.events")
        for file in self.files:
            util.VerifyType(file, BundleFile, "BundleItem.files.value")
            file.VerifyTypes()
        for etype, event in self.events.items():
            util.VerifyType(etype, BundleEventType, "BundleItem.events.key")
            util.VerifyType(event, BundleEvent, "BundleItem.events.value")
            event.VerifyTypes()

    def VerifyValues(self) -> None:
        util.Verify(util.IsValidPathName(self.name), f"BundleItem.name '{self.name}' has invalid name")
        util.Verify(not self.namePrefix or util.IsValidPathName(self.namePrefix), f"BundleItem.namePrefix '{self.namePrefix}' has invalid name")
        util.Verify(not self.nameSuffix or util.IsValidPathName(self.nameSuffix), f"BundleItem.nameSuffix '{self.nameSuffix}' has invalid name")
        util.Verify(not self.bigSuffix or util.IsValidPathName(self.bigSuffix), f"BundleItem.bigSuffix '{self.bigSuffix}' has invalid name")
        for file in self.files:
            file.VerifyValues()
        for event in self.events.values():
            event.VerifyValues()

    def Normalize(self) -> None:
        for file in self.files:
            file.Normalize()
        for event in self.events.values():
            event.Normalize()

    def ResolveWildcards(self) -> None:
        newFiles: list[BundleFile] = []
        curFile: BundleFile

        for curFile in self.files:
            if "*" in curFile.absSourceFile and not os.path.isfile(curFile.absSourceFile):
                globFiles = glob(curFile.absSourceFile, recursive=True)
                if not bool(globFiles):
                    print(f"Note: Wildcard '{curFile.absSourceFile}' currently matches nothing")

                for globFile in globFiles:
                    if os.path.isfile(globFile):
                        newFile: BundleFile = copy(curFile)
                        newFile.absSourceFile = globFile
                        newFiles.append(newFile)
            else:
                util.Verify(os.path.isfile(curFile.absSourceFile), f"BundleFile.absSourceFile '{curFile.absSourceFile}' is not a valid file")
                newFiles.append(curFile)

        for curFile in newFiles:
            curFile.relTargetFile = BundleItem.__ResolveTargetWildcard(curFile.absSourceFile, curFile.relTargetFile)

        self.files = newFiles
        return newFiles

    @staticmethod
    def __ResolveTargetWildcard(source: str, target: str) -> str:
        sourcePath, sourceFile = os.path.split(source)
        targetPath, targetFile = os.path.split(target)
        sourceName, sourceExtn = os.path.splitext(sourceFile)
        targetName, targetExtn = os.path.splitext(targetFile)

        if targetFile == "*":
            newName = sourceName
            newExtn = sourceExtn
        else:
            newName = sourceName if targetName == "*" else targetName
            newExtn = sourceExtn if targetExtn == ".*" else targetExtn

        if "**" in targetPath:
            basePathPair: list[str] = targetPath.split("**", 1)
            basePath = os.path.dirname(basePathPair[0])
            sourceExtraPathPair: list[str] = source.split(basePath)
            if len(sourceExtraPathPair) > 1:
                sourceExtraPath = os.path.dirname(sourceExtraPathPair[-1])
                sourceExtraPath = sourceExtraPath.removeprefix("/")
                sourceExtraPath = sourceExtraPath.removeprefix("\\")
            else:
                sourceExtraPath = ""
            newPath = targetPath.replace("**", sourceExtraPath)
            newPath = os.path.normpath(newPath)
        else:
            newPath = os.path.normpath(targetPath)

        newTarget = os.path.join(newPath, newName + newExtn)
        newTarget = newTarget.removeprefix("./")
        newTarget = newTarget.removeprefix(".\\")
        return newTarget


@dataclass(init=False)
class BundlePack:
    name: str
    itemNames: list[str]
    namePrefix: str
    nameSuffix: str
    allowBuild: bool
    allowInstall: bool
    setGameLanguageOnInstall: str
    events: BundleEventsT

    def __init__(self):
        self.name = None
        self.itemNames = list[str]()
        self.namePrefix = ""
        self.nameSuffix = ""
        self.allowBuild = False
        self.allowInstall = False
        self.setGameLanguageOnInstall = ""
        self.events = BundleEventsT()

    def VerifyTypes(self) -> None:
        util.VerifyType(self.name, str, "BundlePack.name")
        util.VerifyType(self.itemNames, list, "BundlePack.itemNames")
        util.VerifyType(self.namePrefix, str, "BundlePack.namePrefix")
        util.VerifyType(self.nameSuffix, str, "BundlePack.nameSuffix")
        util.VerifyType(self.allowBuild, bool, "BundlePack.allowBuild")
        util.VerifyType(self.allowInstall, bool, "BundlePack.allowInstall")
        util.VerifyType(self.setGameLanguageOnInstall, str, "BundlePack.setGameLanguageOnInstall")
        util.VerifyType(self.events, dict, "BundlePack.events")
        for itemName in self.itemNames:
            util.VerifyType(itemName, str, "BundlePack.itemNames.value")
        for type,event in self.events.items():
            util.VerifyType(type, BundleEventType, "BundlePack.events.key")
            util.VerifyType(event, BundleEvent, "BundlePack.events.value")
            event.VerifyTypes()

    def VerifyValues(self) -> None:
        util.Verify(util.IsValidPathName(self.name), f"BundlePack.name '{self.name}' has invalid name")
        util.Verify(not self.namePrefix or util.IsValidPathName(self.namePrefix), f"BundlePack.namePrefix '{self.namePrefix}' has invalid name")
        util.Verify(not self.nameSuffix or util.IsValidPathName(self.nameSuffix), f"BundlePack.nameSuffix '{self.nameSuffix}' has invalid name")
        for event in self.events.values():
            event.VerifyValues()

    def Normalize(self) -> None:
        for event in self.events.values():
            event.Normalize()


@dataclass(init=False)
class Bundles:
    items: list[BundleItem]
    packs: list[BundlePack]

    def __init__(self):
        self.items = list[BundleItem]()
        self.packs = list[BundlePack]()

    def FindItemByName(self, name: str) -> BundleItem:
        item: BundleItem
        for item in self.items:
            if item.name == name:
                return item
        return None

    def FindPackByName(self, name: str) -> BundlePack:
        pack: BundlePack
        for pack in self.packs:
            if pack.name == name:
                return pack
        return None

    def FindFirstGameLanguageForInstall(self, name: str) -> str:
        item: BundleItem = self.FindItemByName(name)
        if item != None:
            return item.setGameLanguageOnInstall

        pack: BundlePack = self.FindPackByName(name)
        if pack != None:
            itemName: str
            for itemName in pack.itemNames:
                item = self.FindItemByName(itemName)
                assert item != None
                if item.setGameLanguageOnInstall:
                    return item.setGameLanguageOnInstall

        return ""

    def GetPackListContainingItem(self, itemName: str) -> list[BundlePack]:
        pack: BundlePack
        packItemName: str
        packs = list[BundlePack]()
        for pack in self.packs:
            for packItemName in pack.itemNames:
                if packItemName == itemName:
                    packs.append(pack)
        return packs

    def GetPackListToBuild(self) -> list[BundlePack]:
        pack: BundlePack
        packs = list[BundlePack]()
        for pack in self.packs:
            if pack.allowBuild:
                packs.append(pack)
        return packs

    def GetPackListToInstall(self) -> list[BundlePack]:
        pack: BundlePack
        packs = list[BundlePack]()
        for pack in self.packs:
            if pack.allowInstall:
                packs.append(pack)
        return packs

    def IsItemAllowedToBuild(self, itemName: str) -> bool:
        pack: BundlePack
        packs: list[BundlePack] = self.GetPackListContainingItem(itemName)
        for pack in packs:
            if pack.allowBuild:
                return True
        return False

    def HasPackToBuild(self) -> bool:
        packs: list[BundlePack] = self.GetPackListToBuild()
        return bool(packs)

    def HasPackToInstall(self) -> bool:
        packs: list[BundlePack] = self.GetPackListToInstall()
        return bool(packs)

    def VerifyTypes(self) -> None:
        util.VerifyType(self.items, list, "Bundles.items")
        util.VerifyType(self.packs, list, "Bundles.packs")
        for item in self.items:
            util.VerifyType(item, BundleItem, "Bundles.items.value")
            item.VerifyTypes()
        for pack in self.packs:
            util.VerifyType(pack, BundlePack, "Bundles.packs.value")
            pack.VerifyTypes()

    def VerifyValues(self) -> None:
        timer = util.Timer()
        for item in self.items:
            item.VerifyValues()
        for pack in self.packs:
            pack.VerifyValues()
        self.__VerifyUniqueItemNames()
        self.__VerifyKnownItemsInPacks()
        if timer.GetElapsedSeconds() > util.PERFORMANCE_TIMER_THRESHOLD:
            print(f"Bundles.VerifyValues completed in {timer.GetElapsedSecondsString()} s")

    def __VerifyUniqueItemNames(self) -> None:
        itemLen = len(self.items)
        for a in range(itemLen):
            for b in range(a + 1, itemLen):
                nameA: str = self.items[a].name
                nameB: str = self.items[b].name
                util.Verify(nameA != nameB, f"Bundles.items has items with duplicate name '{nameA}'")

    def __VerifyKnownItemsInPacks(self) -> None:
        for pack in self.packs:
            for packItemName in pack.itemNames:
                found: bool = False
                for item in self.items:
                    if packItemName == item.name:
                        found = True
                        break
                util.Verify(found, f"Bundles.packs with pack '{pack.name}' references unknown bundle item '{packItemName}'")

    def Normalize(self) -> None:
        for item in self.items:
            item.Normalize()
        for pack in self.packs:
            pack.Normalize()

    def ResolveWildcards(self) -> None:
        for item in self.items:
            item.ResolveWildcards()


def __MakeBundleFilesFromDict(jFile: dict, jsonDir: str) -> list[BundleFile]:
    files: list[BundleFile] = list()

    parent: str = util.JoinPathIfValid(jsonDir, jsonDir, jFile.get("parent"))

    params: ParamsT = jFile.get("params", ParamsT())

    registryPaths: list[str] = jFile.get("registryList", list[str]())
    for index, path in enumerate(registryPaths):
        registryPaths[index] = os.path.join(jsonDir, path)
    registryDef = BundleRegistryDefinition(registryPaths) if registryPaths else None

    jSource: str = jFile.get("source")
    jSourceList: list = jFile.get("sourceList")
    jSourceTargetList: list = jFile.get("sourceTargetList")

    if jSource:
        bundleFile = BundleFile()
        bundleFile.absSourceFile = util.JoinPathIfValid(None, parent, jSource)
        bundleFile.relTargetFile = jFile.get("target", jSource)
        bundleFile.params = params
        bundleFile.registryDef = registryDef
        files.append(bundleFile)

    if jSourceList:
        jElement: str
        for jElement in jSourceList:
            bundleFile = BundleFile()
            bundleFile.absSourceFile = util.JoinPathIfValid(None, parent, jElement)
            bundleFile.relTargetFile = jElement
            bundleFile.params = params
            bundleFile.registryDef = registryDef
            files.append(bundleFile)

    if jSourceTargetList:
        jElement: dict[str, str]
        for jElement in jSourceTargetList:
            jElementSource: str = jElement.get("source")
            bundleFile = BundleFile()
            bundleFile.absSourceFile = util.JoinPathIfValid(None, parent, jElementSource)
            bundleFile.relTargetFile = jElement.get("target", jElementSource)
            bundleFile.params = params
            bundleFile.registryDef = registryDef
            files.append(bundleFile)

    return files


def __MakeBundleEventsFromDict(jThing: dict, jsonDir: str) -> BundleEventsT:
    events = BundleEventsT()
    eventType: BundleEventType

    for eventType in BundleEventType:
        eventName: str = GetJsonBundleEventName(eventType)
        jEvent: dict = jThing.get(eventName)
        if jEvent:
            event = BundleEvent()
            event.type = eventType
            event.absScript = util.JoinPathIfValid(None, jsonDir, jEvent.get("script"))
            event.funcName = jEvent.get("function", event.funcName)
            event.kwargs = jEvent.get("kwargs", event.kwargs)
            events[event.type] = event

    return events


def __MakeBundleItemFromDict(jItem: dict, jsonDir: str) -> BundleItem:
    item = BundleItem()
    item.name = jItem.get("name")
    item.namePrefix = jItem.get("namePrefix", item.namePrefix)
    item.nameSuffix = jItem.get("nameSuffix", item.nameSuffix)
    item.isBig = jItem.get("big", item.isBig)
    item.bigSuffix = jItem.get("bigSuffix", item.bigSuffix)
    item.setGameLanguageOnInstall = jItem.get("setGameLanguageOnInstall", item.setGameLanguageOnInstall)

    jFiles = jItem.get("files")
    if jFiles:
        jFile: dict
        for jFile in jFiles:
            item.files.extend(__MakeBundleFilesFromDict(jFile, jsonDir))

    item.events = __MakeBundleEventsFromDict(jItem, jsonDir)

    return item


def __MakeBundlePackFromDict(jPack: dict, jsonDir: str) -> BundlePack:
    pack = BundlePack()
    pack.name = jPack.get("name")
    pack.namePrefix = jPack.get("namePrefix", pack.namePrefix)
    pack.nameSuffix = jPack.get("nameSuffix", pack.nameSuffix)
    pack.itemNames = jPack.get("itemNames")
    pack.allowInstall = jPack.get("install", pack.allowInstall)
    pack.allowBuild = jPack.get("build", pack.allowBuild)
    pack.setGameLanguageOnInstall = jPack.get("setGameLanguageOnInstall", pack.setGameLanguageOnInstall)
    pack.events = __MakeBundleEventsFromDict(jPack, jsonDir)

    return pack


def AddBundlePacksFromJsons(jsonFiles: list[JsonFile], bundles: Bundles) -> Bundles:
    """
    Parses bundle packs from all json files where present.
    """
    jPacksPrefix: str = ""
    jPacksSuffix: str = ""

    for jsonFile in jsonFiles:
        jsonDir: str = util.GetAbsSmartFileDir(jsonFile.path)
        jBundles: dict = jsonFile.data.get("bundles")

        if jBundles:
            jPacksPrefix: str = jBundles.get("packsPrefix", jPacksPrefix)
            jPacksSuffix: str = jBundles.get("packsSuffix", jPacksSuffix)
            jPacks: dict = jBundles.get("packs")
            if jPacks:
                jPack: dict
                for jPack in jPacks:
                    bundlePack: BundlePack = __MakeBundlePackFromDict(jPack, jsonDir)

                    if not bundlePack.namePrefix and jPacksPrefix:
                        bundlePack.namePrefix = jPacksPrefix
                    if not bundlePack.nameSuffix and jPacksSuffix:
                        bundlePack.nameSuffix = jPacksSuffix

                    bundles.packs.append(bundlePack)
    return


def AddBundleItemsFromJsons(jsonFiles: list[JsonFile], bundles: Bundles) -> Bundles:
    """
    Parses bundle items from all json files where present.
    """
    jItemsPrefix: str = ""
    jItemsSuffix: str = ""

    for jsonFile in jsonFiles:
        jsonDir: str = util.GetAbsSmartFileDir(jsonFile.path)
        jBundles: dict = jsonFile.data.get("bundles")

        if jBundles:
            jItemsPrefix: str = jBundles.get("itemsPrefix", jItemsPrefix)
            jItemsSuffix: str = jBundles.get("itemsSuffix", jItemsSuffix)
            jItems: dict = jBundles.get("items")

            if jItems:
                jItem: dict
                for jItem in jItems:
                    bundleItem: BundleItem = __MakeBundleItemFromDict(jItem, jsonDir)

                    if not bundleItem.namePrefix and jItemsPrefix:
                        bundleItem.namePrefix = jItemsPrefix
                    if not bundleItem.nameSuffix and jItemsSuffix:
                        bundleItem.nameSuffix = jItemsSuffix

                    bundles.items.append(bundleItem)
    return


def MakeBundlesFromJsons(jsonFiles: list[JsonFile]) -> Bundles:
    bundles = Bundles()

    AddBundleItemsFromJsons(jsonFiles, bundles)
    AddBundlePacksFromJsons(jsonFiles, bundles)

    bundles.VerifyTypes()
    bundles.Normalize()
    bundles.ResolveWildcards()
    bundles.VerifyValues()

    return bundles
