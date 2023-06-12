set RootDir=%~dp0.\..

python.exe "%RootDir%\buildproject.py" --build-definition-file "%RootDir%\build-lite.json"
