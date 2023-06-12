import functools
from copy import copy
from markdownmaker import document as md
from markdownmaker import markdownmaker as md
from generalsmodbuilder import util
from generalsmodbuilder.changelog.parser import ChangeLog, ChangeLogRecord, ChangeLogRecordEntry
from generalsmodbuilder.data.changeconfig import ChangeConfigRecord, Sort, SortDefinition


def __AddRecordsLabelFiltersText(doc: md.Document, configRecord: ChangeConfigRecord, labelCounts: dict[str, int]) -> None:
    hasIncludeLabels = False
    hasExcludeLabels = False

    if bool(configRecord.includeLabels):
        hasIncludeLabels = True
        labelsStr = ", ".join(label for label in sorted(configRecord.includeLabels))
        doc.add(md.Paragraph(f"Includes changes with labels: {labelsStr}"))

    if bool(configRecord.excludeLabels):
        hasExcludeLabels = True
        labelsStr = ", ".join(label for label in sorted(configRecord.excludeLabels))
        doc.add(md.Paragraph(f"Excludes changes with labels: {labelsStr}"))

    if not hasIncludeLabels and not hasExcludeLabels:
        doc.add(md.Paragraph(f"Includes changes with all labels."))

    labelCountStrList = [f"{label} ({count})" for label, count in labelCounts.items()]
    labelCountStrList = sorted(labelCountStrList)
    doc.add(md.Paragraph(f"Occuring labels are"))
    doc.add(md.UnorderedList(labelCountStrList))


def __AddRecordsSortRulesText(doc: md.Document, configRecord: ChangeConfigRecord) -> None:
    sortList = []

    if bool(configRecord.sortDefinitions):
        for definition in configRecord.sortDefinitions:
            if definition.IsDateSort():
                sortList.append(f"date ({definition.sort.name.lower()})")
            elif definition.IsLabelSort():
                sortList.append(f"{definition.label}")

    sortStr = ", ".join(sortList)
    doc.add(md.Paragraph(f"Sorts changes by: {sortStr}"))


def __AddRecordsChangeCountsText(doc: md.Document, logRecord: ChangeLogRecord) -> None:
    entriesCount: int = len(logRecord.entries)
    majorChangeCount = 0
    minorChangeCount = 0
    majorChangeCountByType = dict[str, int]()
    minorChangeCountByType = dict[str, int]()

    for logEntry in logRecord.entries:
        for type, count in logEntry.majorTypeCounts.items():
            majorChangeCount += count
            if majorChangeCountByType.get(type):
                majorChangeCountByType[type] += count
            else:
                majorChangeCountByType[type] = count

        for type, count in logEntry.minorTypeCounts.items():
            minorChangeCount += count
            if minorChangeCountByType.get(type):
                minorChangeCountByType[type] += count
            else:
                minorChangeCountByType[type] = count

    majorChangeCountStrList = [f"{type.upper()} ({count})" for type, count in majorChangeCountByType.items()]
    minorChangeCountStrList = [f"{type.upper()} ({count})" for type, count in minorChangeCountByType.items()]

    doc.add(md.Paragraph(f"Contains {entriesCount} entries with"))
    doc.add(md.UnorderedList([
        f"{majorChangeCount} changes",
        md.UnorderedList(majorChangeCountStrList),
        f"{minorChangeCount} subchanges",
        md.UnorderedList(minorChangeCountStrList),
        ]))


def __MakeRecordTitle(logEntry: ChangeLogRecordEntry) -> str:
    date: str = logEntry.date.strftime('%Y-%m-%d')
    title: str = f"{date} - {logEntry.title}"
    return title


def __MakeRecordTitleLink(logEntry: ChangeLogRecordEntry, index: int) -> str:
    name: str = util.GetFileNameNoExt(logEntry.absSourceFile)
    name = "".join(name.split())
    date: str = logEntry.date.strftime('%Y%m%d')
    # Not using index value to keep clean links from one generation revision to another.
    # Instead using date to generate somewhat unique links and avoid potential collisions.
    link: str = f"link__{date}__{name.lower()}"
    return link


def __MakeMarkdownLink(link: str) -> md.Link:
    return md.Link(label=f"{link}", url=f"{link}")


def __AddRecordsIndex(doc: md.Document, logRecord: ChangeLogRecord) -> None:
    logEntry: ChangeLogRecordEntry

    with md.HeaderSubLevel(doc):
        doc.add(md.Header(f"Index"))

        linkList = list[md.Link]()

        for index, logEntry in enumerate(logRecord.entries):
            title: str = __MakeRecordTitle(logEntry)
            titleLink: str = __MakeRecordTitleLink(logEntry, index)
            link = md.Link(label=title, url=f"#{titleLink}")
            linkList.append(link)

        doc.add(md.Paragraph(md.UnorderedList(linkList)))


def __AddRecordsDetails(doc: md.Document, logRecord: ChangeLogRecord) -> None:
    logEntry: ChangeLogRecordEntry

    with md.HeaderSubLevel(doc):
        with md.HeaderSubLevel(doc):
            for i, logEntry in enumerate(logRecord.entries):
                fileName: str = util.GetFileName(logEntry.absSourceFile)
                title: str = __MakeRecordTitle(logEntry)
                titleLink: str = __MakeRecordTitleLink(logEntry, i)
                majorList = [f"**{change.typeName.upper()}**: {change.text}" for change in logEntry.majorChanges]
                minorList = [f"**{change.typeName.upper()}**: {change.text}" for change in logEntry.minorChanges]
                labelsStr = ", ".join(label for label in logEntry.labels)
                authorsStr = ", ".join(author for author in logEntry.authors)
                linkList = [__MakeMarkdownLink(link) for link in logEntry.links]

                doc.add(md.HorizontalRule())
                doc.add(md.Header(f"{title} <a name='{titleLink}'></a>"))
                if bool(majorList):
                    doc.add(md.Paragraph(md.Bold("Changes")))
                    doc.add(md.UnorderedList(majorList))
                if bool(minorList):
                    doc.add(md.Paragraph(md.Bold("Subchanges")))
                    doc.add(md.UnorderedList(minorList))
                if bool(logEntry.links):
                    doc.add(md.Paragraph(md.Bold("Links")))
                    doc.add(md.UnorderedList(linkList))
                if labelsStr:
                    doc.add(md.Paragraph(f"{md.Bold('Labels:')} {labelsStr}"))
                if authorsStr:
                    doc.add(md.Paragraph(f"{md.Bold('Authors:')} {authorsStr}"))
                doc.add(md.Paragraph(f"{md.Bold('Source:')} {fileName}"))


def GenerateChangeLogMarkdown(logRecord: ChangeLogRecord, absTarget: str) -> None:
    if not bool(logRecord.entries):
        return

    timer = util.Timer()
    print(f"Generate change log at {absTarget}")

    labelCounts = dict[str, int]()
    logEntry: ChangeLogRecordEntry
    for logEntry in logRecord.entries:
        for label in logEntry.labels:
            if labelCounts.get(label) != None:
                labelCounts[label] += 1
            else:
                labelCounts[label] = 1

    doc = md.Document()

    fileStr: str = util.GetFileNameNoExt(absTarget)
    modBuilderLink = md.Link("GeneralsModBuilder", "https://github.com/TheSuperHackers/GeneralsModBuilder")
    doc.add(md.Header(f"Change Log '{fileStr}'"))
    doc.add(md.Paragraph(f"This document was auto generated by {modBuilderLink}. Do not edit by hand."))

    __AddRecordsLabelFiltersText(doc, logRecord.configRecord, labelCounts)
    __AddRecordsSortRulesText(doc, logRecord.configRecord)
    __AddRecordsChangeCountsText(doc, logRecord)
    __AddRecordsIndex(doc, logRecord)
    __AddRecordsDetails(doc, logRecord)

    text: str = doc.write()
    util.MakeDirsForFile(absTarget)
    with open(absTarget, "w", encoding='utf-8') as targetFile:
        targetFile.write(text)

    if timer.GetElapsedSeconds() > util.PERFORMANCE_TIMER_THRESHOLD:
        print(f"Generate change log completed in {timer.GetElapsedSecondsString()} s")


def GenerateChangeLogDocuments(changeLog: ChangeLog) -> None:
    logRecord: ChangeLogRecord
    absTarget: str

    for logRecord in changeLog.records:
        for absTarget in logRecord.configRecord.absTargetFiles:
            if util.HasFileExt(absTarget, "md"):
                GenerateChangeLogMarkdown(logRecord, absTarget)


def __ChangeLogRecordCompare(a: ChangeLogRecordEntry, b: ChangeLogRecordEntry, definitions: list[SortDefinition]) -> int:
    # The sort definition list can contain multiple entries, where earlier entries have higher sort priority.
    # This algoritm adds to return value if a > b and subtracts if a < b, and vice versa if the sort is descending.
    # The higher the sort definition priority, the higher the value to add or subtract.
    value = 0
    weight = len(definitions)

    for i, definition in enumerate(definitions):
        less = False
        greater = False
        if definition.IsDateSort():
            if definition.sort == Sort.Ascending:
                less = a.date < b.date
                greater = a.date > b.date
            elif definition.sort == Sort.Descending:
                less = a.date > b.date
                greater = a.date < b.date
        elif definition.IsLabelSort():
            less = (definition.label in a.labels) and (not definition.label in b.labels)
            greater = (not definition.label in a.labels) and (definition.label in b.labels)

        if less:
            value -= (weight - i) ** (weight - i)
        elif greater:
            value += (weight - i) ** (weight - i)

    return value


def SortChangeList(changeLog: ChangeLog) -> ChangeLog:
    logRecord: ChangeLogRecord
    newChangeLog = ChangeLog()

    for logRecord in changeLog.records:
        newLogRecord = ChangeLogRecord()
        newLogRecord.configRecord = logRecord.configRecord
        newLogRecord.entries = copy(logRecord.entries)
        fnc = lambda a, b: __ChangeLogRecordCompare(a, b, logRecord.configRecord.sortDefinitions)
        cmp = functools.cmp_to_key(fnc)
        newLogRecord.entries.sort(key=cmp)
        newChangeLog.records.append(newLogRecord)

    return newChangeLog


def FilterChangeLog(changeLog: ChangeLog) -> ChangeLog:
    logRecord: ChangeLogRecord
    logEntry: ChangeLogRecordEntry
    newChangeLog = ChangeLog()

    for logRecord in changeLog.records:
        newLogRecord = ChangeLogRecord()
        newLogRecord.configRecord = logRecord.configRecord
        newLogRecord.entries = list[ChangeLogRecordEntry]()

        includeLabels: list[str] = logRecord.configRecord.includeLabels
        excludeLabels: list[str] = logRecord.configRecord.excludeLabels

        for logEntry in logRecord.entries:
            if bool(includeLabels):
                if set(includeLabels).isdisjoint(set(logEntry.labels)):
                    continue
            if bool(excludeLabels):
                if not set(excludeLabels).isdisjoint(set(logEntry.labels)):
                    continue
            newLogRecord.entries.append(logEntry)

        newChangeLog.records.append(newLogRecord)

    return newChangeLog
