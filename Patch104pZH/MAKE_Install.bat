call MAKE_Patch104pZH.bat
call SETUP_UserSettings.bat

::Copy release files to game
xcopy /Y /S %GeneratedReleaseUnpackedDir% %GameRootDir%
