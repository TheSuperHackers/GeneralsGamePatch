echo on
set ThisDir1=%~dp0.
set ThisArg1=%~1
call "%ThisDir1%\SETUP_Folders.bat"

:: Define big file name(s)
set BigName=600_Patch104pZH
set GeneratedReleaseUnpackedFiles=%GeneratedReleaseUnpackedFiles% %BigName%.big

if "%ThisArg1%"=="build" (
    :: Free folders of big file contents
    del /f /q /s "%GeneratedBigFilesUnpackedDir%\%BigName%"
    del /f /q    "%GeneratedBigFilesDir%\%BigName%.big"
    
    :: Copy .big contents
    :: All files listed here become part of the core of Patch104p and are meant
    :: to be critical for client compatibility and essential for functionality.
    :: Optional files should be moved into one of the other scripts.
    xcopy /y /s "%GameFilesDir%\*.ini"                            "%GeneratedBigFilesUnpackedDir%\%BigName%\"
    xcopy /y /s "%GameFilesDir%\*.wnd"                            "%GeneratedBigFilesUnpackedDir%\%BigName%\"
    xcopy /y    "%GameFilesDir%\Art\Textures\exlaser3.dds"        "%GeneratedBigFilesUnpackedDir%\%BigName%\Art\Textures\"
    xcopy /y    "%GameFilesDir%\Art\Textures\gxmammoth_co.tga"    "%GeneratedBigFilesUnpackedDir%\%BigName%\Art\Textures\"
    xcopy /y    "%GameFilesDir%\Art\Textures\gxmammothalt_HI.tga" "%GeneratedBigFilesUnpackedDir%\%BigName%\Art\Textures\"
    xcopy /y    "%GameFilesDir%\Art\Textures\SSTechWarFactory_L.tga" "%GeneratedBigFilesUnpackedDir%\%BigName%\Art\Textures\"
    xcopy /y    "%GameFilesDir%\Art\W3D\ABSWGLink_L.W3D"          "%GeneratedBigFilesUnpackedDir%\%BigName%\Art\W3D\"
    xcopy /y    "%GameFilesDir%\Art\W3D\AVAvnger.W3D"             "%GeneratedBigFilesUnpackedDir%\%BigName%\Art\W3D\"
    xcopy /y    "%GameFilesDir%\Art\W3D\AVAvnger_D.W3D"           "%GeneratedBigFilesUnpackedDir%\%BigName%\Art\W3D\"
    xcopy /y    "%GameFilesDir%\Art\W3D\EXCarptBmb2.W3D"          "%GeneratedBigFilesUnpackedDir%\%BigName%\Art\W3D\"
    xcopy /y    "%GameFilesDir%\Art\W3D\NVLOutpost.W3D"           "%GeneratedBigFilesUnpackedDir%\%BigName%\Art\W3D\"
    xcopy /y    "%GameFilesDir%\Art\W3D\NVLOutpost_D.W3D"         "%GeneratedBigFilesUnpackedDir%\%BigName%\Art\W3D\"
    
    :: Generate .big file(s)
    "%ToolsDir%\GeneralsBigCreator\GeneralsBigCreator.exe" -source "%GeneratedBigFilesUnpackedDir%\%BigName%" -dest "%GeneratedBigFilesDir%\%BigName%.big"
    
    :: Generate Release file(s)
    xcopy /y "%GeneratedBigFilesDir%\%BigName%.big" "%GeneratedReleaseUnpackedDir%\"
)
