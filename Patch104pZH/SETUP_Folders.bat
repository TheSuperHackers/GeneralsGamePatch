:: Setup work folders
set ToolsDir=..\Tools

set ProjectDir=%~dp0
set GameFilesDir=%ProjectDir%GameFilesEdited
set ReleaseUnpackedDir=%ProjectDir%ReleaseUnpacked
set ReleaseDir=%ProjectDir%Release

set GeneratedBigFilesUnpackedDir=%ProjectDir%.Generated\BigFilesUnpacked
set GeneratedBigFilesDir=%ProjectDir%.Generated\BigFiles

set GeneratedReleaseUnpackedDir=%ProjectDir%.Generated\ReleaseUnpacked

:: Create folders
if not exist %ReleaseDir% mkdir %ReleaseDir%
if not exist %GeneratedBigFilesUnpackedDir% mkdir %GeneratedBigFilesUnpackedDir%
if not exist %GeneratedBigFilesDir% mkdir %GeneratedBigFilesDir%
if not exist %GeneratedReleaseUnpackedDir% mkdir %GeneratedReleaseUnpackedDir%

setlocal enableextensions enabledelayedexpansion
