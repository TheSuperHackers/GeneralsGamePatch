@echo off

set SetupDir=%~dp0.

set ModBuilderVer=1.1
set ModBuilderDir=%SetupDir%\.GeneralsModBuilder\v%ModBuilderVer%
set ModBuilderExe=%ModBuilderDir%\generalsmodbuilder.exe
set ModBuilderZip=%ModBuilderDir%\generalsmodbuilder.zip
set ModBuilderZipUrl=https://github.com/TheSuperHackers/GeneralsTools/raw/main/Tools/generalsmodbuilder/v%ModBuilderVer%/generalsmodbuilder_v%ModBuilderVer%.zip
set ModBuilderZipSha256=4381dc52af1d03ac239da01368be0e976527caffd5d2261b56eb80100e5cd9d1
set ModBuilderZipSize=7884988

set ConfigDir=%SetupDir%\..\..
set ConfigFiles=^
    "%ConfigDir%\ModBundleItems.json" ^
    "%ConfigDir%\ModBundlePacks.json" ^
    "%ConfigDir%\ModFolders.json" ^
    "%ConfigDir%\ModRunner.json"

if [%~1]==[print] (
    echo SETUP. Using Generals Mod Builder:
    echo ver... %ModBuilderVer%
    echo dir... %ModBuilderDir%
    echo exe... %ModBuilderExe%
    echo zip... %ModBuilderZip%
    echo zipurl %ModBuilderZipUrl%
    echo zipsha %ModBuilderZipSha256%
    echo zipsiz %ModBuilderZipSize%
    for %%f in (%ConfigFiles%) do (
        echo config %%f
    )
    echo SETUP END.
)
