@echo off

set SetupDir=%~dp0.
set ProjectDir=%~dp0.\..\..

:: The mod config files.
set ConfigFiles=^
    "%ProjectDir%\ModJsonFiles.json" ^
    "%SetupDir%\WindowsRunner.json" ^
    "%SetupDir%\WindowsTools.json"

:: The Mod Builder. It is a git submodule, so the submodule commit decides which
:: version is used. Upgrade it with:
::   git submodule update --remote Tools/GeneralsModBuilder
:: The launcher installs everything the Mod Builder needs on first use.
set ModBuilderDir=%SetupDir%\..\..\..\Tools\GeneralsModBuilder
set ModBuilderCmd=%ModBuilderDir%\modbuilder.cmd

:: Print setup info.
echo SETUP.BAT
for %%f in (%ConfigFiles%) do (
    echo config %%f
)
echo moddir %ModBuilderDir%
echo modcmd %ModBuilderCmd%

if not exist "%ModBuilderCmd%" (
    echo.
    echo The Mod Builder is missing at '%ModBuilderDir%'.
    echo Fetch the git submodule with:
    echo     git submodule update --init --recursive
    exit /B 222
)
