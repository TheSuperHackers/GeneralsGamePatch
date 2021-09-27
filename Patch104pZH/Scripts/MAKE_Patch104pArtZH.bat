echo on
set ThisDir1="%~dp0."
set ThisArg1=%~1
call %ThisDir1%\SETUP_Folders.bat

:: Define big file name(s)
set BigName=600_Patch104pArtZH
set GeneratedReleaseUnpackedFiles=%GeneratedReleaseUnpackedFiles% %BigName%.big

if "%ThisArg1%"=="build" (
  :: Free folders of big file contents
  del /s /f /q %GeneratedBigFilesUnpackedDir%\%BigName%
  del /s /f /q %GeneratedBigFilesDir%\%BigName%.big
  
  :: Copy .big contents
  :: Add optional non-essential art files here.
  xcopy /y %GameFilesDir%\Art\W3D\NBPTower_DNS.W3D %GeneratedBigFilesUnpackedDir%\%BigName%\Art\W3D\
  xcopy /y %GameFilesDir%\Art\W3D\NBPTower_DS.W3D  %GeneratedBigFilesUnpackedDir%\%BigName%\Art\W3D\
  xcopy /y %GameFilesDir%\Art\W3D\NBPTower_ENS.W3D %GeneratedBigFilesUnpackedDir%\%BigName%\Art\W3D\
  xcopy /y %GameFilesDir%\Art\W3D\NBPTower_ES.W3D  %GeneratedBigFilesUnpackedDir%\%BigName%\Art\W3D\
  xcopy /y %GameFilesDir%\Art\W3D\NBPTower_NS.W3D  %GeneratedBigFilesUnpackedDir%\%BigName%\Art\W3D\
  xcopy /y %GameFilesDir%\Art\W3D\NBPTower_S.W3D   %GeneratedBigFilesUnpackedDir%\%BigName%\Art\W3D\
  
  :: Generate .big file(s)
  %ToolsDir%\GeneralsBigCreator\GeneralsBigCreator.exe -source %GeneratedBigFilesUnpackedDir%\%BigName% -dest %GeneratedBigFilesDir%\%BigName%.big
  
  :: Generate Release file(s)
  xcopy /y %GeneratedBigFilesDir%\%BigName%.big %GeneratedReleaseUnpackedDir%\%BigName%.big*
)
