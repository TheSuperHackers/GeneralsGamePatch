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

setlocal

set ThisDir0=%~dp0.
set GeneratedReleaseUnpackedFiles=

call "%ThisDir0%\Scripts\MAKE_Patch104pZH.bat" build
call "%ThisDir0%\Scripts\MAKE_Patch104pArtZH.bat" build
call "%ThisDir0%\SETUP_UserSettings.bat"

:: Rename files as per setup in SETUP_UserSettings.bat
for %%f in (%GameFilesToDisable%) do (
    if exist "%GameRootDir:"=%\%%f" (
        ren "%GameRootDir:"=%\%%f" %%f.PATCH104P
    )
)

:: Copy release files to game
for %%f in (%GeneratedReleaseUnpackedFiles%) do (
    xcopy /y "%GeneratedReleaseUnpackedDir%\%%f" "%GameRootDir:"=%\"
)

endlocal
