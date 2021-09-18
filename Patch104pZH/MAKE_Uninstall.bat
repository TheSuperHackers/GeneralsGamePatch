@echo off
:: BatchGotAdmin
:-------------------------------------
::  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

:: --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"=""
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------

echo on
set ThisDir0=%~dp0
set GeneratedReleaseUnpackedFiles=

call %ThisDir0%Scripts\MAKE_Patch104pZH.bat
call %ThisDir0%Scripts\MAKE_Patch104pArtZH.bat
call %ThisDir0%SETUP_UserSettings.bat

:: Remove release files from game
for %%f in (%GeneratedReleaseUnpackedFiles%) do (
	del /f /q %GameRootDir%\%%f
)

:: Restore files as per setup in SETUP_UserSettings.bat
for %%f in (%GameFilesToDisable%) do (
	if exist %GameRootDir%\%%f.PATCH104P (
		ren %GameRootDir%\%%f.PATCH104P %%f
	)
)
