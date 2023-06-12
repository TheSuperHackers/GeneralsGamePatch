import os
import time
import threading
import traceback
from tkinter import *
from tkinter.ttk import *
from typing import Callable
from generalsmodbuilder import util
from generalsmodbuilder.__version__ import VERSIONSTR
from generalsmodbuilder.build.engine import BuildEngine
from generalsmodbuilder.buildfunctions import CreateJsonFiles, RunWithConfig
from generalsmodbuilder.data.bundles import BundlePack, Bundles, AddBundlePacksFromJsons
from generalsmodbuilder.util import JsonFile


class Gui:
    workThread: threading.Thread
    abortThread: threading.Thread
    buildEngine: BuildEngine
    buildEngineLock: threading.RLock
    mainWindowLock: threading.RLock

    configPaths: list[str]
    buildAndInstallList: list[str]
    debug: bool
    toolsRootDir: str

    makeChangeLog: BooleanVar
    clean: BooleanVar
    build: BooleanVar
    release: BooleanVar
    install: BooleanVar
    uninstall: BooleanVar
    run: BooleanVar
    printConfig: BooleanVar
    clearConsole: BooleanVar

    bundlePackList: Listbox
    executeButton: Button
    makeChangeLogButton: Button
    cleanButton: Button
    buildButton: Button
    releaseButton: Button
    installButton: Button
    runButton: Button
    uninstallButton: Button
    abortButton: Button
    bundlePackRefreshButton: Button


    def __init__(self):
        self.workThread = None
        self.abortThread = None
        self.buildEngine = None
        self.buildEngineLock = threading.RLock()
        self.mainWindowLock = threading.RLock()
        self.configPaths = None
        self.buildAndInstallList = None
        self.debug = False
        self.toolsRootDir = None
        self._ClearMainWindowElements()


    def RunWithConfig(self,
            configPaths: list[str] = list(),
            installList: list[str] = list(),
            buildList: list[str] = list(),
            makeChangeLog: bool = False,
            clean: bool = False,
            build: bool = False,
            release: bool = False,
            install: bool = False,
            uninstall: bool = False,
            run: bool = False,
            debug: bool = False,
            printConfig: bool = False,
            toolsRootDir: str = None):

        self.configPaths = configPaths
        self.buildAndInstallList = installList
        self.buildAndInstallList.extend(buildList)
        self.debug = debug
        self.toolsRootDir = toolsRootDir

        mainWindow: Tk = Gui._CreateMainWindow()

        self.makeChangeLog = BooleanVar(mainWindow, value=makeChangeLog)
        self.clean = BooleanVar(mainWindow, value=clean)
        self.build = BooleanVar(mainWindow, value=build)
        self.release = BooleanVar(mainWindow, value=release)
        self.install = BooleanVar(mainWindow, value=install)
        self.uninstall = BooleanVar(mainWindow, value=uninstall)
        self.run = BooleanVar(mainWindow, value=run)
        self.printConfig = BooleanVar(mainWindow, value=printConfig)
        self.clearConsole = BooleanVar(mainWindow, value=True)

        self._CreateMainWindowElements(mainWindow)
        self._SetAbortElementsState("disabled")
        self._StartWorkThread(self._PopulateBundlePackList)

        mainWindow.mainloop()

        with self.mainWindowLock:
            self._ClearMainWindowElements()

        self.workThread.join()


    @staticmethod
    def _MakeIconFilePath(iconName: str) -> str:
        iconFile: str = os.path.join(util.g_appDir, "gui", iconName)
        return iconFile


    @staticmethod
    def _AddIconToWindow(window: Tk, iconFile: str) -> None:
        if os.path.isfile(iconFile):
            photoImage = PhotoImage(file = iconFile)
            window.wm_iconphoto(False, photoImage)


    @staticmethod
    def _CreateMainWindow() -> Tk:
        window = Tk()
        window.title(f"Generals Mod Builder v{VERSIONSTR} by The Super Hackers")
        window.geometry('660x270')
        window.resizable(0, 0)
        iconFile: str =  Gui._MakeIconFilePath("icon.png")
        Gui._AddIconToWindow(window, iconFile)
        return window


    def _CreateMainWindowElements(self, window: Tk) -> None:
        buttonWidth = 20
        checkboxWidth = 18
        listboxWidth = 21

        mainFrame = Frame(window, padding=10)
        mainFrame.pack()

        frame1000 = Frame(mainFrame)
        frame1000.grid(row=0, column=0, sticky='n')
        frame0100 = Frame(mainFrame)
        frame0100.grid(row=0, column=1, sticky='n')
        frame0010 = Frame(mainFrame)
        frame0010.grid(row=0, column=2, sticky='n')
        frame0001 = Frame(mainFrame)
        frame0001.grid(row=0, column=3, sticky='n')

        executeLabel = Label(frame0100, text = "Sequence execution")
        executeLabel.pack(anchor=CENTER)
        executeFrame = Frame(frame0100, padding=10, relief='solid')
        executeFrame.pack(padx=5, pady=5)

        optionsLabel = Label(frame0001, text = "Options")
        optionsLabel.pack(anchor=CENTER)
        optionsFrame = Frame(frame0001, padding=10, relief='solid')
        optionsFrame.pack(padx=5, pady=5)

        actionsLabel = Label(frame0010, text = "Single actions")
        actionsLabel.pack(anchor=CENTER)
        actionsFrame = Frame(frame0010, padding=10, relief='solid')
        actionsFrame.pack(padx=5, pady=5)

        bundlePackLabel = Label(frame1000, text = "Bundle Pack list")
        bundlePackLabel.pack(anchor=CENTER)
        bundlePackFrame = Frame(frame1000, padding=10, relief='solid')
        bundlePackFrame.pack(padx=5, pady=5)

        # Execute Frame

        makeChangeLogCheck = Checkbutton(executeFrame, width = checkboxWidth, text='Make Change Log', var=self.makeChangeLog)
        makeChangeLogCheck.pack(anchor=W)

        cleanCheck = Checkbutton(executeFrame, width = checkboxWidth, text='Clean', var=self.clean)
        cleanCheck.pack(anchor=W)

        buildCheck = Checkbutton(executeFrame, width = checkboxWidth, text='Build', var=self.build)
        buildCheck.pack(anchor=W)

        releaseCheck = Checkbutton(executeFrame, width = checkboxWidth, text='Build Release', var=self.release)
        releaseCheck.pack(anchor=W)

        installCheck = Checkbutton(executeFrame, width = checkboxWidth, text='Install', var=self.install)
        installCheck.pack(anchor=W)

        runCheck = Checkbutton(executeFrame, width = checkboxWidth, text='Run Game', var=self.run)
        runCheck.pack(anchor=W)

        uninstallCheck = Checkbutton(executeFrame, width = checkboxWidth, text='Uninstall', var=self.uninstall)
        uninstallCheck.pack(anchor=W)

        self.executeButton = Button(executeFrame, width=buttonWidth, text="Execute", command=lambda:self._StartWorkThread(self._Execute))
        self.executeButton.pack(anchor=W)

        # Options Frame

        clearLogCheck = Checkbutton(optionsFrame, width = checkboxWidth, text='Auto Clear Console', var=self.clearConsole)
        clearLogCheck.pack(anchor=W)

        printConfig = Checkbutton(optionsFrame, width = checkboxWidth, text='Print Config', var=self.printConfig)
        printConfig.pack(anchor=W)

        # Actions Frame

        self.makeChangeLogButton = Button(actionsFrame, width=buttonWidth, text="Make Change Log", command=lambda:self._StartWorkThread(self._MakeChangeLog))
        self.makeChangeLogButton.pack(anchor=W)

        self.cleanButton = Button(actionsFrame, width=buttonWidth, text="Clean", command=lambda:self._StartWorkThread(self._Clean))
        self.cleanButton.pack(anchor=W)

        self.buildButton = Button(actionsFrame, width=buttonWidth, text="Build", command=lambda:self._StartWorkThread(self._Build))
        self.buildButton.pack(anchor=W)

        self.releaseButton = Button(actionsFrame, width=buttonWidth, text="Build Release", command=lambda:self._StartWorkThread(self._Release))
        self.releaseButton.pack(anchor=W)

        self.installButton = Button(actionsFrame, width=buttonWidth, text="Install", command=lambda:self._StartWorkThread(self._Install))
        self.installButton.pack(anchor=W)

        self.runButton = Button(actionsFrame, width=buttonWidth, text="Run Game", command=lambda:self._StartWorkThread(self._RunGame))
        self.runButton.pack(anchor=W)

        self.uninstallButton = Button(actionsFrame, width=buttonWidth, text="Uninstall", command=lambda:self._StartWorkThread(self._Uninstall))
        self.uninstallButton.pack(anchor=W)

        self.abortButton = Button(actionsFrame, width=buttonWidth, text="Abort", command=lambda:self._Abort())
        self.abortButton.pack(anchor=W)

        # Bundle Pack Frame

        self.bundlePackList = Listbox(bundlePackFrame, width=listboxWidth, relief='flat', selectmode='multiple')
        self.bundlePackList.pack(anchor=W)

        self.bundlePackRefreshButton = Button(bundlePackFrame, width=buttonWidth, text="Refresh", command=lambda:self._StartWorkThread(self._PopulateBundlePackList))
        self.bundlePackRefreshButton.pack(anchor=W)


    def _ClearMainWindowElements(self) -> None:
        self.makeChangeLog = None
        self.clean = None
        self.build = None
        self.release = None
        self.install = None
        self.uninstall = None
        self.run = None
        self.printConfig = None
        self.clearConsole = None
        self.bundlePackList = None
        self.executeButton = None
        self.makeChangeLogButton = None
        self.cleanButton = None
        self.buildButton = None
        self.releaseButton = None
        self.installButton = None
        self.runButton = None
        self.uninstallButton = None
        self.abortButton = None
        self.bundlePackRefreshButton = None


    @staticmethod
    def _GetBundlePackNamesFromList(bundlePackList: Listbox) -> list[str]:
        bundlePackNames = list()
        selections: tuple = bundlePackList.curselection()
        selection: int
        for selection in selections:
            name: str = bundlePackList.get(selection)
            bundlePackNames.append(name)
        return bundlePackNames


    @staticmethod
    def _GetBundlePackNamesFromConfig(configPaths: list[str]) -> list[str]:
        bundlePackNames = list()
        jsonFiles: list[JsonFile] = CreateJsonFiles(configPaths)
        bundles = Bundles()
        AddBundlePacksFromJsons(jsonFiles, bundles)
        bundlePack: BundlePack
        for bundlePack in bundles.packs:
            bundlePackNames.append(bundlePack.name)
        return bundlePackNames


    def _PopulateBundlePackList(self) -> None:
        with self.mainWindowLock:
            self._SetJobElementsState("disabled")

        bundlePackNames: list[str] = Gui._GetBundlePackNamesFromConfig(self.configPaths)
        self.bundlePackList.delete(0, self.bundlePackList.size())
        self.bundlePackList.insert(0, *bundlePackNames)
        name1: str
        name2: str
        for name1 in self.buildAndInstallList:
            for index,name2 in enumerate(bundlePackNames):
                if name1 == name2:
                    self.bundlePackList.selection_set(index)

        with self.mainWindowLock:
            self._SetJobElementsState("normal")


    @staticmethod
    def _ClearConsole() -> None:
        os.system('cls||clear')


    def _Execute(self) -> None:
        function = lambda:RunWithConfig(
            configPaths=self.configPaths,
            installList=self.buildAndInstallList,
            buildList=self.buildAndInstallList,
            makeChangeLog=self.makeChangeLog.get(),
            clean=self.clean.get(),
            build=self.build.get(),
            release=self.release.get(),
            install=self.install.get(),
            uninstall=self.uninstall.get(),
            run=self.run.get(),
            printConfig=self.printConfig.get(),
            toolsRootDir=self.toolsRootDir,
            engine=self.buildEngine)

        self._DoWork(function)


    def _MakeChangeLog(self) -> None:
        function = lambda:RunWithConfig(
            configPaths=self.configPaths,
            makeChangeLog=True,
            printConfig=self.printConfig.get())

        self._DoWork(function)


    def _Clean(self) -> None:
        function = lambda:RunWithConfig(
            configPaths=self.configPaths,
            installList=self.buildAndInstallList,
            buildList=self.buildAndInstallList,
            clean=True,
            printConfig=self.printConfig.get(),
            toolsRootDir=self.toolsRootDir,
            engine=self.buildEngine)

        self._DoWork(function)


    def _Build(self) -> None:
        function = lambda:RunWithConfig(
            configPaths=self.configPaths,
            installList=self.buildAndInstallList,
            buildList=self.buildAndInstallList,
            build=True,
            printConfig=self.printConfig.get(),
            toolsRootDir=self.toolsRootDir,
            engine=self.buildEngine)

        self._DoWork(function)


    def _Release(self) -> None:
        function = lambda:RunWithConfig(
            configPaths=self.configPaths,
            installList=self.buildAndInstallList,
            buildList=self.buildAndInstallList,
            release=True,
            printConfig=self.printConfig.get(),
            toolsRootDir=self.toolsRootDir,
            engine=self.buildEngine)

        self._DoWork(function)


    def _Install(self) -> None:
        function = lambda:RunWithConfig(
            configPaths=self.configPaths,
            installList=self.buildAndInstallList,
            buildList=self.buildAndInstallList,
            install=True,
            printConfig=self.printConfig.get(),
            toolsRootDir=self.toolsRootDir,
            engine=self.buildEngine)

        self._DoWork(function)


    def _Uninstall(self) -> None:
        function = lambda:RunWithConfig(
            configPaths=self.configPaths,
            installList=self.buildAndInstallList,
            buildList=self.buildAndInstallList,
            uninstall=True,
            printConfig=self.printConfig.get(),
            toolsRootDir=self.toolsRootDir,
            engine=self.buildEngine)

        self._DoWork(function)


    def _RunGame(self) -> None:
        function = lambda:RunWithConfig(
            configPaths=self.configPaths,
            installList=self.buildAndInstallList,
            buildList=self.buildAndInstallList,
            run=True,
            printConfig=self.printConfig.get(),
            toolsRootDir=self.toolsRootDir,
            engine=self.buildEngine)

        self._DoWork(function)


    def _DoWork(self, function: Callable) -> None:
        self._OnWorkBegin()

        if self.debug:
            function()
        else:
            try:
                function()
            except Exception:
                print("ERROR CALLSTACK")
                traceback.print_exc()

        self._OnWorkEnd()


    def _OnWorkBegin(self) -> None:
        with self.buildEngineLock:
            self.buildEngine = BuildEngine()
            self.buildAndInstallList = Gui._GetBundlePackNamesFromList(self.bundlePackList)

        if self.clearConsole.get():
            Gui._ClearConsole()

        with self.mainWindowLock:
            self._SetJobElementsState("disabled")

        self._StartAbortThread()


    def _OnWorkEnd(self) -> None:
        with self.buildEngineLock:
            self.buildEngine = None

        self.abortThread.join()
        self.abortThread = None

        with self.mainWindowLock:
            self._SetJobElementsState("normal")


    def _SetJobElementsState(self, state: str) -> None:
        if self.executeButton != None:
            self.executeButton["state"] = state
            self.makeChangeLogButton["state"] = state
            self.cleanButton["state"] = state
            self.buildButton["state"] = state
            self.releaseButton["state"] = state
            self.installButton["state"] = state
            self.runButton["state"] = state
            self.uninstallButton["state"] = state
            self.bundlePackRefreshButton["state"] = state


    def _SetAbortElementsState(self, state: str) -> None:
        if self.abortButton != None:
            self.abortButton["state"] = state


    def _StartWorkThread(self, func: Callable) -> None:
        self.workThread = threading.Thread(target=func)
        self.workThread.start()


    def _StartAbortThread(self) -> None:
        self.abortThread = threading.Thread(target=self._AbortUpdateLoop)
        self.abortThread.start()


    def _AbortUpdateLoop(self) -> None:
        canAbort: bool = False
        wasAbort: bool = canAbort
        while True:
            with self.buildEngineLock:
                if self.buildEngine == None:
                    with self.mainWindowLock:
                        self._SetAbortElementsState("disabled")
                    break
                canAbort = self.buildEngine.CanAbort()
                if canAbort != wasAbort:
                    if canAbort:
                        with self.mainWindowLock:
                            self._SetAbortElementsState("enabled")
                    else:
                        with self.mainWindowLock:
                            self._SetAbortElementsState("disabled")
                wasAbort = canAbort

            time.sleep(0.1)

        return


    def _Abort(self) -> None:
        with self.buildEngineLock:
            self.buildEngine.Abort()
