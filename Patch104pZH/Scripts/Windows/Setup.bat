@echo off

set SetupDir=%~dp0.

:: Version, size and hash. Sets which Mod Builder is used.
set ModBuilderVer=1.6
set ModBuilderArcSize=30090046
set ModBuilderArcSha256=2996924b7e0d38986c2482a4409e4832749c727acf7950e866bdbf773c08d9a0

:: The mod config files. Relative to this setup file.
set ConfigFiles=^
    "%SetupDir%\..\..\ModBundleItems.json" ^
    "%SetupDir%\..\..\ModBundlePacks.json" ^
    "%SetupDir%\..\..\ModFolders.json" ^
    "%SetupDir%\..\..\ModRunner.json"

:: Misc path setup.
set ModBuilderDir=%SetupDir%\.modbuilder\v%ModBuilderVer%
set ModBuilderExe=%ModBuilderDir%\generalsmodbuilder\generalsmodbuilder.exe
set ModBuilderArc=%ModBuilderDir%\generalsmodbuilder.7z
set ModBuilderArcUrl=https://github.com/TheSuperHackers/GeneralsTools/raw/main/Tools/generalsmodbuilder/v%ModBuilderVer%/generalsmodbuilder_v%ModBuilderVer%.7z

:: Print setup info.
echo SETUP.BAT
echo modver %ModBuilderVer%
echo arcsiz %ModBuilderArcSize%
echo arcsha %ModBuilderArcSha256%
for %%f in (%ConfigFiles%) do (
    echo config %%f
)
echo moddir %ModBuilderDir%
echo modexe %ModBuilderExe%
echo arcfil %ModBuilderArc%
echo arcurl %ModBuilderArcUrl%
