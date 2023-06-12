set RootDir=%~dp0.\..

rd /s /q "%RootDir%\.venv"
rd /s /q "%RootDir%\.venv-poetry"
rd /s /q "%RootDir%\.venv-pyinstaller"
