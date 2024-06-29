@echo off

echo Setup ...

set SetupDir=%~dp0.
set ProjectDir=%~dp0.\..\..

:: Version, size and hash. Sets which Mod Builder is used.
set ModBuilderVer=2.3
set ModBuilderArcSize=32144646
set ModBuilderArcSha256=8d117731685a766516ddb01ca15e6ca3d173cc44d1c7edb4a7a24026833ed71c

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
