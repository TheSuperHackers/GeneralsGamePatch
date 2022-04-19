setlocal

set ThisDir=%~dp0.
set WasInstalled=0

call "%ThisDir%\Setup.bat"

echo Hashing Generals Mod Builder ...
Certutil -hashfile "%ModBuilderExe%" SHA256 | findstr /c:%ModBuilderSha256%

if %errorlevel% NEQ 0 (
    echo Installing Generals Mod Builder at '%ModBuilderExe%'

    if not exist "%ModBuilderDir%" (
        echo Create folder '%ModBuilderDir%'
        mkdir "%ModBuilderDir%"
    )

    curl --location "%ModBuilderUrl%" --output "%ModBuilderExe%" --max-filesize %ModBuilderSize%

    :: Hash cannot be created and checked again in this scope for unknown reason
    set WasInstalled=1
)

if %WasInstalled% NEQ 0 (
    if not exist "%ModBuilderExe%" (
        echo File '%ModBuilderExe%' failed to install
        exit /B 222
    )

    echo Hashing Generals Mod Builder ...
    Certutil -hashfile "%ModBuilderExe%" SHA256 | findstr /c:%ModBuilderSha256%

    if %errorlevel% NEQ 0 (
        echo File '%ModBuilderExe%' does not have expected hash '%ModBuilderSha256%'
        exit /B 222
    )

    for /F %%I in ("%ModBuilderExe%") do (
        if %%~zI NEQ %ModBuilderSize% (
            echo File '%ModBuilderExe%' does not have expected size %ModBuilderSize%
            exit /B 222
        )
    )
)

endlocal
