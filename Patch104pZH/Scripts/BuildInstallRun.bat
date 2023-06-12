@echo off

setlocal

call "%~dp0.\Windows\Build.bat"

echo cmd: Run Generals Mod Builder ...

call "%VenvPythonExe%" "%MainPy%" ^
    --build ^
    --install FullEnglish ^
    --run ^
    --uninstall ^
    --tools-root-dir "%ToolsRootDir%" ^
    --config-list %ConfigFiles% %*

endlocal
