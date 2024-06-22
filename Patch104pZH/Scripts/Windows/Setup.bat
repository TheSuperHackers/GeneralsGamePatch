@echo off

echo Setup ...

set SetupDir=%~dp0.
set ProjectDir=%~dp0.\..\..

:: Version, size and hash. Sets which Mod Builder is used.
set ModBuilderVer=2.2
set ModBuilderArcSize=32146045
set ModBuilderArcSha256=d14929971a4c5c8ffaecc040c162e4badf2ebec2e4b6983c03f470a236c1a624

:: Misc path setup.
set ModBuilderDir=%SetupDir%\.modbuilder\v%ModBuilderVer%
set ModBuilderExe=%ModBuilderDir%\generalsmodbuilder\generalsmodbuilder.exe
set ModBuilderArc=%ModBuilderDir%\generalsmodbuilder.7z
set ModBuilderArcUrl=https://github.com/TheSuperHackers/GeneralsModBuilder/releases/download/v%ModBuilderVer%/generalsmodbuilder_v%ModBuilderVer%.7z

:: The configuration files.
set ConfigFiles=^
    "%ProjectDir%\ModJsonFiles.json" ^
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
