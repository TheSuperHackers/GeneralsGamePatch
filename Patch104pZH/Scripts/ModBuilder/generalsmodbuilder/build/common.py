from re import search, Match
from generalsmodbuilder.data.common import ParamT, ParamsT


def ParamsToArgs(params: ParamsT, includeRegex: str = None, excludeRegex: str = None) -> list[str]:
    args = list()

    for key, value in params.items():

        if includeRegex:
            reKey: Match = search(includeRegex, key)
            if reKey == None:
                continue

        if excludeRegex:
            reKey: Match = search(includeRegex, key)
            if reKey != None:
                continue

        __AppendParamToArgs(args, key)

        if isinstance(value, list):
            for subValue in value:
                __AppendParamToArgs(args, subValue)
        else:
            __AppendParamToArgs(args, value)

    return args


def __AppendParamToArgs(args: list[str], val: ParamT) -> None:
    if strVal := str(val):
        args.append(strVal)
