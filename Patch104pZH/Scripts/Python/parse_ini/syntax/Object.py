from ._common import Module, ModuleTemplate, ParameterTemplate
from .Object_Behavior import Behavior
from .Object_Body import Body
from .Object_ClientUpdate import ClientUpdate
from .Object_Draw import Draw


def convert_real_allow_bugged(value):
    try:
        return float(value[0])
    except ValueError:
        return 0


class ObjectSubmoduleTemplate(ModuleTemplate):
    def __new__(cls, values):
        module_name, module_tag = values
        data = cls._data.copy()
        data["token"] = module_tag
        del data["module"]
        module = getattr(Object, module_name)
        return module(template=module, values=values, **data)


class ObjectModule(Module):
    def parse(self, context, tokens):
        super().parse(context, tokens)


class Object(ModuleTemplate, module=ObjectModule):
    ###########################################################################
    # Art ParameterTemplates
    SelectPortrait = ParameterTemplate(dtype=str)
    ButtonImage = ParameterTemplate(dtype=str)

    UpgradeCameo1 = ParameterTemplate(dtype=str)
    UpgradeCameo2 = ParameterTemplate(dtype=str)
    UpgradeCameo3 = ParameterTemplate(dtype=str)
    UpgradeCameo4 = ParameterTemplate(dtype=str)
    UpgradeCameo5 = ParameterTemplate(dtype=str)

    Draw = Draw()
    PlacementViewAngle = ParameterTemplate(dtype=int)

    # Design Parameters
    Buildable = ParameterTemplate(dtype=bool)
    Side = ParameterTemplate(dtype=str)

    class WeaponSet(ModuleTemplate, allow_duplicates=True):
        Conditions = ParameterTemplate(dtype=list)
        Weapon = ParameterTemplate(dtype=list, allow_duplicates=True)
        PreferredAgainst = ParameterTemplate(dtype=list, allow_duplicates=True)
        AutoChooseSources = ParameterTemplate(dtype=list, allow_duplicates=True)
        WeaponLockSharedAcrossSets = ParameterTemplate(dtype=bool)
        ShareWeaponReloadTime = ParameterTemplate(dtype=bool)

    class ArmorSet(ModuleTemplate, allow_duplicates=True):
        Conditions = ParameterTemplate(dtype=list)
        Armor = ParameterTemplate(dtype=str)
        DamageFX = ParameterTemplate(dtype=str)

    VisionRange = ParameterTemplate(dtype=float)
    ShroudClearingRange = ParameterTemplate(dtype=float)
    ShroudRevealToAllRange = ParameterTemplate(dtype=float)
    BuildCost = ParameterTemplate(dtype=int)
    BuildTime = ParameterTemplate(dtype=float)
    RefundValue = ParameterTemplate(dtype=int)
    EnergyProduction = ParameterTemplate(dtype=int)
    EnergyBonus = ParameterTemplate(dtype=int)
    IsForbidden = ParameterTemplate(dtype=bool)
    IsBridge = ParameterTemplate(dtype=bool)
    IsPrerequisite = ParameterTemplate(dtype=bool)

    class Prerequisites(ModuleTemplate):
        Object = ParameterTemplate(dtype=list, allow_duplicates=True)
        Science = ParameterTemplate(dtype=str, allow_duplicates=True)

    def _four_ints(values):
        # assert len(values) == 4
        return list(map(int, values))

    IsTrainable = ParameterTemplate(dtype=bool)
    ExperienceRequired = ParameterTemplate(converter=_four_ints)
    ExperienceValue = ParameterTemplate(converter=_four_ints, allow_clobber=True)

    CrusherLevel = ParameterTemplate(dtype=int)
    CrushableLevel = ParameterTemplate(dtype=int)

    CommandSet = ParameterTemplate(dtype=str, allow_clobber=True)  # @todo, civ
    MaxSimultaneousOfType = ParameterTemplate(dtype=str)
    MaxSimultaneousLinkKey = ParameterTemplate(dtype=str)

    # Audio Parameters
    VoiceCreated = ParameterTemplate(dtype=str)
    VoiceSelect = ParameterTemplate(dtype=str)
    VoiceSelectElite = ParameterTemplate(dtype=str)
    VoiceGroupSelect = ParameterTemplate(dtype=str)
    VoiceMove = ParameterTemplate(dtype=str)
    VoiceGuard = ParameterTemplate(dtype=str)
    VoiceGarrison = ParameterTemplate(dtype=str)
    VoiceAttack = ParameterTemplate(dtype=str)
    VoiceAttackAir = ParameterTemplate(dtype=str)
    VoiceEnter = ParameterTemplate(dtype=str)
    VoiceFear = ParameterTemplate(dtype=str)
    VoiceTaskUnable = ParameterTemplate(dtype=str)
    VoiceTaskComplete = ParameterTemplate(dtype=str)
    VoiceMeetEnemy = ParameterTemplate(dtype=str)

    SoundCreated = ParameterTemplate(dtype=str)
    SoundOnDamaged = ParameterTemplate(dtype=str)
    SoundOnReallyDamaged = ParameterTemplate(dtype=str)
    SoundMoveStart = ParameterTemplate(dtype=str)
    SoundMoveStartDamaged = ParameterTemplate(dtype=str)
    SoundMoveLoop = ParameterTemplate(dtype=str)
    SoundAmbient = ParameterTemplate(dtype=str, allow_duplicates=True)  # @todo, test this
    SoundAmbientDamaged = ParameterTemplate(dtype=str, allow_duplicates=True)
    SoundAmbientReallyDamaged = ParameterTemplate(dtype=str, allow_duplicates=True)
    SoundAmbientRubble = ParameterTemplate(dtype=str, allow_duplicates=True)
    SoundEnter = ParameterTemplate(dtype=str)
    SoundExit = ParameterTemplate(dtype=str)
    SoundStealthOn = ParameterTemplate(dtype=str)
    SoundStealthOff = ParameterTemplate(dtype=str)
    SoundFallingFromPlane = ParameterTemplate(dtype=str)

    class UnitSpecificSounds(ModuleTemplate, allow_duplicates=True):  # @todo, rm AFG.ini bug
        VoiceCreate = ParameterTemplate(dtype=str)
        VoiceMoveUpgraded = ParameterTemplate(dtype=str)
        VoiceNoBuild = ParameterTemplate(dtype=str)
        VoiceBuildResponse = ParameterTemplate(dtype=str)
        VoiceRepair = ParameterTemplate(dtype=str)
        VoiceDisarm = ParameterTemplate(dtype=str)
        VoiceMelee = ParameterTemplate(dtype=str)
        VoiceSubdue = ParameterTemplate(dtype=str)
        VoiceClearBuilding = ParameterTemplate(dtype=str)
        VoiceSnipePilot = ParameterTemplate(dtype=str)
        VoiceFireRocketPods = ParameterTemplate(dtype=str)
        VoiceFlameLocation = ParameterTemplate(dtype=str)
        VoicePoisonLocation = ParameterTemplate(dtype=str)
        VoiceBombard = ParameterTemplate(dtype=str)
        VoicePrimaryWeaponMode = ParameterTemplate(dtype=str)
        VoiceSecondaryWeaponMode = ParameterTemplate(dtype=str)
        VoiceRapidFire = ParameterTemplate(dtype=str)
        VoiceLowFuel = ParameterTemplate(dtype=str)
        VoiceSupply = ParameterTemplate(dtype=str)
        VoiceCombatDrop = ParameterTemplate(dtype=str)
        VoiceStealCashComplete = ParameterTemplate(dtype=str)
        VoiceDisableVehicleComplete = ParameterTemplate(dtype=str)
        VoiceCaptureBuildingComplete = ParameterTemplate(dtype=str)
        VoiceHackInternet = ParameterTemplate(dtype=str)
        VoiceSalvage = ParameterTemplate(dtype=str)
        VoiceCrush = ParameterTemplate(dtype=str)
        VoiceGetHealed = ParameterTemplate(dtype=str)
        VoiceGarrison = ParameterTemplate(dtype=str)
        VoiceEnter = ParameterTemplate(dtype=str)
        VoiceEnterHostile = ParameterTemplate(dtype=str)
        VoiceUnload = ParameterTemplate(dtype=str)
        VoiceEject = ParameterTemplate(dtype=str)
        SoundEject = ParameterTemplate(dtype=str)
        SoundMoveStart = ParameterTemplate(dtype=str)
        SoundMoveStartDamaged = ParameterTemplate(dtype=str)

        WeaponUpgradeSound = ParameterTemplate(dtype=str)
        TurretMoveStart = ParameterTemplate(dtype=str)
        TurretMoveLoop = ParameterTemplate(dtype=str)
        TruckPowerslideSound = ParameterTemplate(dtype=str)
        TruckLandingSound = ParameterTemplate(dtype=str)
        Afterburner = ParameterTemplate(dtype=str)
        HowitzerFire = ParameterTemplate(dtype=str)
        StartDive = ParameterTemplate(dtype=str)
        DisguiseStarted = ParameterTemplate(dtype=str)
        DisguiseRevealedSuccess = ParameterTemplate(dtype=str)
        DisguiseRevealedFailure = ParameterTemplate(dtype=str)
        Deploy = ParameterTemplate(dtype=str)
        Undeploy = ParameterTemplate(dtype=str)
        UnitPack = ParameterTemplate(dtype=str)
        UnitUnpack = ParameterTemplate(dtype=str)
        UnitCashPing = ParameterTemplate(dtype=str)
        UnitBombPing = ParameterTemplate(dtype=str)
        UnderConstruction = ParameterTemplate(dtype=str)
        StickyBombCreated = ParameterTemplate(dtype=str)

    class UnitSpecificFX(ModuleTemplate):
        CombatDropKillFX = ParameterTemplate(dtype=str)

    ###########################################################################
    # Engineering ParameterTemplates
    RadarPriority = ParameterTemplate(dtype=str)
    DisplayColor = ParameterTemplate(dtype=list)  # R:100 G:100 B:100
    EnterGuard = ParameterTemplate(dtype=bool)
    HijackGuard = ParameterTemplate(dtype=bool)

    Locomotor = ParameterTemplate(dtype=list, allow_duplicates=True)

    EditorSorting = ParameterTemplate()
    KindOf = ParameterTemplate(dtype=list)
    DisplayName = ParameterTemplate(dtype=str, converter=lambda value: value[0])  # @todo, str OBJECT:DogwoodTree OPTIMIZED_TREE
    TransportSlotCount = ParameterTemplate(dtype=int)
    BuildVariations = ParameterTemplate(dtype=list)

    Body = Body()
    Behavior = Behavior()
    ClientUpdate = ClientUpdate()

    FenceWidth = ParameterTemplate(dtype=float)
    FenceXOffset = ParameterTemplate(dtype=float)

    Scale = ParameterTemplate(dtype=float)
    InstanceScaleFuzziness = ParameterTemplate(dtype=float)
    Geometry = ParameterTemplate(dtype=str)
    GeometryMajorRadius = ParameterTemplate(dtype=float, converter=convert_real_allow_bugged)  # @todo float SandbagWallEnd 18.5.0
    GeometryMinorRadius = ParameterTemplate(dtype=float)
    GeometryHeight = ParameterTemplate(dtype=float, converter=convert_real_allow_bugged)  # @todo float MogadishuHouse10 40v.0
    GeometryIsSmall = ParameterTemplate(dtype=bool)

    FactoryExitWidth = ParameterTemplate(dtype=str)
    FactoryExtraBibWidth = ParameterTemplate(dtype=str)

    Shadow = ParameterTemplate(dtype=str)
    ShadowSizeX = ParameterTemplate(dtype=int)
    ShadowSizeY = ParameterTemplate(dtype=int)
    ShadowTexture = ParameterTemplate(dtype=str)

    BuildCompletion = ParameterTemplate(dtype=str)


# hack
class InheritableModule(Object):
    pass


Object.InheritableModule = InheritableModule


class OverrideableByLikeKind(Object):
    pass


Object.OverrideableByLikeKind = OverrideableByLikeKind
