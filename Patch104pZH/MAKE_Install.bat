call MAKE_Patch104pZH.bat

set GameRootDir="F:\Program Files (x86)\EA Games\clean copy of ZH - Copy"

::Copy release files to game
xcopy /Y /S %GeneratedReleaseUnpackedDir% %GameRootDir%
