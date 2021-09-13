FinalBIG

Version 0.4 Beta released March 20th, 2006.

Copyright by Matthias Wagner 2006

C&C Generals is a trademark or registered trademark of Electronic Arts in the USA and/or other countries. All rights reserved.
The Lord of the Rings(tm), The Battle for Middle-earth(tm) is a trademark or registered trademark of Electronic Arts in the USA and/or other countries. All rights reserved.
LucasArts, the LucasArts logo, STAR WARS and related properties are trademarks in the United States and/or in other countries of Lucasfilm Ltd. and/or its affiliates. (c) 2006 Lucasfilm Entertainment Company Ltd. or Lucasfilm Ltd.  All rights reserved.

This software is based in part on the work of the Independent JPEG Group


-----------
Information
-----------
FinalBIG is a viewer and editor for the BIG files of C&C Generals and Lord of the Rings: Battle for Middle Earth. 
It can also open and save the MEG files of Star Wars(TM): Empire at War(TM).
I tried to make it as easy to use as possible.

-------
Contact
-------
Suggestions? Questions?

Mail: webmaster *at* wagnerma.de
Website: http://www.wagnerma.de

-------
Credits
-------
Thanks to Jonathan Wilson for W3D help
Thanks to Deezire for his Module list
Thanks to Waraddict for adding modules
Uses CRC code available at http://www.zorc.breitbandkatze.de/crc.html
Uses MEG file information found here: http://alpha1.dyns.net/eaw/MegFileFormat, http://www.technical-difficulties.com/

-------
License
-------
FinalBIG is freeware and is provided "as-is". Use at your own risk.
No reverse engineering allowed. Editing finalbig.ini welcome.
Please don't mirror FinalBIG without asking me.

--------------------
System Requirements
--------------------
-	OpenGL drivers installed
-	DirectX 9.0c installed (for DX9 version)
-	Tested on WinXP only

----------
HOW TO USE
----------
Actually FinalBIG is very easy to use, especially if you are used to other packaging & compression programs.
You can use FinalBIG to distribute your modifications to Generals and LOTR:BFME.
To open a BIG file, just click on File->Open and select your BIG file. You can now browse the files
included in this BIG file. However, you can also edit it. You can do this either by using the Edit menu,
or you can drag & drop files from Windows Explorer into FinalBIG. Just drop the files (or directories!)
on the file list of your BIG file. A window will come up telling you that FinalBIG needs to activate EditMode.
Accept that, but you really should back up any original BIG files before saving. That´s it! Now save your work,
and you are done!
It works exactly the same way for MEG files.

----------
W3D Viewer
----------
The W3D viewer should display almost all W3Ds fine. 
If you want to rotate the model, press the NumKeys (at the right of your keyboard).
8 is up, 2 is down, 4 is left, 6 is right.
You can also zoom in & out by pressing - and + (NumKeys).

This viewer probably will be extended to display SW:EAW models if I have the time to do this.

-----------
INI Editor
-----------
For Generals & LOTR Ini style files!
Easy to use. Right click and you'll be presented with several options regarding the clicked item.
For example, if you click inside an Object module you'll be presented with a list of Modules/Values to insert.
For many values you can also use Set Value, which will present you a list of values.
Just try it out in the several sections of an INI file.
If you click onto GoTo, another menu pops up that allows you to jump to the several sections inside the current
INI file.
Basically, you do not have to use the INI Editor menu, you can do everything by typing, too. FinalBIG does
not take away your freedom to plainly edit the INI by hand, it just additionally supports some helper features.

----------------
External Editors
----------------
Simple: Define your favorite editors using View->Options. Once you have done that, close the dialog.
Then simply select the file to edit at the left and press CTRL+E (or Edit->Edit with Editor).
FinalBIG will then launch the editor with the selected file. If you want to change the file, don't forget to
save the file in the editor (without changing the filename).
While the editor is opened, FinalBIG will block access to this specific file. This is to avoid sharing difficulties.

----------------
Quick Save
----------------
Currently only implemented for BIG files, this feature tries to only save any changed files inside
the BIG file. That way, it does need much less time than saving several hundred MB of unchanged data.
Keep in mind that this can increase the BIG file, so before distributing, use the normal Save command.
For MEG files, this just works as pressing Save, thus rewriting the whole MEG. However, I will work 
on implementing this feature for MEG files, too.

----------------
MEG File Support
----------------
Keep in mind that MEG files do not support lowercase letters inside filenames. FinalBIG automatically
changes those to uppercase letters.



---------------
TODO List
---------------
- 	Support QuickSave for MEG files (Top prio)
- 	Probably add viewer for SW:EAW models
- 	Probably add XML Editor with more features
- 	Probably add Texture->DDS support (for converting for example TGA's, BMP's etc into DDS format)



----------------------
Changes in 0.4 (beta)
----------------------
-	Support for saving & loading MEG files of Star Wars(TM): Empire At War(TM)
-	Support for DDS texture loading extended for SW: EAW

----------------------
Changes in 0.36 (beta)
----------------------
-	External Editor support: Use your favorite editors (like PSP, Wordpad, etc) to directly edit files inside the BIG file!

----------------------
Changes in 0.35 (beta)
----------------------
-	INI Editor extended: Lists modules & values and allows to set values *** IMPORTANT: I'm searching for people willing to complete the module list! ***
-	Adding a file to a BIG that already exists will now overwrite the original file (you'll be asked)
-	It may now be possible to open BIG files of other games than Generals/LOTR if the file format is compatible

-------------------
Changes in 0.34
-------------------
-	INI Editor
-	Quick Save

-------------------
Changes in 0.33
-------------------
-	W3D Viewer now displays (almost) all W3Ds correctly, including skins
-	JPEG and PNG support
-	Image viewer now uses correct aspect ratio (if width!=height)
-	Manual rotation and zooming possible in W3D viewer

-------------------
Changes in 0.32
-------------------
-	W3D viewer now displays all W3Ds correctly except skin meshes
-	W3D viewer now also displays textures (DDS, TGA and BMP)
-	D3D9 support (optionally)

-------------------
Changes in 0.31
-------------------
-	Added simple W3D viewer (no mesh hierarchy/textures supported yet, will come asap)
-	Fixed Crash Bug when pressing Cancel when inserting a directory

-------------------
Changes in 0.3
-------------------
-	Added Support for LOTR:BFME
-	Added TGA, BMP & DDS Viewer

-------------------
Changes in 0.21
-------------------
-	Fixed crash that occured sometimes when deleting files

-------------------
Changes in 0.2
-------------------
-	Deleting files
-	Renaming files
-	Drag & Drop for adding files & directories
-	Including the folder name when inserting a directory instead of skipping it

