import os.path
from enum import Enum, auto
from glob import glob
from dataclasses import dataclass
from generalsmodbuilder.util import JsonFile
from generalsmodbuilder import util


class Sort(Enum):
    Zero = auto()
    Ascending = auto()
    Descending = auto()


@dataclass(init=False)
class SortDefinition:
    isDate: bool
    label: str
    sort: Sort

    def __init__(self):
        self.isDate = False
        self.label = ""
        self.sort = Sort.Ascending

    def IsDateSort(self) -> bool:
        return self.isDate and not bool(self.label)

    def IsLabelSort(self) -> bool:
        return not self.isDate and bool(self.label)

    def VerifyTypes(self) -> None:
        util.VerifyType(self.isDate, bool, "SortDefinition.isDate")
        util.VerifyType(self.label, str, "SortDefinition.label")
        util.VerifyType(self.sort, Sort, "SortDefinition.sort")

    def VerifyValues(self) -> None:
        util.Verify(self.IsDateSort() or self.IsLabelSort(), "SortDefinition is neither date nor label sort")


@dataclass(init=False)
class ChangeConfigRecord:
    absSourceFiles: list[str]
    absTargetFiles: list[str]
    sortDefinitions: list[SortDefinition]
    includeLabels: list[str]
    excludeLabels: list[str]

    def __init__(self):
        self.absSourceFiles = None
        self.absTargetFiles = None
        self.sortDefinitions = list[SortDefinition]()
        self.includeLabels = list[str]()
        self.excludeLabels = list[str]()

    def Normalize(self) -> None:
        for i, file in enumerate(self.absSourceFiles):
            self.absSourceFiles[i] = os.path.normpath(file)
        for i, file in enumerate(self.absTargetFiles):
            self.absTargetFiles[i] = os.path.normpath(file)

    def VerifyTypes(self) -> None:
        util.VerifyType(self.absSourceFiles, list, "ChangeConfigRecord.absSourceFiles")
        util.VerifyType(self.absTargetFiles, list, "ChangeConfigRecord.absTargetFiles")
        util.VerifyType(self.sortDefinitions, list, "ChangeConfigRecord.sortLabels")
        util.VerifyType(self.includeLabels, list, "ChangeConfigRecord.includeLabels")
        util.VerifyType(self.excludeLabels, list, "ChangeConfigRecord.excludeLabels")
        for file in self.absSourceFiles:
            util.VerifyType(file, str, "ChangeConfigRecord.absSourceFiles.value")
        for file in self.absTargetFiles:
            util.VerifyType(file, str, "ChangeConfigRecord.absTargetFiles.value")
        for definition in self.sortDefinitions:
            util.VerifyType(definition, SortDefinition, "ChangeConfigRecord.sortLabels.value")
            definition.VerifyTypes()
        for label in self.includeLabels:
            util.VerifyType(label, str, "ChangeConfigRecord.includeLabels.value")
        for label in self.excludeLabels:
            util.VerifyType(label, str, "ChangeConfigRecord.excludeLabels.value")

    def VerifyValues(self) -> None:
        # self.absSourceFiles is already verified in ResolveWildcards function.
        for file in self.absTargetFiles:
            util.Verify(util.IsValidPathName(file), f"ChangeConfigRecord.absTargetFiles.value '{file}' is not a valid file name")
        for definition in self.sortDefinitions:
            definition.VerifyValues()

    def ResolveWildcards(self) -> None:
        self.absSourceFiles = ChangeConfigRecord._ResolveWildcardsInFileList(self.absSourceFiles)

    @staticmethod
    def _ResolveWildcardsInFileList(fileList: list[str]) -> list[str]:
        newFiles = list[str]()
        file: str
        for file in fileList:
            if "*" in file and not os.path.isfile(file):
                globFiles: list[str] = glob(file, recursive=True)
                if not bool(globFiles):
                    print(f"Note: Wildcard '{file}' currently matches nothing")

                for globFile in globFiles:
                    if os.path.isfile(globFile):
                        newFiles.append(globFile)
            else:
                util.Verify(os.path.isfile(file), f"File '{file}' is not a valid file")
                newFiles.append(file)
        return newFiles


@dataclass(init=False)
class ChangeConfig:
    records: list[ChangeConfigRecord]

    def __init__(self):
        self.records = list[ChangeConfigRecord]()

    def Normalize(self) -> None:
        for record in self.records:
            record.Normalize()

    def VerifyTypes(self) -> None:
        util.VerifyType(self.records, list, "ChangeConfig.records")
        for record in self.records:
            record.VerifyTypes()

    def VerifyValues(self) -> None:
        for record in self.records:
            record.VerifyValues()

    def ResolveWildcards(self) -> None:
        for record in self.records:
            record.ResolveWildcards()




def __MakeSortFromStr(jStr: str) -> Sort:
    jStrLower: str = jStr.lower()
    if jStrLower == Sort.Ascending.name.lower():
        return Sort.Ascending
    if jStrLower == Sort.Descending.name.lower():
        return Sort.Descending
    return Sort.Zero


def __MakeSortDefinitionsFromList(jSortLabelList: list) -> list[SortDefinition]:
    definitions = list[SortDefinition]()
    jSortLabel: dict
    for jSortLabel in jSortLabelList:
        jDate: str = util.GetCheckedOptional(jSortLabel, "date", str)
        if jDate:
            definition = SortDefinition()
            definition.isDate = True
            definition.sort = __MakeSortFromStr(jDate)
            definitions.append(definition)
            continue

        jLabel: str = util.GetCheckedOptional(jSortLabel, "label", str)
        if jLabel:
            definition = SortDefinition()
            definition.label = jLabel
            definitions.append(definition)

    return definitions


def __MakeAbsFilesFromList(jTargetList: dict, jsonDir: str) -> list[str]:
    files = list[str]()
    jFile: str
    for jFile in jTargetList:
        jFile = os.path.join(jsonDir, jFile)
        files.append(jFile)

    return files


def __MakeChangeConfigRecordFromDict(jRecord: dict, jsonDir: str) -> ChangeConfigRecord:
    record = ChangeConfigRecord()

    jSourceList: list = util.GetCheckedOptional(jRecord, "sourceList", list)
    if jSourceList:
        record.absSourceFiles = __MakeAbsFilesFromList(jSourceList, jsonDir)

    jTargetList: list = util.GetCheckedOptional(jRecord, "targetList", list)
    if jTargetList:
        record.absTargetFiles = __MakeAbsFilesFromList(jTargetList, jsonDir)

    jSortList: list = util.GetCheckedOptional(jRecord, "sortList", list)
    if jSortList:
        record.sortDefinitions = __MakeSortDefinitionsFromList(jSortList)

    record.includeLabels = jRecord.get("includeLabelList", record.includeLabels)
    record.excludeLabels = jRecord.get("excludeLabelList", record.excludeLabels)

    return record


def __MakeChangeConfigRecordsFromList(jRecords: list, jsonDir: str) -> list[ChangeConfigRecord]:
    records = list[ChangeConfigRecord]()
    jRecord: dict
    for jRecord in jRecords:
        record: ChangeConfigRecord = __MakeChangeConfigRecordFromDict(jRecord, jsonDir)
        records.append(record)
    return records


def MakeChangeConfigFromJsons(jsonFiles: list[JsonFile]) -> ChangeConfig:
    config = ChangeConfig()

    for jsonFile in jsonFiles:
        jsonDir: str = util.GetAbsSmartFileDir(jsonFile.path)
        jChangelog: dict = util.GetCheckedOptional(jsonFile.data, "changelog", dict)

        if jChangelog:
            jRecords: list = util.GetCheckedOptional(jChangelog, "records", list)

            if jRecords:
                records: list[ChangeConfigRecord] = __MakeChangeConfigRecordsFromList(jRecords, jsonDir)
                config.records.extend(records)

    config.VerifyTypes()
    config.Normalize()
    config.ResolveWildcards()
    config.VerifyValues()
    return config
