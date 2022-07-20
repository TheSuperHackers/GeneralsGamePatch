@echo off

setlocal

set ThisDir=%~dp0.

call "%ThisDir%\Windows\RequestAdmin.bat" "%~s0" %*

if %errorlevel% EQU 111 (
    exit /B %errorlevel%
)

call "%ThisDir%\Windows\InstallModBuilder.bat"

if %errorlevel% EQU 222 (
    exit /B %errorlevel%
)

call "%ThisDir%\Windows\Setup.bat" print

call "%ModBuilderExe%" --build --release --config-list %ConfigFiles% %*

endlocal
