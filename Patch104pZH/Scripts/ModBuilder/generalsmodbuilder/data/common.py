from typing import Union
from generalsmodbuilder import util


ParamT = Union[str, int, float, bool, list]
ParamsT = dict[str, Union[str, int, float, bool, list[ParamT]]]


def VerifyParamsType(params: ParamsT, name: str) -> None:
    for key,value in params.items():
        util.VerifyType(key, str, f"{name}.key")
        util.VerifyType(value, (str, int, float, bool, list), f"{name}.value")

        if isinstance(value, list):
            for subValue in value:
                util.VerifyType(subValue, (str, int, float, bool, list), f"{name}.value.value")


def VerifyStringListType(strlist: list[str], name: str) -> None:
    util.VerifyType(strlist, list, name)
    for value in strlist:
        util.VerifyType(value, str, f"{name}.value")
