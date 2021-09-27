set ThisDir0="%~dp0."
call %ThisDir0%\Scripts\MAKE_Patch104pZH.bat build
call %ThisDir0%\Scripts\MAKE_Patch104pArtZH.bat build

:: Copy base release files
xcopy /y /s %ReleaseUnpackedDir%\* %GeneratedReleaseUnpackedDir%\*

:: Define archive name(s)
set ArchiveName=Patch104pZH

:: Generate Archive(s)
tar.exe -a -c -C %GeneratedReleaseUnpackedDir% -f %ReleaseDir%\%ArchiveName%.zip *.*
