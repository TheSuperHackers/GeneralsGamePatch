# The Super Patch for Generals: Zero Hour

This project aims to fix and improve the original video game title "Command and Conquer Generals: Zero Hour" from Electronic Arts (EA).

An original copy of the game title with version 1.04 is required to use this Product. It does not function as a standalone Product.

Note: **EA has not endorsed and does not support this product.**

## Core objectives

- Fix game crashes, exploits, bugs and performance issues
- Fix major gameplay, visual and operability issues
- Stay true to the original content, design and art direction of Generals Zero Hour

## Additional objectives

- Build new tools to simplify access and use of Mods, Addons and other optional game content
- Retain best compatibility and accessibility to original Game version(s), Mods, Addons and Custom Maps
- Improve Game AI
- Improve Menu operability and visuals
- Improve Control Bar operability and visuals
- Fix and improve models, textures and audio
- Fix and improve Official Maps
- Add new Language(s)

## Change Logs

Version 1.0 (work in progress)

- [v1.0 all changes sorted by date](Patch104pZH/ReleaseFiles/English/Changes/v1.0/AllSortedByDate.md)
- [v1.0 all changes sorted by severity](Patch104pZH/ReleaseFiles/English/Changes/v1.0/AllSortedBySeverity.md)
- [v1.0 controversial changes sorted by faction](Patch104pZH/ReleaseFiles/English/Changes/v1.0/ControversialOnlySortedByFaction.md)
- [v1.0 USA changes sorted by date](Patch104pZH/ReleaseFiles/English/Changes/v1.0/UsaOnlySortedByDate.md)
- [v1.0 China changes sorted by date](Patch104pZH/ReleaseFiles/English/Changes/v1.0/ChinaOnlySortedByDate.md)
- [v1.0 GLA changes sorted by date](Patch104pZH/ReleaseFiles/English/Changes/v1.0/GlaOnlySortedByDate.md)
- [v1.0 art changes sorted by faction](Patch104pZH/ReleaseFiles/English/Changes/v1.0/ArtOnlySortedByFaction.md)

## Community Surveys

- [Survey 1 (General)](https://bit.ly/zh_survey_1ben)
- [Survey 2 (AI)](https://bit.ly/zh_survey_2en)

## External Discussions

- [GameReplays.org](https://bit.ly/zhpatch)

## Issues & Tasks

- [Tasks](Patch104pZH/Design/Tasks)
- [Issues](https://github.com/TheSuperHackers/GeneralsGamePatch/issues)

## How we approach core objectives

In our first survey we asked the community what they think about addressing bugs that affect gameplay: More than 90% of players want bugs to be fixed. Based on this result and also our discussions and experiences in the developer team, we decided to tackle changes and fixes with the following approach:

- Changes are created and tested in isolated development branches. If a change has severe controversial, but potentially positive effects on gameplay, then it will be reviewed and tweaked before it goes into the main branch.
- Changes are merged into the main development branch, so they can be tested in a combined setting. No changes are cemented: Tests, reviews and tweaks may be necessary to adjust changes further to fit them together well. If a change causes negative consequences that cannot be tweaked in a satisfying way, then it may be reverted entirely to the original state.
- Changes require input from players for accurate evaluation. Ideally changes are looked at in test environments and real matches to gather accurate data and impressions. It is worthwhile to know and consider which other controversial changes exist within the same game setting, as they can influence each other.
- Changes may be subject to a matter of preference that require the community to give input on. In such cases we will include related questions in new surveys and evaluate and apply the results accordingly.

## Build

The project is built with the [Generals Mod Builder](https://github.com/TheSuperHackers/GeneralsModBuilder), which is a git submodule, so clone recursively:

```
git clone --recursive https://github.com/TheSuperHackers/GeneralsGamePatch
```

If the repository is already cloned, fetch the submodule with:

```
git submodule update --init --recursive
```

Nothing else needs to be installed. The Mod Builder launcher installs [uv](https://docs.astral.sh/uv/) on first use, and uv then downloads a suitable Python and the required packages by itself.

Run any of the scripts in [Patch104pZH/Scripts](Patch104pZH/Scripts):

| Script | What it does |
| --- | --- |
| `BuildInstall.bat` | Builds the patch and installs it into the game folder |
| `BuildInstallRun.bat` | Builds, installs, runs the game, then uninstalls when the game closes |
| `BuildInstallRunWithGui.bat` | The same, with the graphical interface |
| `BuildRelease.bat` | Builds the patch and packs the release archives |
| `Uninstall.bat` | Removes the patch from the game folder |

The submodule commit decides which Mod Builder version is used. Upgrade it with:

```
git submodule update --remote Tools/GeneralsModBuilder
git add Tools/GeneralsModBuilder
git commit -m "Upgrade the Mod Builder"
```

## CONTRIBUTE

[How to contribute](CONTRIBUTE.md)

## LICENSE

[GPL v3 License](LICENSE.txt)

[Electronic Arts & The Super Hacker Terms](TERMS.txt)

## DONATE

[Donation info page](DONATE.md)
