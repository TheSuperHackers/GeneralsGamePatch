import os
import traceback
from argparse import ArgumentParser
from generalsmodbuilder.__version__ import VERSIONSTR
from generalsmodbuilder.buildfunctions import RunWithConfig, BuildFileHashRegistry
from generalsmodbuilder.gui.gui import Gui
from generalsmodbuilder import util


def Main(args=None):
    print(f"Generals Mod Builder v{VERSIONSTR} by The Super Hackers")

    parser = ArgumentParser()
    parser.add_argument('-c', '--config', type=str, action="append", help='Path to a configuration file (json). Multiples can be specified.')
    parser.add_argument('-l', '--config-list', type=str, nargs="*", help='Paths to any amount of configuration files (json).')
    parser.add_argument('-a', '--clean', action='store_true')
    parser.add_argument('-b', '--build', action='store_true')
    parser.add_argument(      '--build-pack', type=str, nargs="?", const="_default_", action='append', help='If specified, then only builds the bundle pack by name. Multiples can be specified.')
    parser.add_argument(      '--build-pack-list', type=str, nargs="*", help='If specified, then only builds the bundle packs by name.')
    parser.add_argument('-z', '--release', action='store_true')
    parser.add_argument('-i', '--install', type=str, nargs="?", const="_default_", action='append', help='Installs the specified bundle pack by name. Multiples can be specified.')
    parser.add_argument('-o', '--install-list', type=str, nargs="*", help='Installs the specified bundle packs by name.')
    parser.add_argument('-u', '--uninstall', action='store_true')
    parser.add_argument('-r', '--run', action='store_true')
    parser.add_argument('-g', '--gui', action='store_true')
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--print-config', action='store_true')
    parser.add_argument('--tools-root-dir', type=str, default=None, help='The root directory of tools. By default the directory of the tools json file is used as the root directory for its specified tools.')
    parser.add_argument('--file-hash-registry-input', type=str, action="append", help='Path to generate file hash registry from. Multiples can be specified.')
    parser.add_argument('--file-hash-registry-output', type=str, help='Path to save file hash registry to.')
    parser.add_argument('--file-hash-registry-name', type=str, default="FileHashRegistry", help='Name of the file hash registry.')
    parser.add_argument('--load-default-runner', action='store_true', help='Loads the built-in runner json configuration. Is loaded before custom configurations from --config and --config-list.')
    parser.add_argument('--load-default-tools', action='store_true', help='Loads the built-in tools json configuration. Is loaded before custom configurations from --config and --config-list.')
    parser.add_argument('--make-change-log', action='store_true', help='Generates change log(s) according to the given change log json setup')

    args, unknownargs = parser.parse_known_args(args=args)

    if args.file_hash_registry_input and args.file_hash_registry_output:
        BuildFileHashRegistry(
            args.file_hash_registry_input,
            args.file_hash_registry_output,
            args.file_hash_registry_name)
        return

    # Populate install pack name list.
    installList = list[str]()
    if args.install_list:
        installList.extend(args.install_list)
    if args.install:
        installList.extend(args.install)

    # Populate build pack name list.
    buildList = list[str]()
    if args.build_pack_list:
        buildList.extend(args.build_pack_list)
    if args.build_pack:
        buildList.extend(args.build_pack)

    # Set main tool commands.
    clean = bool(args.clean)
    build = bool(args.build) or bool(buildList)
    release = bool(args.release)
    install = bool(installList)
    uninstall = bool(args.uninstall)
    run = bool(args.run)
    makeChangeLog = bool(args.make_change_log)

    # Check if any work needs to be done.
    if (not build and
        not release and
        not install and
        not uninstall and
        not run and
        not makeChangeLog):
        parser.print_help()
        return

    util.pprint(args)

    configPaths = list[str]()

    # Add default configurations first to list so readers can parse them first.
    if args.load_default_runner:
        configPaths.append(os.path.join(util.g_appDir, "config", "DefaultRunner.json"))
    if args.load_default_tools:
        configPaths.append(os.path.join(util.g_appDir, "config", "DefaultTools.json"))

    # Add custom configurations last so readers can write over default configurations last.
    if args.config_list:
        configPaths.extend(args.config_list)
    if args.config:
        configPaths.extend(args.config)

    for i, path in enumerate(configPaths):
        configPaths[i] = os.path.abspath(path)

    useGui = bool(args.gui)
    debug = bool(args.debug)
    printConfig = bool(args.print_config)
    toolsRootDir = args.tools_root_dir

    if toolsRootDir:
        toolsRootDir = os.path.normpath(toolsRootDir)

    if useGui:
        gui: Gui = Gui()
        gui.RunWithConfig(
            configPaths=configPaths,
            installList=installList,
            buildList=buildList,
            makeChangeLog=makeChangeLog,
            clean=clean,
            build=build,
            release=release,
            install=install,
            uninstall=uninstall,
            run=run,
            debug=debug,
            printConfig=printConfig,
            toolsRootDir=toolsRootDir)
    else:
        def RunWithConfigWrapper():
            RunWithConfig(
                configPaths=configPaths,
                installList=installList,
                buildList=buildList,
                makeChangeLog=makeChangeLog,
                clean=clean,
                build=build,
                release=release,
                install=install,
                uninstall=uninstall,
                run=run,
                printConfig=printConfig,
                toolsRootDir=toolsRootDir)
        if debug:
            RunWithConfigWrapper()
        else:
            try:
                RunWithConfigWrapper()
            except Exception:
                print("ERROR CALLSTACK")
                traceback.print_exc()
                input("Press any key to continue...")


if __name__ == "__main__":
    Main()
