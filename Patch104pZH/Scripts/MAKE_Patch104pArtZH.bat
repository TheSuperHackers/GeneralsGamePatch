set ThisDir1=%~dp0
call %ThisDir1%SETUP_Folders.bat

:: Define big file name(s)
set BigName=600_Patch104pArtZH

:: Free folders of big file contents
del /s /f /q %GeneratedBigFilesUnpackedDir%\%BigName%
del /s /f /q %GeneratedBigFilesDir%\%BigName%.big

:: Copy .big contents
xcopy /Y /S %GameFilesDir%\Art\W3D\AVAvnger.W3D %GeneratedBigFilesUnpackedDir%\%BigName%\
xcopy /Y /S %GameFilesDir%\Art\W3D\AVAvnger_D.W3D %GeneratedBigFilesUnpackedDir%\%BigName%\
xcopy /Y /S %GameFilesDir%\Art\W3D\NBPTower_DNS.W3D %GeneratedBigFilesUnpackedDir%\%BigName%\
xcopy /Y /S %GameFilesDir%\Art\W3D\NBPTower_DS.W3D %GeneratedBigFilesUnpackedDir%\%BigName%\
xcopy /Y /S %GameFilesDir%\Art\W3D\NBPTower_ENS.W3D %GeneratedBigFilesUnpackedDir%\%BigName%\
xcopy /Y /S %GameFilesDir%\Art\W3D\NBPTower_ES.W3D %GeneratedBigFilesUnpackedDir%\%BigName%\
xcopy /Y /S %GameFilesDir%\Art\W3D\NBPTower_NS.W3D %GeneratedBigFilesUnpackedDir%\%BigName%\
xcopy /Y /S %GameFilesDir%\Art\W3D\NBPTower_S.W3D %GeneratedBigFilesUnpackedDir%\%BigName%\
xcopy /Y /S %GameFilesDir%\Art\W3D\NVLOutpost.W3D %GeneratedBigFilesUnpackedDir%\%BigName%\
xcopy /Y /S %GameFilesDir%\Art\W3D\NVLOutpost_D.W3D %GeneratedBigFilesUnpackedDir%\%BigName%\

:: Generate .big file(s)
%ToolsDir%\GeneralsBigCreator\GeneralsBigCreator.exe -source %GeneratedBigFilesUnpackedDir%\%BigName% -dest %GeneratedBigFilesDir%\%BigName%.big

:: Generate Release file(s)
xcopy /Y %GeneratedBigFilesDir%\%BigName%.big %GeneratedReleaseUnpackedDir%\%BigName%.big*
