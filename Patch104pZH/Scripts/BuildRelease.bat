@echo off

setlocal

set ThisDir=%~dp0.

call "%ThisDir%\Windows\RequestAdmin.bat" "%~s0" %*

if %errorlevel% equ 111 (
    exit /B 0
)

if %errorlevel% neq 0 (
    pause
    exit /B %errorlevel%
)

call "%ThisDir%\Windows\InstallModBuilder.bat"

if %errorlevel% neq 0 (
    pause
    exit /B %errorlevel%
)

call "%ThisDir%\Windows\Setup.bat"

call "%ModBuilderExe%" ^
  --build ^
  --release ^
  --verbose-logging ^
  --config-list %ConfigFiles% %*

endlocal
