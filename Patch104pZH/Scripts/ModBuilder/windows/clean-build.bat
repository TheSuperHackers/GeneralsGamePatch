set RootDir=%~dp0.\..

rd /s /q "%RootDir%\.build"
rd /s /q "%RootDir%\.pyinstaller"
rd /s /q "%RootDir%\.release"
rd /s /q "%RootDir%\__pycache__"
rd /s /q "%RootDir%\generalsmodbuilder\__pycache__"
rd /s /q "%RootDir%\generalsmodbuilder\build\__pycache__"
rd /s /q "%RootDir%\generalsmodbuilder\changelog\__pycache__"
rd /s /q "%RootDir%\generalsmodbuilder\config\.tools"
rd /s /q "%RootDir%\generalsmodbuilder\data\__pycache__"
rd /s /q "%RootDir%\generalsmodbuilder\gui\__pycache__"
