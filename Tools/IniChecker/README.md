# Ini Checker
(PC only)

## Description

This tool was developed for mod makers. It finds errors in Generals Zero Hour ini code as well as in scripts automatically. It does not fix errors. Ini Checker just helps to find them. It performs hundreds of checks and allows to detect many types of bugs, but not all of them. So, don't rely on it very much. Some errors can stay.

Ini Checker 3.1 consists of three modules: Ini Scanner, Hotkey Fixer and Scripts Analyzer.

Hotkey Fixer allows you to find free hotkeys for your new buttons with one click and solve hotkey conflicts with ease.

Ini Scanner checks the code and displays you errors and warnings. Some warning are not errors. They point to strange code constructions, which should be checked manually.

## How to use

Unpack the archive. Start Ini Checker. Click "Browse" and find any of your ini files. This is needed to define the folder with ini files you want to check. Nothing more. You don't need to open each file. After you are done, the path similar to this string will appear: "C:/Games/Generals Zero Hour/Data/INI/". Note, that there is no any "Object", "Default" or any other folder in the end. You can also type folder location manually. Preparations are over. You can now start any of modules.

Work with Ini Scanner is easy. Just click "Scan" and wait for a couple of minutes. Then read all it has written. Not all of messages will be errors. Many of them will be just warnings. There is not division between errors and warnings. It puts everything into one heap. It also saves the log into TXT file. So, you can return to it later. Ini Scanner does not see files packed inside *.big archives. Thus, if you have only some INI files unpacked, it will show you many errors. In order the scanner to work properly, you need to have all files from INIZH.big unpacked.

If you use Hotkey Fixer click "Scan for hotkeys" and wait. It will analyze the code and find all buttons, inscriptions, all hotkeys and display them. There are 3 show modes: "Show all buttons", "Show conflicting only" and "Show without hotkeys only". You can choose any you like. Button names are arranged in alphabetic order. So, it is not difficult to find the button you need. Select the button of your choice and click "Suggest a hotkey". The program will analyze all command sets, all buttons, all hotkeys and suggest you a number of non-conflicting keys.

If you use Scripts Analyzer, then the path to SkirmishScripts.scb file will be filled automatically after you choose ini files. You just need to click "Analyze" button. If you want to check scripts for maps then you need to start World Builder first and export scripts from your map. When you are done, return to Ini Checker and point the path to the SCB-file. Note, that there is "Skirmish Scripts" inscription in the right bottom corner. The thing is that the same scripts will be errors for the skirmish AI and will be ok for maps. So, check "Skirmish Scripts" when you analyze skirmish AI and uncheck it for map scripts.

Note:
The program generates text automatically. Some messages can sound a bit weird. But I hope that everything is comprehensible.
