import textwrap as tw
from collections import ChainMap
from collections.abc import Mapping
from functools import partial
from pprint import pprint
from types import MappingProxyType


def convert_entry(obj):
    if len(obj) == 1:
        return obj[0]
    else:
        raise TypeError(obj)


def convert_yes_no(obj):
    if obj[0].upper() == "YES":
        return True
    elif obj[0].upper() == "NO":
        return False
    else:
        raise TypeError(obj)


def validate_int(obj):
    try:
        int(obj)
    except ValueError as exc:
        exc.add_note(obj)
        return False
    return True


def validate_real(obj):
    try:
        float(obj)
    except ValueError:
        return False
    return True


def validate_yes_no(obj):
    return isinstance(obj, bool)


def validate_list(obj):
    if isinstance(obj, str):
        return True  # 1 item list, @TODO, rm this when coverter's are implemented
    return isinstance(obj, list) and all(isinstance(x, str) for x in obj)


def default_converter(value, dtype):
    if dtype is str:
        return convert_entry(value)
    elif dtype is bool:
        return convert_yes_no(value)
    elif dtype is int:
        return dtype(value[0])
    elif dtype is float:
        return dtype(value[0].removesuffix("f"))
    else:
        return value


def default_validator(value, dtype):
    if dtype is int:
        return validate_int(value)
    elif dtype is float:
        return validate_real(value)
    elif dtype is bool:
        return validate_yes_no(value)
    elif dtype is list:
        return validate_list(value)
    elif dtype is not None:
        return isinstance(value, dtype)
    else:
        return True


###############################################################################
###############################################################################
class Parameter:
    def __init__(self, token, template, value):
        self.token = token
        self.template = template
        self.value = value

    def __repr__(self):
        return f"{self.value}"

    @property
    def allow_duplicates(self):
        return self.template.allow_duplicates

    @property
    def allow_clobber(self):
        return self.template.allow_clobber

    def as_dict(self):
        return self.value


class ParameterTemplate:
    def __init__(
        self,
        token=None,
        dtype=None,
        converter=None,
        validator=None,
        allow_duplicates=False,
        allow_clobber=False,
        default_value=None,
    ):
        if converter is None:
            converter = partial(default_converter, dtype=dtype)

        if validator is None:
            validator = partial(default_validator, dtype=dtype)

        if default_value is None:
            if dtype is list:
                default_value = []

        self.token = token
        self.dtype = dtype
        self.convert = converter
        self.validate = validator
        self.allow_duplicates = allow_duplicates
        self.allow_clobber = allow_clobber
        self.default_value = default_value

    def __repr__(self):
        return f"<{type(self).__name__} {self.token}>"

    def __set_name__(self, cls, name):
        if self.token is None:
            self.token = name

    def __set__(self, obj, value):
        setattr(obj, f"_{self.token}", value)

    def __get__(self, obj, owner):
        if obj is None:
            return self
        else:
            return getattr(obj, f"_{self.token}")

    def __call__(self, context, tokens):
        name, *values = tokens
        value = self.convert(values)
        assert self.validate(value)
        token = self.token
        obj = Parameter(token=token, template=self, value=value)
        return name, obj


###############################################################################
###############################################################################
class Module(Mapping):
    def __init__(
        self,
        token,
        template,
        values,
        allow_duplicates,
        module_parameters,
        module_submodules,
    ):
        self.token = token
        self.template = template
        self.values = values
        self.allow_duplicates = allow_duplicates
        self.module_parameters = module_parameters
        self.module_submodules = module_submodules
        self.keywords = ChainMap(self.module_parameters, self.module_submodules)
        self.parameters = {}
        self.submodules = {}
        self.attributes = ChainMap(self.parameters, self.submodules)

    def __repr__(self):
        return f"<{type(self).__name__} {self.token}>"

    def __str__(self):
        result = ""

        for name, parameter in self.parameters.items():
            result += f"{name} = {parameter}\n"

        for name, module in self.submodules.items():
            result += f"{module.token} {name}\n"
            result += tw.indent(str(module), "  ")
            result += "End\n"

        return result

    def __setitem__(self, name, submodule_or_parameter):
        if isinstance(submodule_or_parameter, Module):
            if submodule_or_parameter.allow_duplicates:
                for i in range(999):
                    new_name = name + f".{i:03d}"

                    if new_name not in self.submodules:
                        break
                else:
                    raise RuntimeError(new_name)

                name = new_name
            elif name in self.submodules:
                raise ValueError(f"Duplicate module {name}")

            self.submodules[name] = submodule_or_parameter
        elif isinstance(submodule_or_parameter, Parameter):
            parameter = submodule_or_parameter

            if parameter.allow_duplicates:
                for i in range(999):
                    new_name = name + f".{i:03d}"

                    if new_name not in self.parameters:
                        break
                else:
                    raise RuntimeError(new_name)

                name = new_name
            elif name in self.parameters:
                if parameter.allow_clobber:
                    old_value = self.parameters[name].value
                    new_value = parameter.value
                    print(f"Warning: {self.token} {name} clobbered, before: {old_value}, after: {new_value}")
                else:
                    raise ValueError(f"Duplicate parameter {name}")

            self.parameters[name] = parameter
        else:
            raise KeyError(name)

    def __getitem__(self, token):
        try:
            return self.parameters[token].value
        except KeyError:
            try:
                if token in self.module_parameters:
                    return self.module_parameters[token].default_value

                return self.submodules[token]
            except KeyError:
                raise KeyError(token)

    def __iter__(self):
        yield from self.attributes

    def __len__(self):
        return len(self.attributes)

    def parse(self, context, tokens):
        keyword = tokens[0]

        if keyword in self.keywords:
            name, obj = self.keywords[keyword](context, tokens)
            self[name] = obj
        elif keyword.upper() == "END":
            context.pop()
        else:
            raise KeyError(keyword)

    def parse_module(self, tokens):
        pass

    def convert(self, value):
        return value

    def validate(self, value):
        return True

    def print(self, indent=0):
        for name, value in self.items():
            if isinstance(value, ModuleTemplate):
                print(f"{'    ' * indent}{type(value).__name__} {name}")
                value.print(indent=indent + 1)
                print(f"{'    ' * indent}End\n")
            elif isinstance(value, ParameterTemplate):
                print(f"{'    ' * indent}{name} = {value}")
            else:
                if isinstance(value, list):
                    value = " ".join(value)
                print(f"{'    ' * indent}{name} = {value}")

    def as_dict(self):
        return {k: v.as_dict() for k, v in {**self.parameters, **self.submodules}.items()}

    def pprint(self):
        pprint(self.as_dict(), sort_dicts=False)


class ModuleTemplate:
    def __init_subclass__(cls, token=None, module=Module, allow_duplicates=False, **kwargs):
        parameters = {}
        submodules = {}

        for base in cls.__mro__:
            for attr, value in vars(base).items():
                if attr.startswith("_"):
                    continue
                elif isinstance(value, ParameterTemplate):
                    parameters[value.token] = value
                elif isinstance(value, type) and issubclass(value, ModuleTemplate):
                    submodules[attr] = value
                elif isinstance(value, SubmoduleTemplate):
                    submodules[attr] = value

        if token is None:
            token = cls.__name__

        cls._data = dict(
            token=token,
            template=module,
            allow_duplicates=allow_duplicates,
            module_parameters=MappingProxyType(parameters),
            module_submodules=MappingProxyType(submodules),
        )

        super().__init_subclass__(**kwargs)

    def __new__(cls, context, tokens=["", ""]):
        try:
            token, name, *values = tokens
        except ValueError:
            name, *values = tokens

        data = cls._data.copy()
        module = data["template"]
        obj = module(values=values, **data)
        context.append(obj)
        return name, obj


class SubmoduleTemplate(ModuleTemplate):
    __new__ = object.__new__

    def __repr__(self):
        return f"<{type(self).__name__}>"

    def __call__(self, context, tokens):
        submodule_type, token, name, *trash = tokens
        tokens = token, name
        template = type(self)._data["module_submodules"][token]
        name, obj = template(context, tokens)
        return f"{submodule_type}: {token} {name}", obj
