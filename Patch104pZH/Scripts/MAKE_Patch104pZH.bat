set ThisDir1=%~dp0
call %ThisDir1%SETUP_Folders.bat

:: Define big file name(s)
set BigName=600_Patch104pZH

:: Free folders of big file contents
del /s /f /q %GeneratedBigFilesUnpackedDir%\%BigName%
del /s /f /q %GeneratedBigFilesDir%\%BigName%.big

:: Copy .big contents
:: All files listed here become part of the core of Patch104p and are meant
:: to be critical for client compatibility and essential for functionality.
:: Optional files should be moved into one of the other scripts.
xcopy /Y /S %GameFilesDir%\*.ini %GeneratedBigFilesUnpackedDir%\%BigName%\
xcopy /Y /S %GameFilesDir%\*.wnd %GeneratedBigFilesUnpackedDir%\%BigName%\
xcopy /Y /S %GameFilesDir%\Art\W3D\AVAvnger.W3D %GeneratedBigFilesUnpackedDir%\%BigName%\
xcopy /Y /S %GameFilesDir%\Art\W3D\AVAvnger_D.W3D %GeneratedBigFilesUnpackedDir%\%BigName%\
xcopy /Y /S %GameFilesDir%\Art\W3D\NVLOutpost.W3D %GeneratedBigFilesUnpackedDir%\%BigName%\
xcopy /Y /S %GameFilesDir%\Art\W3D\NVLOutpost_D.W3D %GeneratedBigFilesUnpackedDir%\%BigName%\

:: Generate .big file(s)
%ToolsDir%\GeneralsBigCreator\GeneralsBigCreator.exe -source %GeneratedBigFilesUnpackedDir%\%BigName% -dest %GeneratedBigFilesDir%\%BigName%.big

:: Generate Release file(s)
xcopy /Y %GeneratedBigFilesDir%\%BigName%.big %GeneratedReleaseUnpackedDir%\%BigName%.big*
