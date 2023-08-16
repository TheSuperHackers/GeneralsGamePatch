from ._common import ModuleTemplate, ParameterTemplate


class CommandButton(ModuleTemplate):
    Command = ParameterTemplate(dtype=str)
    WeaponSlot = ParameterTemplate(dtype=str)
    MaxShotsToFire = ParameterTemplate(dtype=int)
    SpecialPower = ParameterTemplate(dtype=str)
    Object = ParameterTemplate(dtype=str)
    Upgrade = ParameterTemplate(dtype=str)
    Science = ParameterTemplate(dtype=list)
    Options = ParameterTemplate(dtype=list)
    CursorName = ParameterTemplate(dtype=str)
    InvalidCursorName = ParameterTemplate(dtype=str)
    TextLabel = ParameterTemplate(dtype=str)
    ButtonImage = ParameterTemplate(dtype=str)
    ButtonBorderType = ParameterTemplate(dtype=str)
    DescriptLabel = ParameterTemplate(dtype=str)
    RadiusCursorType = ParameterTemplate(dtype=str)
    ConflictingLabel = ParameterTemplate(dtype=str)
    UnitSpecificSound = ParameterTemplate(dtype=str)
