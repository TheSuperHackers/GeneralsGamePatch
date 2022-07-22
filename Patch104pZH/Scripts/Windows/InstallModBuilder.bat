setlocal

set ThisDir=%~dp0.
set WasDownloaded=0
set WasInstalled=0

call "%ThisDir%\Setup.bat"

if not exist %ModBuilderExe% (
    if not exist %ModBuilderArc% (
        echo Installing Generals Mod Builder at '%ModBuilderDir%' ...

        if not exist "%ModBuilderDir%" (
            mkdir "%ModBuilderDir%"
        )

        echo Download '%ModBuilderArcUrl%' ...
        curl --location "%ModBuilderArcUrl%" --output "%ModBuilderArc%" --max-filesize %ModBuilderArcSize%
    )
    set WasDownloaded=1
) else (
    echo Generals Mod Builder is installed
)

if %WasDownloaded% NEQ 0 (
    if exist "%ModBuilderArc%" (
        echo Check Generals Mod Builder archive ...
        for /F %%I in ("%ModBuilderArc%") do (
            if %%~zI NEQ %ModBuilderArcSize% (
                echo File '%ModBuilderArc%' does not have expected size %ModBuilderArcSize%
                exit /B 222
            )
        )

        echo Hash Generals Mod Builder archive ...
        Certutil -hashfile "%ModBuilderArc%" SHA256 | findstr /c:%ModBuilderArcSha256%

        if %errorlevel% EQU 0 (
            echo Extract archive '%ModBuilderArc%' ...
            "%ThisDir%\7z.exe" x "%ModBuilderArc%" -y -o"%ModBuilderDir%"

            echo Delete archive '%ModBuilderArc%' ...
            del /q "%ModBuilderArc%"

            set WasInstalled=1
        ) else (
            echo File '%ModBuilderArc%' does not have expected hash '%ModBuilderArcSha256%'
            exit /B 222
        )
    ) else (
        echo File '%ModBuilderArc%' failed to download
        exit /B 222
    )
)

if %WasInstalled% NEQ 0 (
    if not exist "%ModBuilderExe%" (
        echo File '%ModBuilderExe%' failed to install
        exit /B 222
    )
)

endlocal
