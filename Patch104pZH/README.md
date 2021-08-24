# Patch104pZH

#### How to make game changes
* Add and edit game files in *GameFilesEdited* folder.
* When adding an original game file with text contents, please submit the file as is first before adding any changes. This will preserve change history.

#### Build and test project files in Windows 10
* MAKE_Install.bat : Edit game install path in file, run (As Administrator) to generate project .big files, copy to game install path.
* MAKE_Install_Run.bat : Run (As Administrator) to generate project .big files, copy to game install path, start the game process (-win -quickstart).
* MAKE_Release.bat : Run to generate project .big files, pack files to .zip file, copy to Release folder.

#### How to run batch (.bat) file As Administrator
* Press WINDOWS_KEY + R
* In Run window, type *cmd*
* Press CTRL + SHIFT + ENTER to run As Administrator
* In Command Prompt window, type *cd /D C:\YOUR\PATH\TO\REPOSITORY\Patch104pZH*
