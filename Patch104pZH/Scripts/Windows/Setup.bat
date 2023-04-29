@echo off

set SetupDir=%~dp0.

:: Version, size and hash. Sets which Mod Builder is used.
set ModBuilderVer=2.0
set ModBuilderArcSize=31296792
set ModBuilderArcSha256=88eecc54dca509734f260f8813adc6c2759042be743a8cf4e7427f48ae1dbaf7

:: The mod config files. Relative to this setup file.
set ConfigFiles=^
    "%SetupDir%\..\..\ModBundleItems.json" ^
    "%SetupDir%\..\..\ModBundleAudioItems.json" ^
    "%SetupDir%\..\..\ModBundleLanguageItems.json" ^
    "%SetupDir%\..\..\ModBundlePacks.json" ^
    "%SetupDir%\..\..\ModChangeLog.json" ^
    "%SetupDir%\..\..\ModFolders.json" ^
    "%SetupDir%\WindowsRunner.json" ^
    "%SetupDir%\WindowsTools.json"

:: Misc path setup.
set ModBuilderDir=%SetupDir%\.modbuilder\v%ModBuilderVer%
set ModBuilderExe=%ModBuilderDir%\generalsmodbuilder\generalsmodbuilder.exe
set ModBuilderArc=%ModBuilderDir%\generalsmodbuilder.7z
set ModBuilderArcUrl=https://github.com/TheSuperHackers/GeneralsModBuilder/releases/download/v%ModBuilderVer%/generalsmodbuilder_v%ModBuilderVer%.7z

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
