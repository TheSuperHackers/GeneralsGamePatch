from ._common import ModuleTemplate, ParameterTemplate


class CrateData(ModuleTemplate):
    CreationChance = ParameterTemplate(dtype=float)
    KilledByType = ParameterTemplate()
    KillerScience = ParameterTemplate()
    CrateObject = ParameterTemplate(validator=lambda x: float(x[1]))
    VeterancyLevel = ParameterTemplate()
    OwnedByMaker = ParameterTemplate()
