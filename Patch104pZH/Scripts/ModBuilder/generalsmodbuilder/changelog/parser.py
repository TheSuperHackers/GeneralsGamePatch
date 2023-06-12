import datetime
from generalsmodbuilder.data.changeconfig import ChangeConfig, ChangeConfigRecord
from generalsmodbuilder import util


class ChangeLogChange:
    typeName: str
    text: str

    def __init__(self):
        self.typeName = None
        self.text = None

    def VerifyTypes(self) -> None:
        util.VerifyType(self.typeName, str, "ChangeLogChange.typeName")
        util.VerifyType(self.text, str, "ChangeLogChange.text")


class ChangeLogRecordEntry:
    absSourceFile: str
    date: datetime.date
    title: str
    majorChanges: list[ChangeLogChange]
    minorChanges: list[ChangeLogChange]
    majorTypeCounts: dict[str, int]
    minorTypeCounts: dict[str, int]
    labels: list[str]
    links: list[str]
    authors: list[str]

    def __init__(self):
        self.absSourceFile = None
        self.date = None
        self.title = None
        self.majorChanges = None
        self.minorChanges = list[ChangeLogChange]()
        self.majorTypeCounts = dict[str, int]()
        self.minorTypeCounts = dict[str, int]()
        self.labels = list[str]()
        self.links = list[str]()
        self.authors = list[str]()

    def VerifyTypes(self) -> None:
        util.VerifyType(self.absSourceFile, str, "ChangeLogRecordEntry.absSourceFile")
        util.VerifyType(self.date, datetime.date, "ChangeLogRecordEntry.date")
        util.VerifyType(self.title, str, "ChangeLogRecordEntry.title")
        util.VerifyType(self.majorChanges, list, "ChangeLogRecordEntry.majorChanges")
        util.VerifyType(self.minorChanges, list, "ChangeLogRecordEntry.minorChanges")
        util.VerifyType(self.majorTypeCounts, dict, "ChangeLogRecordEntry.majorTypeCounts")
        util.VerifyType(self.minorTypeCounts, dict, "ChangeLogRecordEntry.minorTypeCounts")
        util.VerifyType(self.labels, list, "ChangeLogRecordEntry.labels")
        util.VerifyType(self.links, list, "ChangeLogRecordEntry.links")
        util.VerifyType(self.authors, list, "ChangeLogRecordEntry.authors")

        for change in self.majorChanges:
            change.VerifyTypes()
        for change in self.minorChanges:
            change.VerifyTypes()
        for key, val in self.majorTypeCounts.items():
            util.VerifyType(key, str, "ChangeLogRecordEntry.majorTypeCounts.key")
            util.VerifyType(val, int, "ChangeLogRecordEntry.majorTypeCounts.value")
        for key, val in self.minorTypeCounts.items():
            util.VerifyType(key, str, "ChangeLogRecordEntry.minorTypeCounts.key")
            util.VerifyType(val, int, "ChangeLogRecordEntry.minorTypeCounts.value")
        for label in self.labels:
            util.VerifyType(label, str, "ChangeLogRecordEntry.labels.value")
        for link in self.links:
            util.VerifyType(link, str, "ChangeLogRecordEntry.links.value")
        for author in self.authors:
            util.VerifyType(author, str, "ChangeLogRecordEntry.authors.value")



class ChangeLogRecord:
    configRecord: ChangeConfigRecord
    entries: list[ChangeLogRecordEntry]

    def __init__(self):
        self.configRecord = None
        self.entries = None

    def VerifyTypes(self) -> None:
        util.VerifyType(self.configRecord, ChangeConfigRecord, "ChangeLogRecord.configRecord")
        util.VerifyType(self.entries, list, "ChangeLogRecord.entries")
        for entry in self.entries:
            entry.VerifyTypes()


class ChangeLog:
    records: list[ChangeLogRecord]

    def __init__(self):
        self.records = list[ChangeLogRecord]()

    def VerifyTypes(self) -> None:
        util.VerifyType(self.records, list, "ChangeLog.records")
        for record in self.records:
            record.VerifyTypes()


def __MakeDateFromStr(yDate: str | datetime.date | datetime.datetime) -> datetime.date:
    if isinstance(yDate, datetime.date):
        return yDate

    if isinstance(yDate, datetime.datetime):
        return datetime.date(
            year=yDate.year,
            month=yDate.month,
            day=yDate.day)

    year = 0
    month = 0
    day = 0

    try:
        # DD-MM-YYYY hh:mm:ss
        # 0  3  6    11 14 17
        day = int(yDate[0:2])
        month = int(yDate[3:5])
        year = int(yDate[6:10])
    except ValueError:
        pass

    if year == 0 or month == 0 or day == 0:
        try:
            # YYYY-MM-DD hh:mm:ss
            # 0    5  8  11 14 17
            day = int(yDate[0:4])
            month = int(yDate[5:7])
            year = int(yDate[8:10])
            pass
        except ValueError:
            pass

        if year == 0 or month == 0 or day == 0:
            raise ValueError(f"Error parse date {yDate}. Expected format is DD-MM-YYYY or YYYY-MM-DD")

    return datetime.date(
        year=year,
        month=month,
        day=day)


def _MakeChangeLogRecordEntryFromDict(yData: dict) -> ChangeLogRecordEntry:
    entry = ChangeLogRecordEntry()

    yDate: str = util.GetCheckedMandatory(yData, "date", str | datetime.date | datetime.datetime)
    yTitle: str = util.GetCheckedMandatory(yData, "title", str)
    yMajorchanges: str = util.GetCheckedMandatory(yData, "changes", list)
    yMinorchanges: str = util.GetCheckedOptional(yData, "subchanges", list)
    yLabels: list = util.GetCheckedOptional(yData, "labels", list)
    yLinks: list = util.GetCheckedOptional(yData, "links", list)
    yAuthors: list = util.GetCheckedOptional(yData, "authors", list)

    entry.date = __MakeDateFromStr(yDate)
    entry.title = yTitle
    entry.majorChanges = list[ChangeLogChange]()

    yChangesDict: dict
    type: str
    text: str
    for yChangesDict in yMajorchanges:
        change = ChangeLogChange()
        util.Verify(len(yChangesDict) == 1, "changes has list entry with more than one key and value")
        type: str = list(yChangesDict.keys())[0]
        text: str = list(yChangesDict.values())[0]
        type = type.lower()
        change.typeName = type
        change.text = text
        if entry.majorTypeCounts.get(type):
            entry.majorTypeCounts[type] += 1
        else:
            entry.majorTypeCounts[type] = 1
        entry.majorChanges.append(change)

    if yMinorchanges:
        for yChangesDict in yMinorchanges:
            change = ChangeLogChange()
            util.Verify(len(yChangesDict) == 1, "subchanges has list entry with more than one key and value")
            type: str = list(yChangesDict.keys())[0]
            text: str = list(yChangesDict.values())[0]
            type = type.lower()
            change.typeName = type
            change.text = text
            if entry.minorTypeCounts.get(type):
                entry.minorTypeCounts[type] += 1
            else:
                entry.minorTypeCounts[type] = 1
            entry.minorChanges.append(change)

    if yLabels:
        entry.labels = sorted(set(yLabels))
    if yLinks:
        entry.links = sorted(set(yLinks))
    if yAuthors:
        entry.authors = sorted(set(yAuthors))

    return entry


class ChangeLogRecordCache:
    cache: dict[str, ChangeLogRecordEntry]

    def __init__(self):
        self.cache = dict[str, ChangeLogRecordEntry]()

    def GetChangeLogRecordEntry(self, absSource: str) -> ChangeLogRecordEntry:
        entry: ChangeLogRecordEntry = self.cache.get(absSource)
        if entry:
            return entry
        else:
            yaml = util.YamlFile(absSource)
            entry = _MakeChangeLogRecordEntryFromDict(yaml.data)
            self.cache[absSource] = entry
            return entry


def __MakeChangeLogRecordFromDict(configRecord: ChangeConfigRecord, cache=ChangeLogRecordCache()) -> ChangeLogRecord:
    record = ChangeLogRecord()
    record.configRecord = configRecord
    record.entries = list[ChangeLogRecordEntry]()

    absSource: str
    for absSource in configRecord.absSourceFiles:
        if util.HasFileExt(absSource, "yaml"):
            entry: ChangeLogRecordEntry = cache.GetChangeLogRecordEntry(absSource)
            entry.absSourceFile = absSource
            record.entries.append(entry)

    return record


def MakeChangelogFromChangeConfig(config: ChangeConfig) -> ChangeLog:
    log = ChangeLog()
    configRecord: ChangeConfigRecord
    cache = ChangeLogRecordCache()

    for configRecord in config.records:
        logRecord: ChangeLogRecord = __MakeChangeLogRecordFromDict(configRecord, cache=cache)
        logRecord.configRecord = configRecord
        log.records.append(logRecord)

    log.VerifyTypes()
    return log
