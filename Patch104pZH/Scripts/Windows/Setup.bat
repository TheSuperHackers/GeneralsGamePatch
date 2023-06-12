@echo off

set SetupDir=%~dp0.
set ProjectDir=%~dp0.\..\..
set VenvPythonExe=%ProjectDir%\Scripts\ModBuilder\.venv\Scripts\python.exe
set BuildPy=%ProjectDir%\Scripts\ModBuilder\buildproject.py
set BuildJson=%ProjectDir%\Scripts\ModBuilder\build-lite.json
set MainPy=%ProjectDir%\Scripts\ModBuilder\generalsmodbuilder\main.py

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

if exist "%SetupDir%\UserSetup.bat" (
    call "%SetupDir%\UserSetup.bat"
) else (
    if exist "%SetupDir%\UserSetup.template.bat" (
        call "%SetupDir%\UserSetup.template.bat"
    )
)

if not defined PythonExe (
    set PythonExe=python
)
if not defined ToolsRootDir (
    set ToolsRootDir=%~dp0.
)
