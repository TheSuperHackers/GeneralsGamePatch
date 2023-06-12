from enum import Flag, auto
from dataclasses import dataclass
from generalsmodbuilder.data.bundles import Bundles
from generalsmodbuilder.data.folders import Folders
from generalsmodbuilder.data.runner import Runner
from generalsmodbuilder.data.tools import Tool, ToolsT
from generalsmodbuilder import util


class BuildStep(Flag):
    Zero = 0
    PreBuild = auto()
    Clean = auto()
    Build = auto()
    PostBuild = auto()
    Release = auto()
    Install = auto()
    Run = auto()
    Uninstall = auto()


@dataclass
class BuildSetup:
    step: BuildStep
    folders: Folders
    runner: Runner
    bundles: Bundles
    tools: ToolsT
    printConfig: bool

    def VerifyTypes(self) -> None:
        util.VerifyType(self.step, BuildStep, "BuildSetup.step")
        util.VerifyType(self.folders, Folders, "BuildSetup.folders")
        util.VerifyType(self.runner, Runner, "BuildSetup.runner")
        util.VerifyType(self.bundles, Bundles, "BuildSetup.bundles")
        util.VerifyType(self.tools, dict, "BuildSetup.tools")
        util.VerifyType(self.printConfig, bool, "BuildSetup.printConfig")
        for key, value in self.tools.items():
            util.VerifyType(key, str, "BuildSetup.tools.key")
            util.VerifyType(value, Tool, "BuildSetup.tools.value")

    def VerifyValues(self) -> None:
        util.Verify(self.tools.get("crunch") != None, "BuildSetup.tools is missing a definition for 'crunch'")
        util.Verify(self.tools.get("gametextcompiler") != None, "BuildSetup.tools is missing a definition for 'gametextcompiler'")
        util.Verify(self.tools.get("generalsbigcreator") != None, "BuildSetup.tools is missing a definition for 'generalsbigcreator'")
