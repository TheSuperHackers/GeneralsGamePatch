## How to use

Install Python 3.10.x before launching any of the scripts in this folder.

If the python 3.10 executable is not added to the PATH environment variable, then specify the path to python 3.10 in `Windows\UserSetup.bat` by creating a copy of `Windows\UserSetup.template.bat`.

For example, inside `Windows\UserSetup.bat`:

```
set PythonExe=C:\Python310\python
```

Prefer using the `BuildInstallRunWithGui.bat` script to launch Mod Builder with GUI in its default project configuration.

## Troubleshooting

If the build process was started with an incompatible Python version once and is stuck in an error state, then go to the `ModBuilder` directory and delete the `.venv` directories.
