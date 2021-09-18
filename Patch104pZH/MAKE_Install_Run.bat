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
call %ThisDir0%MAKE_Install.bat

@echo off
:: Rename files as per setup in SETUP_UserSettings.bat
for %%f in (%GameFilesToDisable%) do (
	if exist %GameRootDir%\%%f (
		ren %GameRootDir%\%%f %%f.PATCH104P
		echo on
		echo Rename %%f to %%f.PATCH104P
		@echo off
	)
)

set GameExeArgs0=%GameExeArgs:"=%

::Run game
%GameRootDir%\%GameExeFile% %GameExeArgs0%

:: Restore files as per setup in SETUP_UserSettings.bat
for %%f in (%GameFilesToDisable%) do (
	if exist %GameRootDir%\%%f.PATCH104P (
		ren %GameRootDir%\%%f.PATCH104P %%f
		echo on
		echo Rename %%f.PATCH104P to %%f
		@echo off
	)
)
