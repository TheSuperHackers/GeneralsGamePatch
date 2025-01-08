### List of Textures Locations in `ini` Files

This documentation provides a list of the locations where textures (images) are referenced within
various `.ini` configuration files. These textures are typically used for graphical elements such as
animations, buttons, portraits, and other UI components in the game.

Below, you will find examples of how and where the images are defined within different `.ini` files.
Each entry includes a reference to an image file used for a specific purpose, marked by
the `Image`, `ButtonImage`, or similar tags, or a texture marked by `Texture` or `Model`.

For each `.ini` file, a list of tags that reference images or textures is provided. These tags identify
the locations within the file where textures are used. Note that the texture values may appear immediately
after the tag or after an equal sign (`=`).

### Regex Explanation

The regular expressions (regex) used in this documentation are designed to capture texture
and image references in `.ini` files, specifically the names of the textures and images associated with the tags.
The regex patterns take into account possible variations in how textures are defined, such as:

- **Presence of an equal sign (`=`)**: Some tags may have a texture/image name assigned using an equal 
  sign (e.g., `BioPortraitSmall = texture_name`), and the regex is designed to capture this format.
- **Optional whitespace**: The regex allows for varying amounts of whitespace around the tags,
  equal signs, and texture/image names.
- **Ignoring comments**: The regex ensures that any comments following the `;` symbol are ignored, 
  and only the texture/image names are captured.

### INI Folder List

<details>
  <summary>Click to expand</summary>

File: `Animation2D.ini` <br>
Tags: `Image` (image) <br>
Regex Expression (Image): `^\s*Image\s*(?:=\s*([^\s;]+))?\s*(?:;.*)?$`

---
File: `ChallengeMode.ini` <br>
Tags: `BioPortraitSmall` (image), `BioPortraitLarge` (image), `DefeatedImage` (image), `VictoriousImage` (image) <br>
Regex Expression (Image): `^\s*(BioPortraitSmall|BioPortraitLarge|DefeatedImage|VictoriousImage)\s*(?:=\s*([^\s;]+))?\s*(?:;.*)?$`

---
File: `CommandButton.ini` <br>
Tags: `ButtonImage` (image) <br>
Regex Expression (Image): `^\s*ButtonImage\s*(?:=\s*([^\s;]+))?\s*(?:;.*)?$`


File: `ControlBarScheme.ini` <br>
Tags: 3 types of tags:
1. **Tags without images**:  
   The following tags do not specify images.
   ```
   side value ; no image
   GenBarButtonIn value ; no image
   GenBarButtonOn value ; no image
   ```

2. **Tags with images**:  
   Tags with string value in one word and not numbers only represent images.  
   ```
   GenBarButtonIn SNBarButtonGen2IN ; image
   ```

3. **Tags without images**:  
   Tags containing multiple words or numbers only or no value represent no images. 
   ```
   ButtonBorderSystemColor R:207 G:195 B:2 A:255 ; no image
   ScreenCreationRes X:800 Y:600 ; no image
   Layer 4 ; no image
   tag ; no image
   ```
   
Regex Expression (Image): `^\s*(?!(?:ControlBarScheme|Side|GenBarButtonIn|GenBarButtonOn)\b)(\S+)\s+([^\s;]+)\s*(?:;.*)?$`

---
File: `Crate.ini` <br>
Tags: `Model` (w3d texture file) <br>
Regex Expression (Texture): `^\s*Model\s*(?:=\s*)?(\S+)\s*(?:;.*)?$`

---
File: `GameData.ini` <br>
Tags: `MoveHintName` (W3D texture file) <br>
Regex Expression (Texture): `^\s*MoveHintName\s*(?:=\s*)?(\S+)\s*(?:;.*)?$`

---
File: `InGameUI.ini` <br>
Tags: `Texture` (texture file) <br>
Regex Expression (Texture): `^\s*Texture\s*(?:=\s*)?(\S+)\s*(?:;.*)?$`

---
File: `Mouse.ini` <br>
Tags: `Image` (image), `Texture` (texture file) <br>
Regex Expression (Image): `^\s*Image\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$` <br>
Regex Expression (Texture): `^\s*Texture\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$`

---
File: `ObjectCreationList.ini` <br>
Tags: `ModelNames` (multple w3d texture file), `Texture` (texture file) <br>
Regex Expression (Texture): `^\s*(ModelNames|Texture)\s*(?:=\s*)?((?:[^\s;]+\s*)+)(?:;.*)?$`

---
File: `ParticleSystem.ini` <br>
Tags: `ParticleName` (texture file with extension) <br>
Regex Expression (Texture): `^\s*ParticleName\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$`

---
File: `PlayerTemplate.ini` <br>
Tags: `ScoreScreenImage` (image), `LoadScreenImage` (image), `GeneralImage` (image), `FlagWaterMark` (image),
`EnabledImage` (image), `SideIconImage` (image), `MedallionRegular` (image), `MedallionHilite` (image), `MedallionSelect` (image) <br>
Regex Expression (Image): `^\s*(ScoreScreenImage|LoadScreenImage|GeneralImage|FlagWaterMark|EnabledImage|SideIconImage|MedallionRegular|MedallionHilite|MedallionSelect)\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$`

---
File: `Roads.ini` <br>
Tags: `Texture` (texture file with extension), `TextureDamaged` (texture file with extension),
`TextureReallyDamaged` (texture file with extension), `TextureBroken` (texture file with extension),
`BridgeModelName` (w3d texture file), `BridgeModelNameDamaged` (w3d texture file),
`BridgeModelNameReallyDamaged` (w3d texture file), `BridgeModelNameBroken` (w3d texture file) <br>
Regex Expression (Texture): `^\s*(Texture|TextureDamaged|TextureReallyDamaged|TextureBroken|BridgeModelName|BridgeModelNameDamaged|BridgeModelNameReallyDamaged|BridgeModelNameBroken)\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$`

---
File: `Terrain.ini` <br>
Tags: `Texture` (texture file with extension) <br>
Regex Expression (Texture): `^\s*Texture\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$`

---
File: `Upgrade.ini` <br>
Tags: `ButtonImage` (image) <br>
Regex Expression (Image): `^\s*ButtonImage\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$`

---
File: `Water.ini` <br>
Tags: `SkyTexture` (texture file with extension), `WaterTexture` (texture file with extension), `StandingWaterTexture` (texture file with extension) <br>
Regex Expression (Texture): `^\s*(SkyTexture|WaterTexture|StandingWaterTexture)\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$`

---
File: `Weather.ini` <br>
Tags: `SnowTexture` (texture file with extension) <br>
Regex Expression (Texture): `^\s*SnowTexture\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$`

</details>

### Default Folder List

<details>
  <summary>Click to expand</summary>

File: `Default/ControlBarScheme.ini` <br>
Regex Expression (Image): `^\s*(?!(?:ControlBarScheme|Side|GenBarButtonIn|GenBarButtonOn)\b)(\S+)\s+([^\s;]+)\s*(?:;.*)?$`

---
File: `Upgrade.ini` <br>
Tags: `ButtonImage` (image) <br>
Regex Expression (Image): `^\s*ButtonImage\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$`


</details>

### Object Folder List

<details>
  <summary>Click to expand</summary>

All the ini files in the Object folder have the same tags. <br>
Tags: `Texture` (texture file with or without extension), `Model` (w3d texture file),
      `TrackMarks` (texture file with extension), `ShadowI` (texture file)
      `Animation` ([w3d texture file].[w3d_texture_file]), `IdleAnimation` ([w3d texture file].[w3d_texture_file]),
      `SelectPortrait` (image), `ButtonImage` (image) <br>

Regex Expression (Image): `^\s*(SelectPortrait|ButtonImage)\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$` <br>
Regex Expression (Texture): `^\s*(Texture|Model|TrackMarks|ShadowI|IdleAnimation|Animation)\s*(?:=\s*)?(?:([^.\s;]+)(?:\.[^\s;]+)?|([^\s;]+\.[^\s;]+))\s*(?:;.*)?$` <br>

</details>