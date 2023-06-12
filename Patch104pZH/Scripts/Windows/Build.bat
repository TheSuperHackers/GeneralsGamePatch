@echo off

echo cmd: Setup ...

call "%~dp0.\Setup.bat"

echo cmd: Request Admin ...

call "%~dp0.\RequestAdmin.bat" "%~s0" %*

if %errorlevel% equ 111 (
    exit /B 0
)

if %errorlevel% neq 0 (
    pause
    exit /B %errorlevel%
)

echo cmd: Build Generals Mod Builder ...

call "%PythonExe%" "%BuildPy%" ^
    --build-definition-file "%BuildJson%"

if %errorlevel% neq 0 (
    pause
    exit /B %errorlevel%
)
