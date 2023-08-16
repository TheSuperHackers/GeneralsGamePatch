from ._common import ModuleTemplate, ParameterTemplate, SubmoduleTemplate


class Body(SubmoduleTemplate):
    class InactiveBody(ModuleTemplate):
        pass

    class ActiveBody(ModuleTemplate):
        MaxHealth = ParameterTemplate(dtype=float)
        InitialHealth = ParameterTemplate(dtype=float)

        SubdualDamageCap = ParameterTemplate(dtype=int)
        SubdualDamageHealRate = ParameterTemplate(dtype=int)
        SubdualDamageHealAmount = ParameterTemplate(dtype=int)

    class UndeadBody(ActiveBody):
        SecondLifeMaxHealth = ParameterTemplate(dtype=float)

    class StructureBody(ActiveBody):
        pass

    class HiveStructureBody(ActiveBody):
        PropagateDamageTypesToSlavesWhenExisting = ParameterTemplate(dtype=list)
        SwallowDamageTypesIfSlavesNotExisting = ParameterTemplate(dtype=list)

    class ImmortalBody(ActiveBody):
        pass

    class HighlanderBody(ModuleTemplate):
        MaxHealth = ParameterTemplate(dtype=float)
        InitialHealth = ParameterTemplate(dtype=float)
