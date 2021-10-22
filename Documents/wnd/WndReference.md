# WND File Reference

## General Overview

WND format is not meant to be edited by hand, but it can be done so with ease and precision.

WND file needs to be edited and tested carefully. Corrupting the format will crash the game on start.

Before moving any elements around, adjust the `CREATIONRESOLUTION` on all elements first.
 Set this to match your mockups. Window elements will automatically scale up or down in both X and Y
 with the user selected game resolution.

WND does not allow for comments, but most elements can have custom names that help describing it:
 NAME = "MyWindow.wnd:MyAmazingButton"

Avoid resizing window element to 0 size. It can crash the game on runtime:
 `SCREENRECT = UPPERLEFT: 0 0, BOTTOMRIGHT: 0 0`
 
Hide window elements by setting the following STATUS flags:
 `STATUS = ENABLED+HIDDEN+SEE_THRU+NOINPUT+NOFOCUS`
  
Block screen areas for user input by placing window element with:
 `INPUTCALLBACK = "GameWinBlockInput"`

Window elements with `WINDOWTYPE = SCROLLLISTBOX` cannot render large text rows correctly.
 Avoid using long texts and/or large fonts. Standard HeaderTemplate.ini configuration
 displayed at 1920x1080 Resolution is almost as high as it can go without breaking.

Window transitions styles can be added to `Data\INI\WindowTransitions.ini` file. Styles are
| Keyword               | Description                                         |
|-----------------------|-----------------------------------------------------|
| FLASH                 | Fine White Flash                                    |
| BUTTONFLASH           | Bright FLASH, emits fade sound                      |
| FULLFADE              | Black Fade                                          |
| TEXTONFRAME           | used on static text with delay                      |
| COUNTUP               | used in static numbers with delay                   |
| SCORESCALEUP          | Used in Images on Scorescreen, emits ticks sounds   |
| CONTROLBARARROW       | Doesnt work with screens                            |
| SCREENFADE            | Used by all screen                                  |
| WINSCALEUP            | Same as SCORESCALEUP but emits Shwoosh sound        |
| MAINMENUMEDIUMSCALEUP |                                                     |
| REVERSESOUND          | used in borders, acts like FULLFADE                 |


## Window element attributes

```
WINDOWTYPE
  +USER
  +PUSHBUTTON
  +RADIOBUTTON
  +ENTRYFIELD
  +STATICTEXT
  +PROGRESSBAR
  +SCROLLLISTBOX
  +COMBOBOX
  +CHECKBOX
  +HORZSLIDER
  +VERTSLIDER
```

```
SCREENRECT
  UPPERLEFT: X Y,
  BOTTOMRIGHT: X Y,
  CREATIONRESOLUTION: X Y
```

```
NAME = 
  "WindowName.wnd:ElementName"
```

```
STATUS =
  +ENABLED
  +HIDDEN
  +SEE_THRU
  +IMAGE
  +BORDER
  +NOINPUT
  +NOFOCUS
  +DRAGABLE
  +WRAP_CENTERED
  +ON_MOUSE_DOWN
  +HOTKEY_TEXT
  +RIGHT_CLICK
  +CHECK_LIKE
  +TABSTOP
```

```
STYLE =
  +USER
  +MOUSETRACK
  +PUSHBUTTON
  +RADIOBUTTON
  +ENTRYFIELD
  +STATICTEXT
  +PROGRESSBAR
  +SCROLLLISTBOX
  +COMBOBOX
  +CHECKBOX
  +HORZSLIDER
  +VERTSLIDER
```

```
SYSTEMCALLBACK =
  "[None]"
  "PassMessagesToParentSystem"
  ...
```
  
```
INPUTCALLBACK =
  "[None]"
  "GameWinBlockInput"
  ...
```
  
```
TOOLTIPCALLBACK =
  "[None]"
  ...
```
  
```
DRAWCALLBACK =
  "[None]"
  "W3DNoDraw"
  "W3DGadgetPushButtonImageDraw"
  "W3DGameWinDefaultDraw"
  ...
```
  
```
FONT =
  NAME: "Font"
  SIZE: 0..n
  BOLD: 0..1
```
  
```
HEADERTEMPLATE =
  "[None]"
  "Title"
  "Title"
  "MainButton"
  "Button"
  "ButtonSmall"
  "TextEntry"
  "ComboBoxEntry"
  "MinorTitle"
  "LabelRegular"
  "LabelSmall"
  "LoadScreenCameos"
  "LoadScreenMissionLocation"
  "Arial10BoldTemplate"
  "Arial12BoldTemplate"
  "Arial14Template"
  "Arial14BoldTemplate"
  ...
  See Data\Language\HeaderTemplate.ini
```

```
TOOLTIPDELAY =
  -1
  0..n
```

```
TEXT =
  "CATEGORY:StringName"
  ...
  See Data\Language\generals.csf
```

```
TEXTCOLOR =
  ENABLED: R G B A,
  ENABLEDBORDER: R G B A,
  DISABLED: R G B A,
  DISABLEDBORDER: R G B A,
  HILITE: R G B A,
  HILITEBORDER: R G B A
```
