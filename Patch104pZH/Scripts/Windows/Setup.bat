@echo off

echo Setup ...

set SetupDir=%~dp0.
set ProjectDir=%~dp0.\..\..

:: Version, size and hash. Sets which Mod Builder is used.
set ModBuilderVer=2.1
set ModBuilderArcSize=32209682
set ModBuilderArcSha256=7357871f9e173373b4d7de8385a2cd23c8a3210cd103373830cd2460bfc7acd8

:: Misc path setup.
set ModBuilderDir=%SetupDir%\.modbuilder\v%ModBuilderVer%
set ModBuilderExe=%ModBuilderDir%\generalsmodbuilder\generalsmodbuilder.exe
set ModBuilderArc=%ModBuilderDir%\generalsmodbuilder.7z
set ModBuilderArcUrl=https://github.com/TheSuperHackers/GeneralsModBuilder/releases/download/v%ModBuilderVer%/generalsmodbuilder_v%ModBuilderVer%.7z

:: The configuration files.
set ConfigFiles=^
    "%ProjectDir%\ModBundleItems.json" ^
    "%ProjectDir%\ModBundleAudioItems.json" ^
    "%ProjectDir%\ModBundleLanguageItems.json" ^
    "%ProjectDir%\ModBundleCorePacks.json" ^
    "%ProjectDir%\ModBundleFullPacks.json" ^
    "%ProjectDir%\ModChangeLog.json" ^
    "%ProjectDir%\ModFolders.json" ^
    "%SetupDir%\WindowsRunner.json" ^
    "%SetupDir%\WindowsTools.json"

:: Print setup info.
if defined PrintSetup (
    echo Using Mod Builder version %ModBuilderVer%
    echo Archive size %ModBuilderArcSize%
    echo Archive sha256 %ModBuilderArcSha256%
    echo Archive url %ModBuilderArcUrl%
    echo Archive path %ModBuilderArc%
    echo Install path %ModBuilderDir%
    echo Executable path %ModBuilderExe%
    echo Configuration files:
    for %%f in (%ConfigFiles%) do (
        echo %%f
    )
)
