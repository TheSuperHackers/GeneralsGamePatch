from ._common import ModuleTemplate, ParameterTemplate, SubmoduleTemplate


class Behavior(SubmoduleTemplate):
    ###########################################################################
    # Create ModuleTemplates
    class PreorderCreate(ModuleTemplate):
        pass

    class SpecialPowerCreate(ModuleTemplate):
        pass

    class VeterancyGainCreate(ModuleTemplate):
        StartingLevel = ParameterTemplate(dtype=str)
        ScienceRequired = ParameterTemplate(dtype=str)

    class LockWeaponCreate(ModuleTemplate):
        SlotToLock = ParameterTemplate(dtype=list)

    class GrantUpgradeCreate(ModuleTemplate):
        UpgradeToGrant = ParameterTemplate(dtype=str)
        ExemptStatus = ParameterTemplate(dtype=str)

    class GrantScienceUpgrade(ModuleTemplate):
        GrantScience = ParameterTemplate(dtype=str)
        TriggeredBy = ParameterTemplate(dtype=str)

    class GrantStealthBehavior(ModuleTemplate):
        StartRadius = ParameterTemplate(dtype=float)
        FinalRadius = ParameterTemplate(dtype=float)
        RadiusGrowRate = ParameterTemplate(dtype=float)
        RadiusParticleSystemName = ParameterTemplate(dtype=str)
        KindOf = ParameterTemplate(dtype=list)
        ForbiddenKindOf = ParameterTemplate(dtype=list)

    class SpawnBehavior(ModuleTemplate):
        SpawnTemplateName = ParameterTemplate(dtype=str, allow_duplicates=True)
        SpawnNumber = ParameterTemplate(dtype=str)
        SpawnReplaceDelay = ParameterTemplate(dtype=str)
        SpawnedRequireSpawner = ParameterTemplate(dtype=bool)
        OneShot = ParameterTemplate(dtype=bool)
        CanReclaimOrphans = ParameterTemplate(dtype=bool)
        AggregateHealth = ParameterTemplate(dtype=bool)
        ExitByBudding = ParameterTemplate(dtype=bool)
        InitialBurst = ParameterTemplate(dtype=str)
        SlavesHaveFreeWill = ParameterTemplate(dtype=bool)

    class SupplyCenterCreate(ModuleTemplate):
        pass

    class SupplyWarehouseCreate(ModuleTemplate):
        pass

    ###########################################################################
    # Update ModuleTemplates
    class HordeUpdate(ModuleTemplate):
        UpdateRate = ParameterTemplate(dtype=int)
        RubOffRadius = ParameterTemplate(dtype=int)
        AlliesOnly = ParameterTemplate(dtype=bool)
        ExactMatch = ParameterTemplate(dtype=bool)
        Action = ParameterTemplate(dtype=str)
        Radius = ParameterTemplate(dtype=int)
        KindOf = ParameterTemplate(dtype=list)
        Count = ParameterTemplate(dtype=int)
        AllowedNationalism = ParameterTemplate(dtype=str)
        FlagSubObjectNames = ParameterTemplate(dtype=str)

    class SupplyCenterDockUpdate(ModuleTemplate):
        NumberApproachPositions = ParameterTemplate(dtype=int)
        AllowsPassthrough = ParameterTemplate(dtype=bool)
        GrantTemporaryStealth = ParameterTemplate(dtype=int)

    class SupplyWarehouseDockUpdate(ModuleTemplate):
        NumberApproachPositions = ParameterTemplate(dtype=int)
        AllowsPassthrough = ParameterTemplate(dtype=bool)
        StartingBoxes = ParameterTemplate(dtype=int)
        DeleteWhenEmpty = ParameterTemplate(dtype=bool)

    class RepairDockUpdate(ModuleTemplate):
        NumberApproachPositions = ParameterTemplate(dtype=int)
        AllowsPassthrough = ParameterTemplate(dtype=bool)
        TimeForFullHeal = ParameterTemplate(dtype=int)

    class RailedTransportDockUpdate(ModuleTemplate):
        NumberApproachPositions = ParameterTemplate(dtype=int)
        PullInsideDuration = ParameterTemplate(dtype=int)
        PushOutsideDuration = ParameterTemplate(dtype=int)
        ToleranceDistance = ParameterTemplate(dtype=float)

    class AssistedTargetingUpdate(ModuleTemplate):
        AssistingClipSize = ParameterTemplate(dtype=int)
        AssistingWeaponSlot = ParameterTemplate(dtype=str)
        LaserFromAssisted = ParameterTemplate(dtype=str)
        LaserToTarget = ParameterTemplate(dtype=str)

    ###########################################################################
    # Fire Weapon ModuleTemplates
    class FireWeaponUpdate(ModuleTemplate):
        Weapon = ParameterTemplate(dtype=str)
        ExclusiveWeaponDelay = ParameterTemplate(dtype=int)
        InitialDelay = ParameterTemplate(dtype=int)

    class FireOCLAfterWeaponCooldownUpdate(ModuleTemplate):
        WeaponSlot = ParameterTemplate(dtype=list)
        TriggeredBy = ParameterTemplate(dtype=list)
        ConflictsWith = ParameterTemplate(dtype=list)

        OCL = ParameterTemplate(dtype=list)
        MinShotsToCreateOCL = ParameterTemplate(dtype=int)
        OCLLifetimePerSecond = ParameterTemplate(dtype=int)
        OCLLifetimeMaxCap = ParameterTemplate(dtype=int)

    class FireWeaponCollide(ModuleTemplate):
        FireOnce = ParameterTemplate(dtype=bool)  # not functional
        CollideWeapon = ParameterTemplate(dtype=str)
        RequiredStatus = ParameterTemplate(dtype=str)
        ForbiddenStatus = ParameterTemplate(dtype=str)

    class FireWeaponWhenDamagedBehavior(ModuleTemplate):
        DamageTypes = ParameterTemplate(dtype=list)
        DamageAmount = ParameterTemplate(dtype=int)

        StartsActive = ParameterTemplate(dtype=bool)
        TriggeredBy = ParameterTemplate(dtype=list)
        ConflictsWith = ParameterTemplate(dtype=list)

        ReactionWeaponPristine = ParameterTemplate(dtype=str)
        ReactionWeaponDamaged = ParameterTemplate(dtype=str)
        ReactionWeaponReallyDamaged = ParameterTemplate(dtype=str)
        ReactionWeaponRubble = ParameterTemplate(dtype=str)
        ContinuousWeaponPristine = ParameterTemplate(dtype=str)
        ContinuousWeaponDamaged = ParameterTemplate(dtype=str)
        ContinuousWeaponReallyDamaged = ParameterTemplate(dtype=str)
        ContinuousWeaponRubble = ParameterTemplate(dtype=str)

    class FireWeaponPower(ModuleTemplate):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)
        MaxShotsToFire = ParameterTemplate(dtype=int)

    # Collide ModuleTemplates
    class SquishCollide(ModuleTemplate):
        pass

    class _CollideBehavior(ModuleTemplate):
        RequiredKindOf = ParameterTemplate(dtype=list)
        ForbiddenKindOf = ParameterTemplate(dtype=list)
        ForbidOwnerPlayer = ParameterTemplate(dtype=int)
        HumanOnly = ParameterTemplate(dtype=int)
        BuildingPickup = ParameterTemplate(dtype=bool)
        PickupScience = ParameterTemplate(dtype=str)

        ExecuteFX = ParameterTemplate(dtype=str)
        ExecuteAnimation = ParameterTemplate(dtype=str)
        ExecuteAnimationTime = ParameterTemplate(dtype=float)
        ExecuteAnimationZRise = ParameterTemplate(dtype=float)
        ExecuteAnimationFades = ParameterTemplate(dtype=bool)

    class MoneyCrateCollide(_CollideBehavior):
        MoneyProvided = ParameterTemplate()
        UpgradedBoost = ParameterTemplate(validator=lambda x: len(x) == 2)

    class HealCrateCollide(_CollideBehavior):
        EffectRange = ParameterTemplate(dtype=float)

    class VeterancyCrateCollide(_CollideBehavior):
        EffectRange = ParameterTemplate(dtype=float)
        AddsOwnerVeterancy = ParameterTemplate(dtype=bool)
        IsPilot = ParameterTemplate(dtype=bool)

    class UnitCrateCollide(_CollideBehavior):
        UnitCount = ParameterTemplate()
        UnitName = ParameterTemplate()

    class SalvageCrateCollide(_CollideBehavior):
        WeaponChance = ParameterTemplate()
        LevelChance = ParameterTemplate()
        MoneyChance = ParameterTemplate()
        MinMoney = ParameterTemplate()
        MaxMoney = ParameterTemplate()

    class ConvertToCarBombCrateCollide(ModuleTemplate):
        RequiredKindOf = ParameterTemplate(dtype=list)
        ForbiddenKindOf = ParameterTemplate(dtype=list)
        FXList = ParameterTemplate(dtype=list)

        ExecuteFX = ParameterTemplate(dtype=str)
        ExecuteAnimation = ParameterTemplate(dtype=str)
        ExecuteAnimationTime = ParameterTemplate(dtype=float)
        ExecuteAnimationZRise = ParameterTemplate(dtype=float)
        ExecuteAnimationFades = ParameterTemplate(dtype=bool)

    class ConvertToHijackedVehicleCrateCollide(ModuleTemplate):
        RequiredKindOf = ParameterTemplate(dtype=list)
        ForbiddenKindOf = ParameterTemplate(dtype=list)

        ExecuteFX = ParameterTemplate(dtype=str)
        ExecuteAnimation = ParameterTemplate(dtype=str)
        ExecuteAnimationTime = ParameterTemplate(dtype=float)
        ExecuteAnimationZRise = ParameterTemplate(dtype=float)
        ExecuteAnimationFades = ParameterTemplate(dtype=bool)

    class SabotagePowerPlantCrateCollide(_CollideBehavior):
        SabotagePowerDuration = ParameterTemplate(dtype=int)

    class SabotageSupplyCenterCrateCollide(_CollideBehavior):
        StealCashAmount = ParameterTemplate(dtype=int)

    class SabotageSupplyDropzoneCrateCollide(_CollideBehavior):
        StealCashAmount = ParameterTemplate(dtype=int)

    class SabotageMilitaryFactoryCrateCollide(_CollideBehavior):
        SabotageDuration = ParameterTemplate(dtype=int)

    class SabotageInternetCenterCrateCollide(_CollideBehavior):
        SabotageDuration = ParameterTemplate(dtype=int)

    class SabotageSuperweaponCrateCollide(_CollideBehavior):
        pass

    class SabotageCommandCenterCrateCollide(_CollideBehavior):
        pass

    class SabotageFakeBuildingCrateCollide(_CollideBehavior):
        pass

    class ShroudCrateCollide(_CollideBehavior):
        pass

    ###########################################################################
    # Upgrade ModuleTemplates
    class _UpgradeBehavior(ModuleTemplate):
        TriggeredBy = ParameterTemplate(dtype=list)
        ConflictsWith = ParameterTemplate(dtype=list)
        RequiresAllTriggers = ParameterTemplate(dtype=bool)
        FXListUpgrade = ParameterTemplate(dtype=str)

    class WeaponBonusUpgrade(_UpgradeBehavior):
        pass

    class WeaponSetUpgrade(_UpgradeBehavior):
        pass

    # CCG only, removed in ZH
    # class DelayedWeaponSetUpgradeUpdate(ModuleTemplate):
    #     pass

    class WeaponBonusUpdate(ModuleTemplate):
        RequiredAffectKindOf = ParameterTemplate(dtype=list)
        ForbiddenAffectKindOf = ParameterTemplate(dtype=list)
        BonusDuration = ParameterTemplate(dtype=int)
        BonusDelay = ParameterTemplate(dtype=int)
        BonusRange = ParameterTemplate(dtype=int)
        BonusConditionType = ParameterTemplate(dtype=list)

    class ArmorUpgrade(_UpgradeBehavior):
        pass

    class MaxHealthUpgrade(_UpgradeBehavior):
        AddMaxHealth = ParameterTemplate(dtype=float)
        ChangeType = ParameterTemplate(dtype=list)

    class SpyVisionUpdate(_UpgradeBehavior):
        NeedsUpgrade = ParameterTemplate(dtype=bool)
        SelfPowered = ParameterTemplate(dtype=bool)
        SelfPoweredDuration = ParameterTemplate(dtype=int)
        SelfPoweredInterval = ParameterTemplate(dtype=int)
        SpyOnKindof = ParameterTemplate(dtype=list)

    class LocomotorSetUpgrade(_UpgradeBehavior):
        pass

    class CommandSetUpgrade(_UpgradeBehavior):
        RemovesUpgrades = ParameterTemplate(dtype=list)
        CommandSet = ParameterTemplate(dtype=str)
        CommandSetAlt = ParameterTemplate(dtype=str)
        TriggerAlt = ParameterTemplate(dtype=list)

    class CountermeasuresBehavior(_UpgradeBehavior):
        FlareTemplateName = ParameterTemplate(dtype=str)
        FlareBoneBaseName = ParameterTemplate(dtype=str)
        VolleySize = ParameterTemplate(dtype=int)
        VolleyArcAngle = ParameterTemplate(dtype=float)
        VolleyVelocityFactor = ParameterTemplate(dtype=float)
        DelayBetweenVolleys = ParameterTemplate(dtype=int)
        NumberOfVolleys = ParameterTemplate(dtype=int)
        ReloadTime = ParameterTemplate(dtype=int)
        EvasionRate = ParameterTemplate(dtype=str)  # percent
        ReactionLaunchLatency = ParameterTemplate(dtype=int)
        MissileDecoyDelay = ParameterTemplate(dtype=int)
        MustReloadAtAirfield = ParameterTemplate(dtype=bool)

    class AutoHealBehavior(_UpgradeBehavior):
        StartsActive = ParameterTemplate(dtype=bool)

        HealingAmount = ParameterTemplate(dtype=int)
        HealingDelay = ParameterTemplate(dtype=int)
        StartHealingDelay = ParameterTemplate(dtype=int)
        Radius = ParameterTemplate(dtype=float)

        SingleBurst = ParameterTemplate(dtype=bool)
        AffectsWholePlayer = ParameterTemplate(dtype=bool)
        KindOf = ParameterTemplate(dtype=list)
        ForbiddenKindOf = ParameterTemplate(dtype=list)
        SkipSelfForHealing = ParameterTemplate(dtype=bool)

        RadiusParticleSystemName = ParameterTemplate(dtype=str)
        UnitHealPulseParticleSystemName = ParameterTemplate(dtype=str)

    class ModelConditionUpgrade(_UpgradeBehavior):
        ConditionFlag = ParameterTemplate(dtype=list)

    class StatusBitsUpgrade(_UpgradeBehavior):
        RemovesUpgrades = ParameterTemplate(dtype=list)
        StatusToSet = ParameterTemplate(dtype=str)
        StatusToClear = ParameterTemplate(dtype=str)

    class StealthUpgrade(_UpgradeBehavior):
        pass

    class StealthUpdate(ModuleTemplate):
        UseRiderStealth = ParameterTemplate(dtype=bool)
        StealthDelay = ParameterTemplate(dtype=int)
        MoveThresholdSpeed = ParameterTemplate(dtype=int)
        StealthForbiddenConditions = ParameterTemplate(dtype=list)
        HintDetectableConditions = ParameterTemplate(dtype=list)
        FriendlyOpacityMin = ParameterTemplate(dtype=str)  # percentage
        FriendlyOpacityMax = ParameterTemplate(dtype=str)  # percentage
        PulseFrequency = ParameterTemplate(dtype=int)
        RevealDistanceFromTarget = ParameterTemplate(dtype=float)
        OrderIdleEnemiesToAttackMeUponReveal = ParameterTemplate(dtype=bool)
        ForbiddenStatus = ParameterTemplate(dtype=list)
        RequiredStatus = ParameterTemplate(dtype=list)
        InnateStealth = ParameterTemplate(dtype=bool)

        EnemyDetectionEvaEvent = ParameterTemplate(dtype=str)
        OwnDetectionEvaEvent = ParameterTemplate(dtype=str)
        GrantedBySpecialPower = ParameterTemplate(dtype=bool)
        BlackMarketCheckDelay = ParameterTemplate(dtype=int)

        DisguisesAsTeam = ParameterTemplate(dtype=bool)
        DisguiseFX = ParameterTemplate(dtype=str)
        DisguiseRevealFX = ParameterTemplate(dtype=str)
        DisguiseTransitionTime = ParameterTemplate(dtype=int)
        DisguiseRevealTransitionTime = ParameterTemplate(dtype=int)

    class StealthDetectorUpdate(ModuleTemplate):
        DetectionRate = ParameterTemplate(dtype=int)
        DetectionRange = ParameterTemplate(dtype=int)
        CanDetectWhileGarrisoned = ParameterTemplate(dtype=bool)
        CanDetectWhileContained = ParameterTemplate(dtype=bool)
        ExtraRequiredKindOf = ParameterTemplate(dtype=str)
        ExtraForbiddenKindOf = ParameterTemplate(dtype=str)
        PingSound = ParameterTemplate(dtype=str)
        LoudPingSound = ParameterTemplate(dtype=str)
        IRParticleSysName = ParameterTemplate(dtype=str)
        IRBrightParticleSysName = ParameterTemplate(dtype=str)
        IRGridParticleSysName = ParameterTemplate(dtype=str)
        IRBeaconParticleSysName = ParameterTemplate(dtype=str)
        IRParticleSysBone = ParameterTemplate(dtype=str)
        InitiallyDisabled = ParameterTemplate(dtype=bool)

    class SubObjectsUpgrade(_UpgradeBehavior):
        ShowSubObjects = ParameterTemplate(dtype=list)
        HideSubObjects = ParameterTemplate(dtype=list)

    class UnpauseSpecialPowerUpgrade(_UpgradeBehavior):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)

    class ObjectCreationUpgrade(_UpgradeBehavior):
        UpgradeObject = ParameterTemplate(dtype=str)

    class PassengersFireUpgrade(_UpgradeBehavior):
        pass

    class PowerPlantUpgrade(_UpgradeBehavior):
        pass

    class ActiveShroudUpgrade(_UpgradeBehavior):
        NewShroudRange = ParameterTemplate(dtype=float)

    class CostModifierUpgrade(_UpgradeBehavior):
        EffectKindOf = ParameterTemplate(dtype=str)
        Percentage = ParameterTemplate(dtype=str)

    class ExperienceScalarUpgrade(_UpgradeBehavior):
        AddXPScalar = ParameterTemplate(dtype=float)

    class RadarUpgrade(_UpgradeBehavior):
        DisableProof = ParameterTemplate(dtype=bool)

    class ReplaceObjectUpgrade(_UpgradeBehavior):
        ReplaceObject = ParameterTemplate(dtype=str)

    class DelayedUpgrade(_UpgradeBehavior):
        DelayTime = ParameterTemplate(dtype=int)

    class FireWeaponWhenDeadBehavior(_UpgradeBehavior):
        StartsActive = ParameterTemplate(dtype=bool)
        DeathTypes = ParameterTemplate(dtype=list)
        RequiredStatus = ParameterTemplate(dtype=str)
        ExemptStatus = ParameterTemplate(dtype=str)
        DeathWeapon = ParameterTemplate(dtype=str)

    ###########################################################################
    # Special Power ModuleTemplates
    class SpecialPowerCompletionDie(ModuleTemplate):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)

    class SpecialAbility(ModuleTemplate):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)
        UpdateModuleStartsAttack = ParameterTemplate(dtype=bool)
        InitiateSound = ParameterTemplate(dtype=str)
        StartsPaused = ParameterTemplate(dtype=bool)

    class SpecialAbilityUpdate(ModuleTemplate):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)
        StartAbilityRange = ParameterTemplate(dtype=float)
        AbilityAbortRange = ParameterTemplate(dtype=float)
        PreparationTime = ParameterTemplate(dtype=int)
        PreTriggerUnstealthTime = ParameterTemplate(dtype=int)
        SkipPackingWithNoTarget = ParameterTemplate(dtype=bool)
        SpecialObject = ParameterTemplate(dtype=str)
        SpecialObjectAttachToBone = ParameterTemplate(dtype=str)
        SpecialObjectsPersistent = ParameterTemplate(dtype=bool)
        MaxSpecialObjects = ParameterTemplate(dtype=int)
        EffectDuration = ParameterTemplate(dtype=int)
        EffectValue = ParameterTemplate(dtype=int)
        UniqueSpecialObjectTargets = ParameterTemplate(dtype=bool)
        SpecialObjectsPersistWhenOwnerDies = ParameterTemplate(dtype=bool)
        AlwaysValidateSpecialObjects = ParameterTemplate(dtype=bool)
        FlipOwnerAfterPacking = ParameterTemplate(dtype=bool)
        FlipOwnerAfterUnpacking = ParameterTemplate(dtype=bool)
        FleeRangeAfterCompletion = ParameterTemplate(dtype=float)
        DisableFXParticleSystem = ParameterTemplate(dtype=str)
        DoCaptureFX = ParameterTemplate(dtype=bool)
        PackSound = ParameterTemplate(dtype=str)
        UnpackSound = ParameterTemplate(dtype=str)
        PrepSoundLoop = ParameterTemplate(dtype=str)
        TriggerSound = ParameterTemplate(dtype=str)
        LoseStealthOnTrigger = ParameterTemplate(dtype=bool)
        AwardXPForTriggering = ParameterTemplate(dtype=int)
        SkillPointsForTriggering = ParameterTemplate(dtype=int)
        ApproachRequiresLOS = ParameterTemplate(dtype=bool)
        NeedToFaceTarget = ParameterTemplate(dtype=bool)
        UnpackTime = ParameterTemplate(dtype=int)
        PackTime = ParameterTemplate(dtype=int)
        PersistentPrepTime = ParameterTemplate(dtype=int)
        PersistenceRequiresRecharge = ParameterTemplate(dtype=bool)

    class OCLSpecialPower(ModuleTemplate):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)
        OCL = ParameterTemplate(dtype=str)
        UpgradeOCL = ParameterTemplate(dtype=list, allow_duplicates=True)
        OCLAdjustPositionToPassable = ParameterTemplate(dtype=bool)
        CreateLocation = ParameterTemplate(dtype=list)
        StartsPaused = ParameterTemplate(dtype=bool)
        ReferenceObject = ParameterTemplate(dtype=str)
        ScriptedSpecialPowerOnly = ParameterTemplate(dtype=bool)

    class OCLUpdate(ModuleTemplate):
        FactionTriggered = ParameterTemplate(dtype=bool)
        FactionOCL = ParameterTemplate(dtype=list, allow_duplicates=True)
        MinDelay = ParameterTemplate(dtype=int)
        MaxDelay = ParameterTemplate(dtype=int)
        CreateAtEdge = ParameterTemplate(dtype=bool)
        OCL = ParameterTemplate(dtype=str)

    class CleanupAreaPower(ModuleTemplate):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)
        MaxMoveDistanceFromLocation = ParameterTemplate(dtype=float)
        StartsPaused = ParameterTemplate(dtype=bool)
        InitiateSound = ParameterTemplate(dtype=str)

    class SpyVisionSpecialPower(ModuleTemplate):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)
        BaseDuration = ParameterTemplate(dtype=int)
        StartsPaused = ParameterTemplate(dtype=bool)

        BonusDurationPerCaptured = ParameterTemplate(dtype=int)  # obsolete
        MaxDuration = ParameterTemplate(dtype=int)  # obsolete

    class LeafletDropBehavior(ModuleTemplate):
        DisabledDuration = ParameterTemplate(dtype=int)
        Delay = ParameterTemplate(dtype=int)
        AffectRadius = ParameterTemplate(dtype=float)
        LeafletFXParticleSystem = ParameterTemplate(dtype=str)

    class SpectreGunshipUpdate(ModuleTemplate):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)
        GunshipOrbitRadius = ParameterTemplate(dtype=int)
        TargetingReticleRadius = ParameterTemplate(dtype=int)
        AttackAreaRadius = ParameterTemplate(dtype=int)
        OrbitTime = ParameterTemplate(dtype=int)
        OrbitInsertionSlope = ParameterTemplate(dtype=float)

        HowitzerWeaponTemplate = ParameterTemplate(dtype=str)
        HowitzerFiringRate = ParameterTemplate(dtype=int)
        HowitzerFollowLag = ParameterTemplate(dtype=int)
        RandomOffsetForHowitzer = ParameterTemplate(dtype=int)

        GattlingTemplateName = ParameterTemplate(dtype=str)
        GattlingStrafeFXParticleSystem = ParameterTemplate(dtype=str)
        StrafingIncrement = ParameterTemplate(dtype=int)

        class AttackAreaDecal(ModuleTemplate):
            Texture = ParameterTemplate(dtype=str)
            Style = ParameterTemplate(dtype=str)
            OpacityMin = ParameterTemplate(dtype=str)  # percent
            OpacityMax = ParameterTemplate(dtype=str)  # percent
            OpacityThrobTime = ParameterTemplate(dtype=int)
            Color = ParameterTemplate(dtype=list)  # [r: g: b: a:]
            OnlyVisibleToOwningPlayer = ParameterTemplate(dtype=bool)

        class TargetingReticleDecal(AttackAreaDecal):
            pass

    class BattlePlanUpdate(ModuleTemplate):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)

        BombardmentPlanAnimationTime = ParameterTemplate(dtype=int)
        HoldTheLinePlanAnimationTime = ParameterTemplate(dtype=int)
        SearchAndDestroyPlanAnimationTime = ParameterTemplate(dtype=int)
        TransitionIdleTime = ParameterTemplate(dtype=int)

        BombardmentAnnouncementName = ParameterTemplate(dtype=str)
        BombardmentPlanUnpackSoundName = ParameterTemplate(dtype=str)
        BombardmentPlanPackSoundName = ParameterTemplate(dtype=str)

        SearchAndDestroyPlanUnpackSoundName = ParameterTemplate(dtype=str)
        SearchAndDestroyPlanIdleLoopSoundName = ParameterTemplate(dtype=str)
        SearchAndDestroyPlanPackSoundName = ParameterTemplate(dtype=str)
        SearchAndDestroyAnnouncementName = ParameterTemplate(dtype=str)

        HoldTheLinePlanUnpackSoundName = ParameterTemplate(dtype=str)
        HoldTheLinePlanPackSoundName = ParameterTemplate(dtype=str)
        HoldTheLineAnnouncementName = ParameterTemplate(dtype=str)

        HoldTheLineMessageLabel = ParameterTemplate(dtype=str)
        BombardmentMessageLabel = ParameterTemplate(dtype=str)
        SearchAndDestroyMessageLabel = ParameterTemplate(dtype=str)

        ValidMemberKindOf = ParameterTemplate(dtype=list)
        InvalidMemberKindOf = ParameterTemplate(dtype=list)
        BattlePlanChangeParalyzeTime = ParameterTemplate(dtype=int)
        HoldTheLinePlanArmorDamageScalar = ParameterTemplate(dtype=float)
        SearchAndDestroyPlanSightRangeScalar = ParameterTemplate(dtype=float)

        StrategyCenterSearchAndDestroySightRangeScalar = ParameterTemplate(dtype=float)
        StrategyCenterSearchAndDestroyDetectsStealth = ParameterTemplate(dtype=bool)
        StrategyCenterHoldTheLineMaxHealthScalar = ParameterTemplate(dtype=float)
        StrategyCenterHoldTheLineMaxHealthChangeType = ParameterTemplate(dtype=list)

        VisionObjectName = ParameterTemplate(dtype=str)

    class ParticleUplinkCannonUpdate(ModuleTemplate):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)
        BeginChargeTime = ParameterTemplate(dtype=int)
        RaiseAntennaTime = ParameterTemplate(dtype=int)

        ReadyDelayTime = ParameterTemplate(dtype=int)
        WidthGrowTime = ParameterTemplate(dtype=int)
        BeamTravelTime = ParameterTemplate(dtype=int)
        TotalFiringTime = ParameterTemplate(dtype=int)

        RevealRange = ParameterTemplate(dtype=float)

        OuterEffectBoneName = ParameterTemplate(dtype=str)
        OuterEffectNumBones = ParameterTemplate(dtype=int)
        OuterNodesLightFlareParticleSystem = ParameterTemplate(dtype=str)
        OuterNodesMediumFlareParticleSystem = ParameterTemplate(dtype=str)
        OuterNodesIntenseFlareParticleSystem = ParameterTemplate(dtype=str)

        ConnectorBoneName = ParameterTemplate(dtype=str)
        ConnectorMediumLaserName = ParameterTemplate(dtype=str)
        ConnectorIntenseLaserName = ParameterTemplate(dtype=str)
        ConnectorMediumFlare = ParameterTemplate(dtype=str)
        ConnectorIntenseFlare = ParameterTemplate(dtype=str)

        FireBoneName = ParameterTemplate(dtype=str)

        LaserBaseLightFlareParticleSystemName = ParameterTemplate(dtype=str)
        LaserBaseMediumFlareParticleSystemName = ParameterTemplate(dtype=str)
        LaserBaseIntenseFlareParticleSystemName = ParameterTemplate(dtype=str)

        ParticleBeamLaserName = ParameterTemplate(dtype=str)
        SwathOfDeathDistance = ParameterTemplate(dtype=float)
        SwathOfDeathAmplitude = ParameterTemplate(dtype=float)
        TotalScorchMarks = ParameterTemplate(dtype=int)
        ScorchMarkScalar = ParameterTemplate(dtype=float)
        BeamLaunchFX = ParameterTemplate(dtype=str)
        DelayBetweenLaunchFX = ParameterTemplate(dtype=str)
        GroundHitFX = ParameterTemplate(dtype=str)
        DamagePerSecond = ParameterTemplate(dtype=int)
        TotalDamagePulses = ParameterTemplate(dtype=int)
        DamageType = ParameterTemplate(dtype=str)
        DamageRadiusScalar = ParameterTemplate(dtype=float)

        PoweringUpSoundLoop = ParameterTemplate(dtype=str)
        UnpackToIdleSoundLoop = ParameterTemplate(dtype=str)
        FiringToPackSoundLoop = ParameterTemplate(dtype=str)
        GroundAnnihilationSoundLoop = ParameterTemplate(dtype=str)

        DamagePulseRemnantObjectName = ParameterTemplate(dtype=str)
        ManualDrivingSpeed = ParameterTemplate(dtype=int)
        ManualFastDrivingSpeed = ParameterTemplate(dtype=int)
        DoubleClickToFastDriveDelay = ParameterTemplate(dtype=int)

    class MissileLauncherBuildingUpdate(ModuleTemplate):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)
        DoorOpenTime = ParameterTemplate(dtype=int)
        # DoorOpeningTime = ParameterTemplate(dtype=int)  # @TODO, rm; used?
        DoorWaitOpenTime = ParameterTemplate(dtype=int)
        DoorCloseTime = ParameterTemplate(dtype=int)

        DoorOpeningFX = ParameterTemplate(dtype=str)
        DoorOpenFX = ParameterTemplate(dtype=str)
        DoorWaitingToCloseFX = ParameterTemplate(dtype=str)
        DoorClosingFX = ParameterTemplate(dtype=str)
        DoorClosedFX = ParameterTemplate(dtype=str)
        DoorOpenIdleAudio = ParameterTemplate(dtype=str)

    class CashBountyPower(ModuleTemplate):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)
        Bounty = ParameterTemplate(dtype=str)  # percent
        StartsPaused = ParameterTemplate(dtype=bool)

    class CashHackSpecialPower(ModuleTemplate):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)
        MoneyAmount = ParameterTemplate(dtype=int)
        UpgradeMoneyAmount = ParameterTemplate(dtype=list, allow_duplicates=True)
        StartsPaused = ParameterTemplate(dtype=bool)

    class SpectreGunshipDeploymentUpdate(ModuleTemplate):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)
        RequiredScience = ParameterTemplate(dtype=str)
        GunshipTemplateName = ParameterTemplate(dtype=str)
        AttackAreaRadius = ParameterTemplate(dtype=int)
        CreateLocation = ParameterTemplate(dtype=list)

    class BaikonurLaunchPower(ModuleTemplate):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)
        DetonationObject = ParameterTemplate(dtype=str)
        StartsPaused = ParameterTemplate(dtype=bool)

    class DefectorSpecialPower(ModuleTemplate):
        SpecialPowerTemplate = ParameterTemplate(dtype=str)
        FatCursorRadius = ParameterTemplate(dtype=float)
        StartsPaused = ParameterTemplate(dtype=bool)

    ###########################################################################
    # Contain ModuleTemplates
    class _ContainBehavior(ModuleTemplate):
        Slots = ParameterTemplate(dtype=int)
        DamagePercentToUnits = ParameterTemplate(dtype=str)
        AllowInsideKindOf = ParameterTemplate(dtype=list)
        ForbidInsideKindOf = ParameterTemplate(dtype=list)
        DoorOpenTime = ParameterTemplate(dtype=int)
        ScatterNearbyOnExit = ParameterTemplate(dtype=bool)
        DestroyRidersWhoAreNotFreeToExit = ParameterTemplate(dtype=bool)
        ResetMoodCheckTimeOnExit = ParameterTemplate(dtype=bool)
        OrientLikeContainerOnExit = ParameterTemplate(dtype=bool)
        KeepContainerVelocityOnExit = ParameterTemplate(dtype=bool)

    class TransportContain(_ContainBehavior):
        AllowAlliesInside = ParameterTemplate(dtype=bool)
        AllowNeutralInside = ParameterTemplate(dtype=bool)
        AllowEnemiesInside = ParameterTemplate(dtype=bool)
        ExitDelay = ParameterTemplate(dtype=int)
        NumberOfExitPaths = ParameterTemplate(dtype=int)
        GoAggressiveOnExit = ParameterTemplate(dtype=bool)
        BurnedDeathToUnits = ParameterTemplate(dtype=bool)
        ExitPitchRate = ParameterTemplate(dtype=int)
        ExitBone = ParameterTemplate(dtype=str)

        HealthRegen_PerSec = ParameterTemplate(dtype=int, token="HealthRegen%PerSec")  # percent
        InitialPayload = ParameterTemplate(dtype=list)
        ArmedRidersUpgradeMyWeaponSet = ParameterTemplate(dtype=bool)
        DelayExitInAir = ParameterTemplate(dtype=bool, allow_clobber=True)  # @todo, bug Demobus
        EnterSound = ParameterTemplate(dtype=str)  # SoundEnter override
        ExitSound = ParameterTemplate(dtype=str)  # SoundExit override
        WeaponBonusPassedToPassengers = ParameterTemplate(dtype=bool)
        PassengersAllowedToFire = ParameterTemplate(dtype=bool)

    class InternetHackContain(TransportContain):
        pass

    class OverlordContain(ModuleTemplate):
        Slots = ParameterTemplate(dtype=int)
        DamagePercentToUnits = ParameterTemplate(dtype=str)
        AllowInsideKindOf = ParameterTemplate(dtype=list)

        PassengersAllowedToFire = ParameterTemplate(dtype=bool)
        PassengersInTurret = ParameterTemplate(dtype=bool)
        ExperienceSinkForRider = ParameterTemplate(dtype=bool)
        WeaponBonusPassedToPassengers = ParameterTemplate(dtype=bool)
        PayloadTemplateName = ParameterTemplate(dtype=str)
        InitialPayload = ParameterTemplate(dtype=list)  # str, int tuple

    class GarrisonContain(ModuleTemplate):
        ContainMax = ParameterTemplate(dtype=int)
        EnterSound = ParameterTemplate(dtype=str)  # SoundEnter override?
        ExitSound = ParameterTemplate(dtype=str)  # SoundExit override?
        DamagePercentToUnits = ParameterTemplate(dtype=str)
        MobileGarrison = ParameterTemplate(dtype=bool)
        InitialRoster = ParameterTemplate(dtype=list)
        ImmuneToClearBuildingAttacks = ParameterTemplate(dtype=bool)
        IsEnclosingContainer = ParameterTemplate(dtype=bool)
        HealObjects = ParameterTemplate(dtype=bool)
        TimeForFullHeal = ParameterTemplate(dtype=int)
        PassengersAllowedToFire = ParameterTemplate(dtype=bool)
        AllowInsideKindOf = ParameterTemplate(dtype=list)
        ForbidInsideKindOf = ParameterTemplate(dtype=list)
        AllowAlliesInside = ParameterTemplate(dtype=bool)
        AllowEnemiesInside = ParameterTemplate(dtype=bool)
        AllowNeutralInside = ParameterTemplate(dtype=bool)

    class HelixContain(ModuleTemplate):
        Slots = ParameterTemplate(dtype=int)
        DamagePercentToUnits = ParameterTemplate(dtype=str)
        AllowInsideKindOf = ParameterTemplate(dtype=list)
        ForbidInsideKindOf = ParameterTemplate(dtype=list)
        AllowAlliesInside = ParameterTemplate(dtype=bool)
        AllowNeutralInside = ParameterTemplate(dtype=bool)
        AllowEnemiesInside = ParameterTemplate(dtype=bool)
        ExitDelay = ParameterTemplate(dtype=int)
        NumberOfExitPaths = ParameterTemplate(dtype=int)
        GoAggressiveOnExit = ParameterTemplate(dtype=bool)
        ScatterNearbyOnExit = ParameterTemplate(dtype=bool)
        OrientLikeContainerOnExit = ParameterTemplate(dtype=bool)
        KeepContainerVelocityOnExit = ParameterTemplate(dtype=bool)
        BurnedDeathToUnits = ParameterTemplate(dtype=bool)
        ExitPitchRate = ParameterTemplate(dtype=int)
        ExitBone = ParameterTemplate(dtype=str)
        DoorOpenTime = ParameterTemplate(dtype=int)
        # HealthRegen%PerSec = ParameterTemplate(dtype=int)  # percent
        DestroyRidersWhoAreNotFreeToExit = ParameterTemplate(dtype=bool)
        ResetMoodCheckTimeOnExit = ParameterTemplate(dtype=bool)
        # InitialPayload = ParameterTemplate(dtype=list) ?
        ArmedRidersUpgradeMyWeaponSet = ParameterTemplate(dtype=bool)
        DelayExitInAir = ParameterTemplate(dtype=bool)
        EnterSound = ParameterTemplate(dtype=str)  # SoundEnter override
        ExitSound = ParameterTemplate(dtype=str)  # SoundExit override
        PassengersAllowedToFire = ParameterTemplate(dtype=bool)
        PassengersInTurret = ParameterTemplate(dtype=bool)
        WeaponBonusPassedToPassengers = ParameterTemplate(dtype=bool)
        PayloadTemplateName = ParameterTemplate(dtype=str)
        ShouldDrawPips = ParameterTemplate(dtype=bool)

    class RiderChangeContain(ModuleTemplate):
        Rider1 = ParameterTemplate(dtype=list)
        Rider2 = ParameterTemplate(dtype=list)
        Rider3 = ParameterTemplate(dtype=list)
        Rider4 = ParameterTemplate(dtype=list)
        Rider5 = ParameterTemplate(dtype=list)
        Rider6 = ParameterTemplate(dtype=list)
        Rider7 = ParameterTemplate(dtype=list)
        Rider8 = ParameterTemplate(dtype=list)
        ScuttleDelay = ParameterTemplate(dtype=int)
        ScuttleStatus = ParameterTemplate(dtype=str)

        Slots = ParameterTemplate(dtype=int)
        DamagePercentToUnits = ParameterTemplate(dtype=str)
        AllowInsideKindOf = ParameterTemplate(dtype=list)
        ForbidInsideKindOf = ParameterTemplate(dtype=list)

        ExitDelay = ParameterTemplate(dtype=int)
        NumberOfExitPaths = ParameterTemplate(dtype=int)
        GoAggressiveOnExit = ParameterTemplate(dtype=bool)
        ScatterNearbyOnExit = ParameterTemplate(dtype=bool)
        OrientLikeContainerOnExit = ParameterTemplate(dtype=bool)
        KeepContainerVelocityOnExit = ParameterTemplate(dtype=bool)
        BurnedDeathToUnits = ParameterTemplate(dtype=bool)
        ExitPitchRate = ParameterTemplate(dtype=int)
        ExitBone = ParameterTemplate(dtype=str)
        DoorOpenTime = ParameterTemplate(dtype=int)
        HealthRegen_PerSec = ParameterTemplate(token="HealthRegen%PerSec", dtype=int)  # percent
        DestroyRidersWhoAreNotFreeToExit = ParameterTemplate(dtype=bool)
        ResetMoodCheckTimeOnExit = ParameterTemplate(dtype=bool)
        InitialPayload = ParameterTemplate(dtype=list)
        ArmedRidersUpgradeMyWeaponSet = ParameterTemplate(dtype=bool)
        DelayExitInAir = ParameterTemplate(dtype=bool)
        EnterSound = ParameterTemplate(dtype=str)  # SoundEnter override
        ExitSound = ParameterTemplate(dtype=str)  # SoundExit override

    class MobNexusContain(ModuleTemplate):
        Slots = ParameterTemplate(dtype=int)
        InitialPayload = ParameterTemplate(dtype=list)
        DamagePercentToUnits = ParameterTemplate(dtype=str)  # percent
        HealthRegen_PerSec = ParameterTemplate(dtype=str, token="HealthRegen%PerSec")

    class ParachuteContain(ModuleTemplate):
        PitchRateMax = ParameterTemplate(dtype=int)
        RollRateMax = ParameterTemplate(dtype=int)
        LowAltitudeDamping = ParameterTemplate(dtype=float)
        ParachuteOpenDist = ParameterTemplate(dtype=float)
        KillWhenLandingInWaterSlop = ParameterTemplate(dtype=bool)
        FreeFallDamagePercent = ParameterTemplate(dtype=str)  # percent
        AllowInsideKindOf = ParameterTemplate(dtype=list)
        ForbidInsideKindOf = ParameterTemplate(dtype=list)
        ParachuteOpenSound = ParameterTemplate(dtype=str)

    class HealContain(ModuleTemplate):
        ContainMax = ParameterTemplate(dtype=int)
        TimeForFullHeal = ParameterTemplate(dtype=int)
        EnterSound = ParameterTemplate(dtype=str)  # SoundEnter override?
        ExitSound = ParameterTemplate(dtype=str)  # SoundExit override?
        AllowInsideKindOf = ParameterTemplate(dtype=list)
        ForbidInsideKindOf = ParameterTemplate(dtype=list)
        AllowAlliesInside = ParameterTemplate(dtype=bool)
        AllowNeutralInside = ParameterTemplate(dtype=bool)
        AllowEnemiesInside = ParameterTemplate(dtype=bool)

    class TunnelContain(ModuleTemplate):
        TimeForFullHeal = ParameterTemplate(dtype=int)
        EnterSound = ParameterTemplate(dtype=str)  # SoundEnter override?
        ExitSound = ParameterTemplate(dtype=str)  # SoundExit override?
        NumberOfExitPaths = ParameterTemplate(dtype=int)
        AllowAlliesInside = ParameterTemplate(dtype=bool)
        AllowNeutralInside = ParameterTemplate(dtype=bool)
        AllowEnemiesInside = ParameterTemplate(dtype=bool)
        ExemptStatus = ParameterTemplate(dtype=list)

    class RailedTransportContain(_ContainBehavior):
        pass

    ###########################################################################
    # AI Update ModuleTemplates
    class AIUpdateInterface(ModuleTemplate):
        AutoAcquireEnemiesWhenIdle = ParameterTemplate(dtype=list)
        MoodAttackCheckRate = ParameterTemplate(dtype=int)
        ForbidPlayerCommands = ParameterTemplate(dtype=bool)
        TurretsLinked = ParameterTemplate(dtype=bool)

        class Turret(ModuleTemplate):
            ControlledWeaponSlots = ParameterTemplate(dtype=list)
            TurretTurnRate = ParameterTemplate(dtype=int)
            TurretPitchRate = ParameterTemplate(dtype=int)
            NaturalTurretAngle = ParameterTemplate(dtype=int)
            NaturalTurretPitch = ParameterTemplate(dtype=int)
            FirePitch = ParameterTemplate(dtype=int)
            MinPhysicalPitch = ParameterTemplate(dtype=int)
            GroundUnitPitch = ParameterTemplate(dtype=int)
            TurretFireAngleSweep = ParameterTemplate(dtype=list, allow_duplicates=True)
            TurretSweepSpeedModifier = ParameterTemplate(dtype=list, allow_duplicates=True)
            AllowsPitch = ParameterTemplate(dtype=bool)
            MinIdleScanAngle = ParameterTemplate(dtype=float)
            MaxIdleScanAngle = ParameterTemplate(dtype=float)
            MinIdleScanInterval = ParameterTemplate(dtype=int)
            MaxIdleScanInterval = ParameterTemplate(dtype=int)
            RecenterTime = ParameterTemplate(dtype=int)
            FiresWhileTurning = ParameterTemplate(dtype=bool)
            InitiallyDisabled = ParameterTemplate(dtype=bool)

        class AltTurret(Turret):
            pass

    class ChinookAIUpdate(AIUpdateInterface):
        RappelSpeed = ParameterTemplate(dtype=int)
        RopeDropSpeed = ParameterTemplate(dtype=int)
        RopeName = ParameterTemplate(dtype=str)
        RopeFinalHeight = ParameterTemplate(dtype=int)
        RopeWidth = ParameterTemplate(dtype=float)
        RopeWobbleLen = ParameterTemplate(dtype=int)
        RopeWobbleAmplitude = ParameterTemplate(dtype=float)
        RopeWobbleRate = ParameterTemplate(dtype=int)
        RopeColor = ParameterTemplate(dtype=list)  # @TODO [r: g: b:]
        RotorWashParticleSystem = ParameterTemplate(dtype=str)
        NumRopes = ParameterTemplate(dtype=int)
        PerRopeDelayMin = ParameterTemplate(dtype=int)
        PerRopeDelayMax = ParameterTemplate(dtype=int)
        MinDropHeight = ParameterTemplate(dtype=int)
        WaitForRopesToDrop = ParameterTemplate(dtype=bool)

        MaxBoxes = ParameterTemplate(dtype=int)
        SupplyCenterActionDelay = ParameterTemplate(dtype=int)
        SupplyWarehouseActionDelay = ParameterTemplate(dtype=int)
        SupplyWarehouseScanDistance = ParameterTemplate(dtype=int)
        SuppliesDepletedVoice = ParameterTemplate(dtype=str)
        UpgradedSupplyBoost = ParameterTemplate(dtype=str)  # percent

    class JetAIUpdate(AIUpdateInterface):
        # ForbidPlayerCommands ?
        # TurretsLinked ?

        OutOfAmmoDamagePerSecond = ParameterTemplate(dtype=str)  # percent
        NeedsRunway = ParameterTemplate(dtype=bool)
        KeepsParkingSpaceWhenAirborne = ParameterTemplate(dtype=bool)
        TakeoffDistForMaxLift = ParameterTemplate(dtype=str)  # percent
        TakeoffPause = ParameterTemplate(dtype=int)
        MinHeight = ParameterTemplate(dtype=int)
        ParkingOffset = ParameterTemplate(dtype=list)
        SneakyOffsetWhenAttacking = ParameterTemplate(dtype=float)
        AttackLocomotorType = ParameterTemplate(dtype=str)
        AttackLocomotorPersistTime = ParameterTemplate(dtype=float)
        AttackersMissPersistTime = ParameterTemplate(dtype=float)
        ReturnToBaseIdleTime = ParameterTemplate(dtype=int)
        ReturnForAmmoLocomotorType = ParameterTemplate(dtype=str)
        LockonTime = ParameterTemplate(dtype=int)
        LockonCursor = ParameterTemplate(dtype=str)
        LockonInitialDist = ParameterTemplate(dtype=int)
        LockonFreq = ParameterTemplate(dtype=float)
        LockonAngleSpin = ParameterTemplate(dtype=float)
        LockonBlinky = ParameterTemplate(dtype=bool)

    class DeployStyleAIUpdate(AIUpdateInterface):
        PackTime = ParameterTemplate(dtype=int)
        UnpackTime = ParameterTemplate(dtype=int)
        TurretsFunctionOnlyWhenDeployed = ParameterTemplate(dtype=bool)
        TurretsMustCenterBeforePacking = ParameterTemplate(dtype=bool)
        ManualDeployAnimations = ParameterTemplate(dtype=bool)
        ResetTurretBeforePacking = ParameterTemplate(dtype=bool)

    class DozerAIUpdate(AIUpdateInterface):
        RepairHealthPercentPerSecond = ParameterTemplate(dtype=str)
        BoredTime = ParameterTemplate(dtype=int)
        BoredRange = ParameterTemplate(dtype=int)

    class SupplyTruckAIUpdate(AIUpdateInterface):
        MaxBoxes = ParameterTemplate(dtype=int)
        SupplyCenterActionDelay = ParameterTemplate(dtype=int)
        SupplyWarehouseActionDelay = ParameterTemplate(dtype=int)
        SupplyWarehouseScanDistance = ParameterTemplate(dtype=int)
        SuppliesDepletedVoice = ParameterTemplate(dtype=str)

    class TransportAIUpdate(AIUpdateInterface):
        pass

    class AssaultTransportAIUpdate(TransportAIUpdate):
        MembersGetHealedAtLifeRatio = ParameterTemplate(dtype=float)
        ClearRangeRequiredToContinueAttackMove = ParameterTemplate(dtype=int)

    class WanderAIUpdate(ModuleTemplate):
        pass

    class WorkerAIUpdate(ModuleTemplate):
        RepairHealthPercentPerSecond = ParameterTemplate(dtype=str)
        BoredTime = ParameterTemplate(dtype=int)
        BoredRange = ParameterTemplate(dtype=int)
        MaxBoxes = ParameterTemplate(dtype=int)
        AutoAcquireEnemiesWhenIdle = ParameterTemplate(dtype=list)
        UpgradedSupplyBoost = ParameterTemplate(dtype=int)
        SupplyCenterActionDelay = ParameterTemplate(dtype=int)
        SupplyWarehouseActionDelay = ParameterTemplate(dtype=int)
        SupplyWarehouseScanDistance = ParameterTemplate(dtype=int)
        SuppliesDepletedVoice = ParameterTemplate(dtype=str)

    class HackInternetAIUpdate(ModuleTemplate):
        UnpackTime = ParameterTemplate(dtype=int)
        PackTime = ParameterTemplate(dtype=int)
        PackUnpackVariationFactor = ParameterTemplate(dtype=float)
        CashUpdateDelay = ParameterTemplate(dtype=int)
        CashUpdateDelayFast = ParameterTemplate(dtype=int)
        RegularCashAmount = ParameterTemplate(dtype=int)
        VeteranCashAmount = ParameterTemplate(dtype=int)
        EliteCashAmount = ParameterTemplate(dtype=int)
        HeroicCashAmount = ParameterTemplate(dtype=int)
        XpPerCashUpdate = ParameterTemplate(dtype=int)

    class MissileAIUpdate(ModuleTemplate):
        DetonateOnNoFuel = ParameterTemplate(dtype=bool)
        DetonateCallsKill = ParameterTemplate(dtype=bool)
        UseWeaponSpeed = ParameterTemplate(dtype=bool)
        IgnitionFX = ParameterTemplate(dtype=str)
        InitialVelocity = ParameterTemplate(dtype=int)
        IgnitionDelay = ParameterTemplate(dtype=int)
        FuelLifetime = ParameterTemplate(dtype=int)
        TryToFollowTarget = ParameterTemplate(dtype=bool)
        KillSelfDelay = ParameterTemplate(dtype=int)

        DistanceScatterWhenJammed = ParameterTemplate(dtype=int)

        GarrisonHitKillRequiredKindOf = ParameterTemplate(dtype=str)
        GarrisonHitKillForbiddenKindOf = ParameterTemplate(dtype=str)
        GarrisonHitKillCount = ParameterTemplate(dtype=int)
        GarrisonHitKillFX = ParameterTemplate(dtype=str)
        DistanceToTargetForLock = ParameterTemplate(dtype=int)
        DistanceToTargetBeforeDiving = ParameterTemplate(dtype=int)
        DistanceToTravelBeforeTurning = ParameterTemplate(dtype=int)

    class DeliverPayloadAIUpdate(ModuleTemplate):
        DoorDelay = ParameterTemplate(dtype=int)
        DeliveryDistance = ParameterTemplate(dtype=int)
        MaxAttempts = ParameterTemplate(dtype=int)
        DropDelay = ParameterTemplate(dtype=int)
        DropOffset = ParameterTemplate(dtype=list)  # [x: y: z:]
        DropVariance = ParameterTemplate(dtype=list)  # [x: y: z:]
        PutInContainer = ParameterTemplate(dtype=str)

    class RailedTransportAIUpdate(ModuleTemplate):
        PathPrefixName = ParameterTemplate(dtype=str)

    ###########################################################################
    # Damage ModuleTemplates
    class TransitionDamageFX(ModuleTemplate):
        DamageFXTypes = ParameterTemplate(dtype=list)
        DamageParticleTypes = ParameterTemplate(dtype=list)

        DamagedFXList1 = ParameterTemplate(dtype=list)
        DamagedOCL1 = ParameterTemplate(dtype=list)
        DamagedParticleSystem1 = ParameterTemplate(dtype=list)

        DamagedFXList2 = ParameterTemplate(dtype=list)
        DamagedOCL2 = ParameterTemplate(dtype=list)
        DamagedParticleSystem2 = ParameterTemplate(dtype=list)

        DamagedFXList3 = ParameterTemplate(dtype=list)
        DamagedOCL3 = ParameterTemplate(dtype=list)
        DamagedParticleSystem3 = ParameterTemplate(dtype=list)

        DamagedFXList4 = ParameterTemplate(dtype=list)
        DamagedOCL4 = ParameterTemplate(dtype=list)
        DamagedParticleSystem4 = ParameterTemplate(dtype=list)

        DamagedFXList5 = ParameterTemplate(dtype=list)
        DamagedOCL5 = ParameterTemplate(dtype=list)
        DamagedParticleSystem5 = ParameterTemplate(dtype=list)

        DamagedFXList6 = ParameterTemplate(dtype=list)
        DamagedOCL6 = ParameterTemplate(dtype=list)
        DamagedParticleSystem6 = ParameterTemplate(dtype=list)

        DamagedFXList7 = ParameterTemplate(dtype=list)
        DamagedOCL7 = ParameterTemplate(dtype=list)
        DamagedParticleSystem7 = ParameterTemplate(dtype=list)

        DamagedFXList8 = ParameterTemplate(dtype=list)
        DamagedOCL8 = ParameterTemplate(dtype=list)
        DamagedParticleSystem8 = ParameterTemplate(dtype=list)

        DamagedFXList9 = ParameterTemplate(dtype=list)
        DamagedOCL9 = ParameterTemplate(dtype=list)
        DamagedParticleSystem9 = ParameterTemplate(dtype=list)

        DamagedFXList10 = ParameterTemplate(dtype=list)
        DamagedOCL10 = ParameterTemplate(dtype=list)
        DamagedParticleSystem10 = ParameterTemplate(dtype=list)

        DamagedFXList11 = ParameterTemplate(dtype=list)
        DamagedOCL11 = ParameterTemplate(dtype=list)
        DamagedParticleSystem11 = ParameterTemplate(dtype=list)

        DamagedFXList12 = ParameterTemplate(dtype=list)
        DamagedOCL12 = ParameterTemplate(dtype=list)
        DamagedParticleSystem12 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList1 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL1 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem1 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList2 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL2 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem2 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList3 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL3 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem3 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList4 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL4 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem4 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList5 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL5 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem5 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList6 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL6 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem6 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList7 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL7 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem7 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList8 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL8 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem8 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList9 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL9 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem9 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList10 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL10 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem10 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList11 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL11 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem11 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList12 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL12 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem12 = ParameterTemplate(dtype=list)

        RubbleFXList1 = ParameterTemplate(dtype=list)
        RubbleOCL1 = ParameterTemplate(dtype=list)
        RubbleParticleSystem1 = ParameterTemplate(dtype=list)

        RubbleFXList2 = ParameterTemplate(dtype=list)
        RubbleOCL2 = ParameterTemplate(dtype=list)
        RubbleParticleSystem2 = ParameterTemplate(dtype=list)

        RubbleFXList3 = ParameterTemplate(dtype=list)
        RubbleOCL3 = ParameterTemplate(dtype=list)
        RubbleParticleSystem3 = ParameterTemplate(dtype=list)

        RubbleFXList4 = ParameterTemplate(dtype=list)
        RubbleOCL4 = ParameterTemplate(dtype=list)
        RubbleParticleSystem4 = ParameterTemplate(dtype=list)

        RubbleFXList5 = ParameterTemplate(dtype=list)
        RubbleOCL5 = ParameterTemplate(dtype=list)
        RubbleParticleSystem5 = ParameterTemplate(dtype=list)

        RubbleFXList6 = ParameterTemplate(dtype=list)
        RubbleOCL6 = ParameterTemplate(dtype=list)
        RubbleParticleSystem6 = ParameterTemplate(dtype=list)

        RubbleFXList7 = ParameterTemplate(dtype=list)
        RubbleOCL7 = ParameterTemplate(dtype=list)
        RubbleParticleSystem7 = ParameterTemplate(dtype=list)

        RubbleFXList8 = ParameterTemplate(dtype=list)
        RubbleOCL8 = ParameterTemplate(dtype=list)
        RubbleParticleSystem8 = ParameterTemplate(dtype=list)

        RubbleFXList9 = ParameterTemplate(dtype=list)
        RubbleOCL9 = ParameterTemplate(dtype=list)
        RubbleParticleSystem9 = ParameterTemplate(dtype=list)

        RubbleFXList10 = ParameterTemplate(dtype=list)
        RubbleOCL10 = ParameterTemplate(dtype=list)
        RubbleParticleSystem10 = ParameterTemplate(dtype=list)

        RubbleFXList11 = ParameterTemplate(dtype=list)
        RubbleOCL11 = ParameterTemplate(dtype=list)
        RubbleParticleSystem11 = ParameterTemplate(dtype=list)

        RubbleFXList12 = ParameterTemplate(dtype=list)
        RubbleOCL12 = ParameterTemplate(dtype=list)
        RubbleParticleSystem12 = ParameterTemplate(dtype=list)

    class BoneFXDamage(ModuleTemplate):
        pass

    class BoneFXUpdate(ModuleTemplate):
        DamageFXTypes = ParameterTemplate(dtype=list)
        DamageParticleTypes = ParameterTemplate(dtype=list)

        PristineFXList1 = ParameterTemplate(dtype=list)
        PristineOCL1 = ParameterTemplate(dtype=list)
        PristineParticleSystem1 = ParameterTemplate(dtype=list)

        PristineFXList2 = ParameterTemplate(dtype=list)
        PristineOCL2 = ParameterTemplate(dtype=list)
        PristineParticleSystem2 = ParameterTemplate(dtype=list)

        PristineFXList3 = ParameterTemplate(dtype=list)
        PristineOCL3 = ParameterTemplate(dtype=list)
        PristineParticleSystem3 = ParameterTemplate(dtype=list)

        PristineFXList4 = ParameterTemplate(dtype=list)
        PristineOCL4 = ParameterTemplate(dtype=list)
        PristineParticleSystem4 = ParameterTemplate(dtype=list)

        PristineFXList5 = ParameterTemplate(dtype=list)
        PristineOCL5 = ParameterTemplate(dtype=list)
        PristineParticleSystem5 = ParameterTemplate(dtype=list)

        PristineFXList6 = ParameterTemplate(dtype=list)
        PristineOCL6 = ParameterTemplate(dtype=list)
        PristineParticleSystem6 = ParameterTemplate(dtype=list)

        PristineFXList7 = ParameterTemplate(dtype=list)
        PristineOCL7 = ParameterTemplate(dtype=list)
        PristineParticleSystem7 = ParameterTemplate(dtype=list)

        PristineFXList8 = ParameterTemplate(dtype=list)
        PristineOCL8 = ParameterTemplate(dtype=list)
        PristineParticleSystem8 = ParameterTemplate(dtype=list)

        DamagedFXList1 = ParameterTemplate(dtype=list)
        DamagedOCL1 = ParameterTemplate(dtype=list)
        DamagedParticleSystem1 = ParameterTemplate(dtype=list)

        DamagedFXList2 = ParameterTemplate(dtype=list)
        DamagedOCL2 = ParameterTemplate(dtype=list)
        DamagedParticleSystem2 = ParameterTemplate(dtype=list)

        DamagedFXList3 = ParameterTemplate(dtype=list)
        DamagedOCL3 = ParameterTemplate(dtype=list)
        DamagedParticleSystem3 = ParameterTemplate(dtype=list)

        DamagedFXList4 = ParameterTemplate(dtype=list)
        DamagedOCL4 = ParameterTemplate(dtype=list)
        DamagedParticleSystem4 = ParameterTemplate(dtype=list)

        DamagedFXList5 = ParameterTemplate(dtype=list)
        DamagedOCL5 = ParameterTemplate(dtype=list)
        DamagedParticleSystem5 = ParameterTemplate(dtype=list)

        DamagedFXList6 = ParameterTemplate(dtype=list)
        DamagedOCL6 = ParameterTemplate(dtype=list)
        DamagedParticleSystem6 = ParameterTemplate(dtype=list)

        DamagedFXList7 = ParameterTemplate(dtype=list)
        DamagedOCL7 = ParameterTemplate(dtype=list)
        DamagedParticleSystem7 = ParameterTemplate(dtype=list)

        DamagedFXList8 = ParameterTemplate(dtype=list)
        DamagedOCL8 = ParameterTemplate(dtype=list)
        DamagedParticleSystem8 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList1 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL1 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem1 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList2 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL2 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem2 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList3 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL3 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem3 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList4 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL4 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem4 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList5 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL5 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem5 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList6 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL6 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem6 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList7 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL7 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem7 = ParameterTemplate(dtype=list)

        ReallyDamagedFXList8 = ParameterTemplate(dtype=list)
        ReallyDamagedOCL8 = ParameterTemplate(dtype=list)
        ReallyDamagedParticleSystem8 = ParameterTemplate(dtype=list)

        RubbleFXList1 = ParameterTemplate(dtype=list)
        RubbleOCL1 = ParameterTemplate(dtype=list)
        RubbleParticleSystem1 = ParameterTemplate(dtype=list)

        RubbleFXList2 = ParameterTemplate(dtype=list)
        RubbleOCL2 = ParameterTemplate(dtype=list)
        RubbleParticleSystem2 = ParameterTemplate(dtype=list)

        RubbleFXList3 = ParameterTemplate(dtype=list)
        RubbleOCL3 = ParameterTemplate(dtype=list)
        RubbleParticleSystem3 = ParameterTemplate(dtype=list)

        RubbleFXList4 = ParameterTemplate(dtype=list)
        RubbleOCL4 = ParameterTemplate(dtype=list)
        RubbleParticleSystem4 = ParameterTemplate(dtype=list)

        RubbleFXList5 = ParameterTemplate(dtype=list)
        RubbleOCL5 = ParameterTemplate(dtype=list)
        RubbleParticleSystem5 = ParameterTemplate(dtype=list)

        RubbleFXList6 = ParameterTemplate(dtype=list)
        RubbleOCL6 = ParameterTemplate(dtype=list)
        RubbleParticleSystem6 = ParameterTemplate(dtype=list)

        RubbleFXList7 = ParameterTemplate(dtype=list)
        RubbleOCL7 = ParameterTemplate(dtype=list)
        RubbleParticleSystem7 = ParameterTemplate(dtype=list)

        RubbleFXList8 = ParameterTemplate(dtype=list)
        RubbleOCL8 = ParameterTemplate(dtype=list)
        RubbleParticleSystem8 = ParameterTemplate(dtype=list)

    class FlammableUpdate(ModuleTemplate):
        BurnedDelay = ParameterTemplate(dtype=int)
        BurningSoundName = ParameterTemplate(dtype=str)
        FlameDamageLimit = ParameterTemplate(dtype=int)
        FlameDamageExpiration = ParameterTemplate(dtype=int)
        AflameDuration = ParameterTemplate(dtype=int)
        AflameDamageAmount = ParameterTemplate(dtype=int)
        AflameDamageDelay = ParameterTemplate(dtype=int)

    class PoisonedBehavior(ModuleTemplate):
        PoisonDamageInterval = ParameterTemplate(dtype=int)
        PoisonDuration = ParameterTemplate(dtype=int)

    class FireSpreadUpdate(ModuleTemplate):
        OCLEmbers = ParameterTemplate(dtype=str)
        MinSpreadDelay = ParameterTemplate(dtype=int)
        MaxSpreadDelay = ParameterTemplate(dtype=int)
        SpreadTryRange = ParameterTemplate(dtype=float)

    ###########################################################################
    # Death and Deletion
    class HeightDieUpdate(ModuleTemplate):
        TargetHeight = ParameterTemplate(dtype=float)
        TargetHeightIncludesStructures = ParameterTemplate(dtype=bool)
        OnlyWhenMovingDown = ParameterTemplate(dtype=bool)
        InitialDelay = ParameterTemplate(dtype=int)
        SnapToGroundOnDeath = ParameterTemplate(dtype=bool)
        DestroyAttachedParticlesAtHeight = ParameterTemplate(dtype=float)

    class DamDie(ModuleTemplate):
        pass

    class DestroyDie(ModuleTemplate):
        DeathTypes = ParameterTemplate(dtype=list)
        RequiredStatus = ParameterTemplate(dtype=str)
        ExemptStatus = ParameterTemplate(dtype=str)

    class EjectPilotDie(DestroyDie):
        GroundCreationList = ParameterTemplate(dtype=str)
        AirCreationList = ParameterTemplate(dtype=str)
        VeterancyLevels = ParameterTemplate(dtype=list)

    class FXListDie(DestroyDie):
        DeathFX = ParameterTemplate(dtype=str)
        OrientToObject = ParameterTemplate(dtype=bool)
        StartsActive = ParameterTemplate(dtype=bool)
        TriggeredBy = ParameterTemplate(dtype=list)
        ConflictsWith = ParameterTemplate(dtype=list)
        RequiresAllTriggers = ParameterTemplate(dtype=bool)

    class KeepObjectDie(DestroyDie):
        pass

    class RebuildHoleExposeDie(DestroyDie):
        HoleName = ParameterTemplate(dtype=str)
        HoleMaxHealth = ParameterTemplate(dtype=float)
        TransferAttackers = ParameterTemplate(dtype=bool)

    class UpgradeDie(DestroyDie):
        UpgradeToRemove = ParameterTemplate(dtype=list)

    class CreateCrateDie(DestroyDie):
        CrateData = ParameterTemplate(dtype=str)

    class CreateObjectDie(DestroyDie):
        CreationList = ParameterTemplate(dtype=str)
        TransferPreviousHealth = ParameterTemplate(dtype=bool)

    class CrushDie(DestroyDie):
        TotalCrushSound = ParameterTemplate(dtype=str)
        BackEndCrushSound = ParameterTemplate(dtype=str)
        FrontEndCrushSound = ParameterTemplate(dtype=str)
        TotalCrushSoundPercent = ParameterTemplate(dtype=str)  # percent
        BackEndCrushSoundPercent = ParameterTemplate(dtype=str)  # percent
        FrontEndCrushSoundPercent = ParameterTemplate(dtype=str)  # percent

    class _DeathBehavior(ModuleTemplate):
        DeathTypes = ParameterTemplate(dtype=list)
        RequiredStatus = ParameterTemplate(dtype=list)
        ExemptStatus = ParameterTemplate(dtype=list)

        FX = ParameterTemplate(dtype=list, allow_duplicates=True)
        OCL = ParameterTemplate(dtype=list, allow_duplicates=True)
        Weapon = ParameterTemplate(dtype=list, allow_duplicates=True)

    class InstantDeathBehavior(_DeathBehavior):
        pass

    class SlowDeathBehavior(_DeathBehavior):
        ProbabilityModifier = ParameterTemplate(dtype=int)
        ModifierBonusPerOverkillPercent = ParameterTemplate(dtype=str)

        SinkRate = ParameterTemplate(dtype=float)
        SinkDelay = ParameterTemplate(dtype=int)
        SinkDelayVariance = ParameterTemplate(dtype=int)

        DestructionDelay = ParameterTemplate(dtype=int)
        DestructionDelayVariance = ParameterTemplate(dtype=int)
        DestructionAltitude = ParameterTemplate(dtype=int)

        FlingForce = ParameterTemplate(dtype=int)
        FlingForceVariance = ParameterTemplate(dtype=int)
        FlingPitch = ParameterTemplate(dtype=int)
        FlingPitchVariance = ParameterTemplate(dtype=int)

    class BattleBusSlowDeathBehavior(SlowDeathBehavior):
        FXStartUndeath = ParameterTemplate(dtype=str)
        OCLStartUndeath = ParameterTemplate(dtype=str)
        FXHitGround = ParameterTemplate(dtype=str)
        OCLHitGround = ParameterTemplate(dtype=str)
        DelayFromGroundToFinalDeath = ParameterTemplate(dtype=int)
        ThrowForce = ParameterTemplate(dtype=float)
        PercentDamageToPassengers = ParameterTemplate(dtype=str)
        EmptyHulkDestructionDelay = ParameterTemplate(dtype=int)

    class HelicopterSlowDeathBehavior(ModuleTemplate):
        DestructionDelay = ParameterTemplate(dtype=int)
        DestructionDelayVariance = ParameterTemplate(dtype=int)
        DestructionAltitude = ParameterTemplate(dtype=int)

        SpiralOrbitTurnRate = ParameterTemplate(dtype=float)
        SpiralOrbitForwardSpeed = ParameterTemplate(dtype=float)
        SpiralOrbitForwardSpeedDamping = ParameterTemplate(dtype=float)
        MinSelfSpin = ParameterTemplate(dtype=int)
        MaxSelfSpin = ParameterTemplate(dtype=int)
        SelfSpinUpdateDelay = ParameterTemplate(dtype=int)
        SelfSpinUpdateAmount = ParameterTemplate(dtype=int)
        MinBladeFlyOffDelay = ParameterTemplate(dtype=int)
        MaxBladeFlyOffDelay = ParameterTemplate(dtype=int)
        AttachParticle = ParameterTemplate(dtype=str)
        AttachParticleBone = ParameterTemplate(dtype=str)
        AttachParticleLoc = ParameterTemplate(dtype=list)
        BladeObjectName = ParameterTemplate(dtype=str)
        BladeBoneName = ParameterTemplate(dtype=str)
        OCLEjectPilot = ParameterTemplate(dtype=str)
        FXBlade = ParameterTemplate(dtype=str)
        OCLBlade = ParameterTemplate(dtype=str)

        FallHowFast = ParameterTemplate(dtype=str)
        FXHitGround = ParameterTemplate(dtype=str)
        OCLHitGround = ParameterTemplate(dtype=str)
        FXFinalBlowUp = ParameterTemplate(dtype=str)
        OCLFinalBlowUp = ParameterTemplate(dtype=str)

        DelayFromGroundToFinalDeath = ParameterTemplate(dtype=int)
        FinalRubbleObject = ParameterTemplate(dtype=str)
        MaxBraking = ParameterTemplate(dtype=int)
        SoundDeathLoop = ParameterTemplate(dtype=str)

    class JetSlowDeathBehavior(ModuleTemplate):
        DeathTypes = ParameterTemplate(dtype=list)
        RequiredStatus = ParameterTemplate(dtype=str)
        ExemptStatus = ParameterTemplate(dtype=str)

        DestructionDelay = ParameterTemplate(dtype=int)
        DestructionDelayVariance = ParameterTemplate(dtype=int)
        DestructionAltitude = ParameterTemplate(dtype=int)

        FXOnGroundDeath = ParameterTemplate(dtype=str)
        OCLOnGroundDeath = ParameterTemplate(dtype=str)
        FXInitialDeath = ParameterTemplate(dtype=str)
        OCLInitialDeath = ParameterTemplate(dtype=str)
        DelaySecondaryFromInitialDeath = ParameterTemplate(dtype=int)
        FXSecondary = ParameterTemplate(dtype=str)
        OCLSecondary = ParameterTemplate(dtype=str)
        DelayFinalBlowUpFromHitGround = ParameterTemplate(dtype=int)
        DeathLoopSound = ParameterTemplate(dtype=str)
        RollRate = ParameterTemplate(dtype=float)
        RollRateDelta = ParameterTemplate(dtype=str)
        PitchRate = ParameterTemplate(dtype=float)

        FallHowFast = ParameterTemplate(dtype=str)
        FXHitGround = ParameterTemplate(dtype=str)
        OCLHitGround = ParameterTemplate(dtype=str)
        FXFinalBlowUp = ParameterTemplate(dtype=str)
        OCLFinalBlowUp = ParameterTemplate(dtype=str)

    class NeutronMissileSlowDeathBehavior(_DeathBehavior):
        # RequiredStatus ?
        # ExemptStatus ?
        DestructionDelay = ParameterTemplate(dtype=int)
        DestructionDelayVariance = ParameterTemplate(dtype=int)
        DestructionAltitude = ParameterTemplate(dtype=int)

        ScorchMarkSize = ParameterTemplate(dtype=int)
        FXList = ParameterTemplate(dtype=list)

        Blast1Enabled = ParameterTemplate(dtype=bool)
        Blast1Delay = ParameterTemplate(dtype=int)
        Blast1ScorchDelay = ParameterTemplate(dtype=int)
        Blast1InnerRadius = ParameterTemplate(dtype=float)
        Blast1OuterRadius = ParameterTemplate(dtype=float)
        Blast1MaxDamage = ParameterTemplate(dtype=float)
        Blast1MinDamage = ParameterTemplate(dtype=float)
        Blast1ToppleSpeed = ParameterTemplate(dtype=float)
        Blast1PushForce = ParameterTemplate(dtype=float)

        Blast2Enabled = ParameterTemplate(dtype=bool)
        Blast2Delay = ParameterTemplate(dtype=int)
        Blast2ScorchDelay = ParameterTemplate(dtype=int)
        Blast2InnerRadius = ParameterTemplate(dtype=float)
        Blast2OuterRadius = ParameterTemplate(dtype=float)
        Blast2MaxDamage = ParameterTemplate(dtype=float)
        Blast2MinDamage = ParameterTemplate(dtype=float)
        Blast2ToppleSpeed = ParameterTemplate(dtype=float)
        Blast2PushForce = ParameterTemplate(dtype=float)

        Blast3Enabled = ParameterTemplate(dtype=bool)
        Blast3Delay = ParameterTemplate(dtype=int)
        Blast3ScorchDelay = ParameterTemplate(dtype=int)
        Blast3InnerRadius = ParameterTemplate(dtype=float)
        Blast3OuterRadius = ParameterTemplate(dtype=float)
        Blast3MaxDamage = ParameterTemplate(dtype=float)
        Blast3MinDamage = ParameterTemplate(dtype=float)
        Blast3ToppleSpeed = ParameterTemplate(dtype=float)
        Blast3PushForce = ParameterTemplate(dtype=float)

        Blast4Enabled = ParameterTemplate(dtype=bool)
        Blast4Delay = ParameterTemplate(dtype=int)
        Blast4ScorchDelay = ParameterTemplate(dtype=int)
        Blast4InnerRadius = ParameterTemplate(dtype=float)
        Blast4OuterRadius = ParameterTemplate(dtype=float)
        Blast4MaxDamage = ParameterTemplate(dtype=float)
        Blast4MinDamage = ParameterTemplate(dtype=float)
        Blast4ToppleSpeed = ParameterTemplate(dtype=float)
        Blast4PushForce = ParameterTemplate(dtype=float)

        Blast5Enabled = ParameterTemplate(dtype=bool)
        Blast5Delay = ParameterTemplate(dtype=int)
        Blast5ScorchDelay = ParameterTemplate(dtype=int)
        Blast5InnerRadius = ParameterTemplate(dtype=float)
        Blast5OuterRadius = ParameterTemplate(dtype=float)
        Blast5MaxDamage = ParameterTemplate(dtype=float)
        Blast5MinDamage = ParameterTemplate(dtype=float)
        Blast5ToppleSpeed = ParameterTemplate(dtype=float)
        Blast5PushForce = ParameterTemplate(dtype=float)

        Blast6Enabled = ParameterTemplate(dtype=bool)
        Blast6Delay = ParameterTemplate(dtype=int)
        Blast6ScorchDelay = ParameterTemplate(dtype=int)
        Blast6InnerRadius = ParameterTemplate(dtype=float)
        Blast6OuterRadius = ParameterTemplate(dtype=float)
        Blast6MaxDamage = ParameterTemplate(dtype=float)
        Blast6MinDamage = ParameterTemplate(dtype=float)
        Blast6ToppleSpeed = ParameterTemplate(dtype=float)
        Blast6PushForce = ParameterTemplate(dtype=float)

        Blast7Enabled = ParameterTemplate(dtype=bool)
        Blast7Delay = ParameterTemplate(dtype=int)
        Blast7ScorchDelay = ParameterTemplate(dtype=int)
        Blast7InnerRadius = ParameterTemplate(dtype=float)
        Blast7OuterRadius = ParameterTemplate(dtype=float)
        Blast7MaxDamage = ParameterTemplate(dtype=float)
        Blast7MinDamage = ParameterTemplate(dtype=float)
        Blast7ToppleSpeed = ParameterTemplate(dtype=float)
        Blast7PushForce = ParameterTemplate(dtype=float)

        Blast8Enabled = ParameterTemplate(dtype=bool)
        Blast8Delay = ParameterTemplate(dtype=int)
        Blast8ScorchDelay = ParameterTemplate(dtype=int)
        Blast8InnerRadius = ParameterTemplate(dtype=float)
        Blast8OuterRadius = ParameterTemplate(dtype=float)
        Blast8MaxDamage = ParameterTemplate(dtype=float)
        Blast8MinDamage = ParameterTemplate(dtype=float)
        Blast8ToppleSpeed = ParameterTemplate(dtype=float)
        Blast8PushForce = ParameterTemplate(dtype=float)

        Blast9Enabled = ParameterTemplate(dtype=bool)
        Blast9Delay = ParameterTemplate(dtype=int)
        Blast9ScorchDelay = ParameterTemplate(dtype=int)
        Blast9InnerRadius = ParameterTemplate(dtype=float)
        Blast9OuterRadius = ParameterTemplate(dtype=float)
        Blast9MaxDamage = ParameterTemplate(dtype=float)
        Blast9MinDamage = ParameterTemplate(dtype=float)
        Blast9ToppleSpeed = ParameterTemplate(dtype=float)
        Blast9PushForce = ParameterTemplate(dtype=float)

    class LifetimeUpdate(ModuleTemplate):
        MinLifetime = ParameterTemplate(dtype=int)
        MaxLifetime = ParameterTemplate(dtype=int)

    class DeletionUpdate(ModuleTemplate):
        MinLifetime = ParameterTemplate(dtype=int)
        MaxLifetime = ParameterTemplate(dtype=int)

    ###########################################################################
    # Misc Behaviors
    class AnimationSteeringUpdate(ModuleTemplate):
        MinTransitionTime = ParameterTemplate(dtype=int)

    class ProjectileStreamUpdate(ModuleTemplate):
        pass

    class DumbProjectileBehavior(ModuleTemplate):
        MaxLifespan = ParameterTemplate(dtype=int)
        TumbleRandomly = ParameterTemplate(dtype=bool)
        DetonateCallsKill = ParameterTemplate(dtype=bool)
        OrientToFlightPath = ParameterTemplate(dtype=bool)
        FirstHeight = ParameterTemplate(dtype=int)
        FirstPercentIndent = ParameterTemplate(dtype=str)  # percent
        SecondHeight = ParameterTemplate(dtype=int)
        SecondPercentIndent = ParameterTemplate(dtype=str)  # percent
        GarrisonHitKillRequiredKindOf = ParameterTemplate(dtype=list)
        GarrisonHitKillForbiddenKindOf = ParameterTemplate(dtype=list)
        GarrisonHitKillCount = ParameterTemplate(dtype=int)
        GarrisonHitKillFX = ParameterTemplate(dtype=str)
        FlightPathAdjustDistPerSecond = ParameterTemplate(dtype=float)

    class SmartBombTargetHomingUpdate(ModuleTemplate):
        CourseCorrectionScalar = ParameterTemplate(dtype=float)

    class BunkerBusterBehavior(ModuleTemplate):
        UpgradeRequired = ParameterTemplate(dtype=str)
        DetonationFX = ParameterTemplate(dtype=str)
        CrashThroughBunkerFX = ParameterTemplate(dtype=str)
        CrashThroughBunkerFXFrequency = ParameterTemplate(dtype=int)
        SeismicEffectRadius = ParameterTemplate(dtype=int)
        SeismicEffectMagnitude = ParameterTemplate(dtype=int)
        ShockwaveWeaponTemplate = ParameterTemplate(dtype=str)
        OccupantDamageWeaponTemplate = ParameterTemplate(dtype=str)

    class StickyBombUpdate(ModuleTemplate):
        GeometryBasedDamageWeapon = ParameterTemplate(dtype=str)
        GeometryBasedDamageFX = ParameterTemplate(dtype=str)

    class EnemyNearUpdate(ModuleTemplate):
        pass

    class CheckpointUpdate(ModuleTemplate):
        pass

    class AutoDepositUpdate(ModuleTemplate):
        ActualMoney = ParameterTemplate(dtype=bool)
        DepositTiming = ParameterTemplate(dtype=int)
        DepositAmount = ParameterTemplate(dtype=int)
        InitialCaptureBonus = ParameterTemplate(dtype=int)
        UpgradedBoost = ParameterTemplate(dtype=list)

    class ProductionUpdate(ModuleTemplate):
        MaxQueueEntries = ParameterTemplate(dtype=int)
        ConstructionCompleteDuration = ParameterTemplate(dtype=int)
        QuantityModifier = ParameterTemplate(dtype=list)
        DisabledTypesToProcess = ParameterTemplate(dtype=list)

        NumDoorAnimations = ParameterTemplate(dtype=int)
        DoorOpeningTime = ParameterTemplate(dtype=int)
        DoorWaitOpenTime = ParameterTemplate(dtype=int)
        DoorCloseTime = ParameterTemplate(dtype=int)

    class DefaultProductionExitUpdate(ModuleTemplate):
        UnitCreatePoint = ParameterTemplate(dtype=list)  # [x: y: z:]
        NaturalRallyPoint = ParameterTemplate(dtype=list)  # [x: y: z:]
        UseSpawnRallyPoint = ParameterTemplate(dtype=bool)

    class QueueProductionExitUpdate(ModuleTemplate):
        UnitCreatePoint = ParameterTemplate(dtype=list)  # [x: y: z:]
        NaturalRallyPoint = ParameterTemplate(dtype=list)  # [x: y: z:]
        ExitDelay = ParameterTemplate(dtype=int)
        InitialBurst = ParameterTemplate(dtype=int)
        AllowAirborneCreation = ParameterTemplate(dtype=bool)

    class SupplyCenterProductionExitUpdate(ModuleTemplate):
        UnitCreatePoint = ParameterTemplate(dtype=list)  # [x: y: z:]
        NaturalRallyPoint = ParameterTemplate(dtype=list)  # [x: y: z:]
        GrantTemporaryStealth = ParameterTemplate(dtype=int)

    class SpawnPointProductionExitUpdate(ModuleTemplate):
        SpawnPointBoneName = ParameterTemplate(dtype=str)

    class ParkingPlaceBehavior(ModuleTemplate):
        HealAmountPerSecond = ParameterTemplate(dtype=int)
        NumRows = ParameterTemplate(dtype=int)
        NumCols = ParameterTemplate(dtype=int)
        HasRunways = ParameterTemplate(dtype=bool)
        ApproachHeight = ParameterTemplate(dtype=int)
        ParkInHangars = ParameterTemplate(dtype=bool)

    class FlightDeckBehavior(ModuleTemplate):
        NumRunways = ParameterTemplate(dtype=float)
        NumSpacesPerRunway = ParameterTemplate(dtype=float)

        Runway1Spaces = ParameterTemplate(dtype=list)
        Runway1Takeoff = ParameterTemplate(dtype=list)
        Runway1Landing = ParameterTemplate(dtype=list)
        Runway1Taxi = ParameterTemplate(dtype=list)
        Runway1Creation = ParameterTemplate(dtype=list)
        Runway1CatapultSystem = ParameterTemplate(dtype=str)

        Runway2Spaces = ParameterTemplate(dtype=list)
        Runway2Takeoff = ParameterTemplate(dtype=list)
        Runway2Landing = ParameterTemplate(dtype=list)
        Runway2Taxi = ParameterTemplate(dtype=list)
        Runway2Creation = ParameterTemplate(dtype=list)
        Runway2CatapultSystem = ParameterTemplate(dtype=str)

        HealAmountPerSecond = ParameterTemplate(dtype=int)
        ApproachHeight = ParameterTemplate(dtype=int)
        LandingDeckHeightOffset = ParameterTemplate(dtype=float)
        ParkingCleanupPeriod = ParameterTemplate(dtype=int)
        HumanFollowPeriod = ParameterTemplate(dtype=int)

        PayloadTemplate = ParameterTemplate(dtype=str)
        ReplacementDelay = ParameterTemplate(dtype=int)
        DockAnimationDelay = ParameterTemplate(dtype=int)

        LaunchWaveDelay = ParameterTemplate(dtype=int)
        LaunchRampDelay = ParameterTemplate(dtype=int)
        LowerRampDelay = ParameterTemplate(dtype=int)
        CatapultFireDelay = ParameterTemplate(dtype=int)

    class RadarUpdate(ModuleTemplate):
        RadarExtendTime = ParameterTemplate(dtype=int)

    class BaseRegenerateUpdate(ModuleTemplate):
        pass

    class PowerPlantUpdate(ModuleTemplate):
        RodsExtendTime = ParameterTemplate(dtype=int)

    class OverchargeBehavior(ModuleTemplate):
        HealthPercentToDrainPerSecond = ParameterTemplate(dtype=str)  # percent
        NotAllowedWhenHealthBelowPercent = ParameterTemplate(dtype=str)  # percent

    class EMPUpdate(ModuleTemplate):
        DisabledDuration = ParameterTemplate(dtype=int)
        Lifetime = ParameterTemplate(dtype=int)
        StartColor = ParameterTemplate(dtype=list)  # @TODO [r: g: b:]
        StartFadeTime = ParameterTemplate(dtype=int)
        StartScale = ParameterTemplate(dtype=float)
        EndColor = ParameterTemplate(dtype=list)  # @TODO [r: g: b:]
        TargetScaleMin = ParameterTemplate(dtype=float)
        TargetScaleMax = ParameterTemplate(dtype=float)
        DisableFXParticleSystem = ParameterTemplate(dtype=str)
        SparksPerCubicFoot = ParameterTemplate(dtype=int)

        DoesNotAffectMyOwnBuildings = ParameterTemplate(dtype=bool)
        DoesNotAffect = ParameterTemplate(dtype=list)
        EffectRadius = ParameterTemplate(dtype=int)
        VictimForbiddenKindOf = ParameterTemplate(dtype=list)
        VictimRequiredKindOf = ParameterTemplate(dtype=list)

    class GenerateMinefieldBehavior(ModuleTemplate):
        TriggeredBy = ParameterTemplate(dtype=list)
        MineName = ParameterTemplate(dtype=str)
        GenerationFX = ParameterTemplate(dtype=str)
        DistanceAroundObject = ParameterTemplate(dtype=int)
        MinesPerSquareFoot = ParameterTemplate(dtype=int)
        GenerateOnlyOnDeath = ParameterTemplate(dtype=bool)
        BorderOnly = ParameterTemplate(dtype=bool)
        SmartBorder = ParameterTemplate(dtype=bool)
        SmartBorderSkipInterior = ParameterTemplate(dtype=bool)
        AlwaysCircular = ParameterTemplate(dtype=bool)
        RandomJitter = ParameterTemplate(dtype=int)
        SkipIfThisMuchUnderStructure = ParameterTemplate(dtype=int)
        Upgradable = ParameterTemplate(dtype=bool)
        UpgradedMineName = ParameterTemplate(dtype=str)
        UpgradedTriggeredBy = ParameterTemplate(dtype=list)

    class MinefieldBehavior(ModuleTemplate):
        DetonationWeapon = ParameterTemplate(dtype=str)
        DetonatedBy = ParameterTemplate(dtype=list)
        Regenerates = ParameterTemplate(dtype=bool)
        StopsRegenAfterCreatorDies = ParameterTemplate(dtype=bool)
        WorkersDetonate = ParameterTemplate(dtype=bool)
        CreatorDeathCheckRate = ParameterTemplate(dtype=int)
        ScootFromStartingPointTime = ParameterTemplate(dtype=int)
        NumVirtualMines = ParameterTemplate(dtype=int)
        RepeatDetonateMoveThresh = ParameterTemplate(dtype=float)
        DegenPercentPerSecondAfterCreatorDies = ParameterTemplate(dtype=str)  # percent
        CreationList = ParameterTemplate(dtype=str)

    class PropagandaTowerBehavior(ModuleTemplate):
        Radius = ParameterTemplate(dtype=float)
        DelayBetweenUpdates = ParameterTemplate(dtype=int)
        HealPercentEachSecond = ParameterTemplate(dtype=str)  # percent
        PulseFX = ParameterTemplate(dtype=str)
        AffectsSelf = ParameterTemplate(dtype=bool)
        UpgradeRequired = ParameterTemplate(dtype=str)
        UpgradedHealPercentEachSecond = ParameterTemplate(dtype=str)  # percent
        UpgradedPulseFX = ParameterTemplate(dtype=str)

    class NeutronMissileUpdate(ModuleTemplate):
        LaunchFX = ParameterTemplate(dtype=str)
        TargetFromDirectlyAbove = ParameterTemplate(dtype=int)
        RelativeSpeed = ParameterTemplate(dtype=float)
        MaxTurnRate = ParameterTemplate(dtype=int)
        ForwardDamping = ParameterTemplate(dtype=float)
        SpecialSpeedTime = ParameterTemplate(dtype=int)
        SpecialSpeedHeight = ParameterTemplate(dtype=int)
        SpecialAccelFactor = ParameterTemplate(dtype=int)
        SpecialJitterDistance = ParameterTemplate(dtype=float)
        IgnitionFX = ParameterTemplate(dtype=str)
        DistanceToTargetBeforeDiving = ParameterTemplate(dtype=int)
        DistanceToTravelBeforeTurning = ParameterTemplate(dtype=int)
        IgnitionDelay = ParameterTemplate(dtype=int)
        DeliveryDecalRadius = ParameterTemplate(dtype=int)

        class DeliveryDecal(ModuleTemplate):
            Texture = ParameterTemplate(dtype=str)
            Style = ParameterTemplate(dtype=str)
            OpacityMin = ParameterTemplate(dtype=str)  # percent
            OpacityMax = ParameterTemplate(dtype=str)  # percent
            OpacityThrobTime = ParameterTemplate(dtype=int)
            Color = ParameterTemplate(dtype=list)  # [r: g: b: a:]
            OnlyVisibleToOwningPlayer = ParameterTemplate(dtype=bool)

    class NeutronBlastBehavior(ModuleTemplate):
        BlastRadius = ParameterTemplate(dtype=int)
        AffectAirborne = ParameterTemplate(dtype=bool)
        AffectAllies = ParameterTemplate(dtype=bool)

    class RadiusDecalUpdate(ModuleTemplate):
        pass

    class HijackerUpdate(ModuleTemplate):
        ParachuteName = ParameterTemplate(dtype=str)
        AttachToTargetBone = ParameterTemplate(dtype=str)
        OffsetZ = ParameterTemplate(dtype=int)

    class RebuildHoleBehavior(ModuleTemplate):
        WorkerObjectName = ParameterTemplate(dtype=str)
        WorkerRespawnDelay = ParameterTemplate(dtype=int)
        HoleHealthRegen_PerSecond = ParameterTemplate(token="HoleHealthRegen%PerSecond", dtype=str)  # percent

    class DemoTrapUpdate(ModuleTemplate):
        DefaultProximityMode = ParameterTemplate(dtype=bool)
        DetonationWeaponSlot = ParameterTemplate(dtype=list)
        ProximityModeWeaponSlot = ParameterTemplate(dtype=list)
        ManualModeWeaponSlot = ParameterTemplate(dtype=list)
        TriggerDetonationRange = ParameterTemplate(dtype=float)
        IgnoreTargetTypes = ParameterTemplate(dtype=list)
        AutoDetonationWithFriendsInvolved = ParameterTemplate(dtype=bool)
        DetonateWhenKilled = ParameterTemplate(dtype=bool)
        DetonationWeapon = ParameterTemplate(dtype=str)

    class SupplyWarehouseCripplingBehavior(ModuleTemplate):
        SelfHealSupression = ParameterTemplate(dtype=int)
        # SelfHealingSupression = ParameterTemplate(dtype=int)
        SelfHealDelay = ParameterTemplate(dtype=int)
        SelfHealAmount = ParameterTemplate(dtype=int)

    class TechBuildingBehavior(ModuleTemplate):
        PulseFX = ParameterTemplate(dtype=str)
        PulseFXRate = ParameterTemplate(dtype=int)

    class StructureCollapseUpdate(ModuleTemplate):
        RequiredStatus = ParameterTemplate(dtype=str)
        ExemptStatus = ParameterTemplate(dtype=str)

        MinCollapseDelay = ParameterTemplate(dtype=int)
        MaxCollapseDelay = ParameterTemplate(dtype=int)
        CollapseDamping = ParameterTemplate(dtype=float)
        MaxShudder = ParameterTemplate(dtype=float)
        MinBurstDelay = ParameterTemplate(dtype=int)
        MaxBurstDelay = ParameterTemplate(dtype=int)
        BigBurstFrequency = ParameterTemplate(dtype=int)

        FXList = ParameterTemplate(dtype=list, allow_duplicates=True)
        OCL = ParameterTemplate(dtype=list, allow_duplicates=True)
        # @todo Weapon?

    class ToppleUpdate(ModuleTemplate):
        ToppleFX = ParameterTemplate(dtype=str)
        BounceFX = ParameterTemplate(dtype=str)
        StumpName = ParameterTemplate(dtype=str)
        KillWhenStartToppling = ParameterTemplate(dtype=bool)
        KillWhenFinishedToppling = ParameterTemplate(dtype=bool)
        KillStumpWhenToppled = ParameterTemplate(dtype=bool)
        ToppleLeftOrRightOnly = ParameterTemplate(dtype=bool)
        ReorientToppledRubble = ParameterTemplate(dtype=bool)
        InitialVelocityPercent = ParameterTemplate(dtype=str)  # percent
        InitialAccelPercent = ParameterTemplate(dtype=str)  # percent
        BounceVelocityPercent = ParameterTemplate(dtype=str)  # percent

    class StructureToppleUpdate(ModuleTemplate):
        MinToppleDelay = ParameterTemplate(dtype=int)
        MaxToppleDelay = ParameterTemplate(dtype=int)
        MinToppleBurstDelay = ParameterTemplate(dtype=int)
        MaxToppleBurstDelay = ParameterTemplate(dtype=int)
        StructuralIntegrity = ParameterTemplate(dtype=float)
        StructuralDecay = ParameterTemplate(dtype=float)
        TopplingFX = ParameterTemplate(dtype=str)
        ToppleDelayFX = ParameterTemplate(dtype=str)
        ToppleStartFX = ParameterTemplate(dtype=str)
        ToppleDoneFX = ParameterTemplate(dtype=str)
        CrushingFX = ParameterTemplate(dtype=str)
        CrushingWeaponName = ParameterTemplate(dtype=str)
        DamageFXTypes = ParameterTemplate(dtype=list)
        AngleFX = ParameterTemplate(dtype=list)

    class WaveGuideUpdate(ModuleTemplate):
        WaveDelay = ParameterTemplate(dtype=int)
        YSize = ParameterTemplate(dtype=float)
        LinearWaveSpacing = ParameterTemplate(dtype=float)
        WaveBendMagnitude = ParameterTemplate(dtype=float)
        WaterVelocity = ParameterTemplate(dtype=float)
        PreferredHeight = ParameterTemplate(dtype=float)
        ShorelineEffectDistance = ParameterTemplate(dtype=float)
        DamageRadius = ParameterTemplate(dtype=float)
        DamageAmount = ParameterTemplate(dtype=int)
        ToppleForce = ParameterTemplate(dtype=float)
        RandomSplashSound = ParameterTemplate(dtype=str)
        RandomSplashSoundFrequency = ParameterTemplate(dtype=int)
        BridgeParticle = ParameterTemplate(dtype=str)
        BridgeParticleAngleFudge = ParameterTemplate(dtype=float)
        LoopingSound = ParameterTemplate(dtype=str)

    class FirestormDynamicGeometryInfoUpdate(ModuleTemplate):
        InitialDelay = ParameterTemplate(dtype=int)
        InitialHeight = ParameterTemplate(dtype=float)
        InitialMajorRadius = ParameterTemplate(dtype=float)
        InitialMinorRadius = ParameterTemplate(dtype=float)
        FinalHeight = ParameterTemplate(dtype=float)
        FinalMajorRadius = ParameterTemplate(dtype=float)
        FinalMinorRadius = ParameterTemplate(dtype=float)
        TransitionTime = ParameterTemplate(dtype=int)
        ReverseAtTransitionTime = ParameterTemplate(dtype=bool)
        ScorchSize = ParameterTemplate(dtype=float)
        ParticleOffsetZ = ParameterTemplate(dtype=float)
        ParticleSystem1 = ParameterTemplate(dtype=str)
        ParticleSystem2 = ParameterTemplate(dtype=str)
        ParticleSystem3 = ParameterTemplate(dtype=str)
        ParticleSystem4 = ParameterTemplate(dtype=str)
        ParticleSystem5 = ParameterTemplate(dtype=str)
        ParticleSystem6 = ParameterTemplate(dtype=str)
        ParticleSystem7 = ParameterTemplate(dtype=str)
        ParticleSystem8 = ParameterTemplate(dtype=str)
        ParticleSystem9 = ParameterTemplate(dtype=str)
        ParticleSystem10 = ParameterTemplate(dtype=str)
        ParticleSystem11 = ParameterTemplate(dtype=str)
        ParticleSystem12 = ParameterTemplate(dtype=str)
        ParticleSystem13 = ParameterTemplate(dtype=str)
        ParticleSystem14 = ParameterTemplate(dtype=str)
        ParticleSystem15 = ParameterTemplate(dtype=str)
        ParticleSystem16 = ParameterTemplate(dtype=str)
        FXList = ParameterTemplate(dtype=str)
        DelayBetweenDamageFrames = ParameterTemplate(dtype=int)
        MaxHeightForDamage = ParameterTemplate(dtype=int)
        DamageAmount = ParameterTemplate(dtype=float)

    class PhysicsBehavior(ModuleTemplate):
        VehicleCrashesIntoNonBuildingWeaponTemplate = ParameterTemplate(dtype=str)
        VehicleCrashesIntoBuildingWeaponTemplate = ParameterTemplate(dtype=str)

        Mass = ParameterTemplate(dtype=float)
        ForwardFriction = ParameterTemplate(dtype=float)
        ZFriction = ParameterTemplate(dtype=int)
        LateralFriction = ParameterTemplate(dtype=int)
        AerodynamicFriction = ParameterTemplate(dtype=float)
        CenterOfMassOffset = ParameterTemplate(dtype=float)
        AllowBouncing = ParameterTemplate(dtype=bool)
        AllowCollideForce = ParameterTemplate(dtype=bool)
        KillWhenRestingOnGround = ParameterTemplate(dtype=bool)
        MinFallHeightForDamage = ParameterTemplate(dtype=int)
        FallHeightDamageFactor = ParameterTemplate(dtype=float)
        PitchRollYawFactor = ParameterTemplate(dtype=float)

        ShockMaxRoll = ParameterTemplate(dtype=float)
        ShockMaxPitch = ParameterTemplate(dtype=float)
        ShockMaxYaw = ParameterTemplate(dtype=float)
        ShockResistance = ParameterTemplate(dtype=float)

    class FloatUpdate(ModuleTemplate):
        Enabled = ParameterTemplate(dtype=bool)

    class TensileFormationUpdate(ModuleTemplate):
        Enabled = ParameterTemplate(dtype=bool)
        CrackSound = ParameterTemplate(dtype=str)

    class RailroadBehavior(ModuleTemplate):
        IsLocomotive = ParameterTemplate(dtype=bool)
        CrashFXTemplateName = ParameterTemplate(dtype=str)
        PathPrefixName = ParameterTemplate(dtype=str)
        CarriageTemplateName = ParameterTemplate(dtype=str, allow_duplicates=True)
        BigMetalBounceSound = ParameterTemplate(dtype=str)
        SmallMetalBounceSound = ParameterTemplate(dtype=str)
        MeatyBounceSound = ParameterTemplate(dtype=str)
        RunningGarrisonSpeedMax = ParameterTemplate(dtype=float)
        KillSpeedMin = ParameterTemplate(dtype=int)
        SpeedMax = ParameterTemplate(dtype=float)
        WaitAtStationTime = ParameterTemplate(dtype=int)
        RunningSound = ParameterTemplate(dtype=str)
        ClicketyClackSound = ParameterTemplate(dtype=str)
        WhistleSound = ParameterTemplate(dtype=str)
        Friction = ParameterTemplate(dtype=float)

        Acceleration = ParameterTemplate(dtype=float)
        Braking = ParameterTemplate(dtype=float)

    class BridgeTowerBehavior(ModuleTemplate):
        pass

    class BridgeBehavior(ModuleTemplate):
        LateralScaffoldSpeed = ParameterTemplate(dtype=float)
        VerticalScaffoldSpeed = ParameterTemplate(dtype=float)
        BridgeDieFX = ParameterTemplate(dtype=list, allow_duplicates=True)
        BridgeDieOCL = ParameterTemplate(dtype=list, allow_duplicates=True)

    class BridgeScaffoldBehavior(ModuleTemplate):
        pass

    class CommandButtonHuntUpdate(ModuleTemplate):
        pass

    class AutoFindHealingUpdate(ModuleTemplate):
        ScanRate = ParameterTemplate(dtype=int)
        ScanRange = ParameterTemplate(dtype=float)
        NeverHeal = ParameterTemplate(dtype=float)
        AlwaysHeal = ParameterTemplate(dtype=float)

    class PilotFindVehicleUpdate(ModuleTemplate):
        ScanRate = ParameterTemplate(dtype=int)
        ScanRange = ParameterTemplate(dtype=float)
        MinHealth = ParameterTemplate(dtype=float)

    class CleanupHazardUpdate(ModuleTemplate):
        ScanRate = ParameterTemplate(dtype=int)
        ScanRange = ParameterTemplate(dtype=float)
        WeaponSlot = ParameterTemplate(dtype=list)

    class PointDefenseLaserUpdate(ModuleTemplate):
        ScanRate = ParameterTemplate(dtype=int)
        ScanRange = ParameterTemplate(dtype=float)
        WeaponTemplate = ParameterTemplate(dtype=str)
        PrimaryTargetTypes = ParameterTemplate(dtype=list)
        SecondaryTargetTypes = ParameterTemplate(dtype=list)
        PredictTargetVelocityFactor = ParameterTemplate(dtype=float)

    class SlavedUpdate(ModuleTemplate):
        GuardMaxRange = ParameterTemplate(dtype=int)
        GuardWanderRange = ParameterTemplate(dtype=int)
        AttackRange = ParameterTemplate(dtype=int)
        AttackWanderRange = ParameterTemplate(dtype=int)
        ScoutRange = ParameterTemplate(dtype=int)
        ScoutWanderRange = ParameterTemplate(dtype=int)
        StayOnSameLayerAsMaster = ParameterTemplate(dtype=bool)
        DistToTargetToGrantRangeBonus = ParameterTemplate(dtype=int)

        RepairRange = ParameterTemplate(dtype=int)
        RepairMinAltitude = ParameterTemplate(dtype=float)
        RepairMaxAltitude = ParameterTemplate(dtype=float)
        RepairRatePerSecond = ParameterTemplate(dtype=float)
        RepairWhenBelowHealth_ = ParameterTemplate(token="RepairWhenBelowHealth%", dtype=str)  # percent
        RepairMinReadyTime = ParameterTemplate(dtype=int)
        RepairMaxReadyTime = ParameterTemplate(dtype=int)
        RepairMinWeldTime = ParameterTemplate(dtype=int)
        RepairMaxWeldTime = ParameterTemplate(dtype=int)
        RepairWeldingSys = ParameterTemplate(dtype=str)
        RepairWeldingFXBone = ParameterTemplate(dtype=str)

    class MobMemberSlavedUpdate(ModuleTemplate):
        MustCatchUpRadius = ParameterTemplate(dtype=int)
        NoNeedToCatchUpRadius = ParameterTemplate(dtype=int)
        Squirrelliness = ParameterTemplate(dtype=float)
        CatchUpCrisisBailTime = ParameterTemplate(dtype=int)

    class DynamicShroudClearingRangeUpdate(ModuleTemplate):
        ChangeInterval = ParameterTemplate(dtype=int)
        GrowInterval = ParameterTemplate(dtype=int)
        ShrinkDelay = ParameterTemplate(dtype=int)
        ShrinkTime = ParameterTemplate(dtype=int)
        GrowDelay = ParameterTemplate(dtype=int)
        GrowTime = ParameterTemplate(dtype=int)
        FinalVision = ParameterTemplate(dtype=float)

        class GridDecalTemplate(ModuleTemplate):
            Texture = ParameterTemplate(dtype=str)
            Style = ParameterTemplate(dtype=str)
            OpacityMin = ParameterTemplate(dtype=str)  # percent
            OpacityMax = ParameterTemplate(dtype=str)  # percent
            OpacityThrobTime = ParameterTemplate(dtype=int)
            OnlyVisibleToOwningPlayer = ParameterTemplate(dtype=bool)

            Color = ParameterTemplate(dtype=list)  # [r: g: b: a:], ignored by engine
