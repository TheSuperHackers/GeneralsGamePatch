from ._common import ModuleTemplate, ParameterTemplate, SubmoduleTemplate


class Draw(SubmoduleTemplate):
    class W3DDefaultDraw(ModuleTemplate):
        pass

    class W3DModelDraw(ModuleTemplate):
        class DefaultConditionState(ModuleTemplate):
            Model = ParameterTemplate(dtype=str, allow_clobber=True)  # @todo, bug Mammoth
            Animation = ParameterTemplate(allow_duplicates=True)
            IdleAnimation = ParameterTemplate(allow_duplicates=True)
            AnimationMode = ParameterTemplate(dtype=str)
            AnimationSpeedFactorRange = ParameterTemplate(dtype=list)

            ParticleSysBone = ParameterTemplate(validator=lambda x: len(x) == 2, allow_duplicates=True)
            WeaponRecoilBone = ParameterTemplate(validator=lambda x: len(x) == 2, allow_duplicates=True)
            WeaponFireFXBone = ParameterTemplate(validator=lambda x: len(x) == 2, allow_duplicates=True)
            WeaponMuzzleFlash = ParameterTemplate(validator=lambda x: len(x) == 2, allow_duplicates=True)
            WeaponLaunchBone = ParameterTemplate(validator=lambda x: len(x) == 2, allow_duplicates=True)
            WeaponHideShowBone = ParameterTemplate(dtype=list, allow_duplicates=True)
            ShowSubObject = ParameterTemplate(dtype=list, allow_duplicates=True)
            HideSubObject = ParameterTemplate(dtype=list, allow_duplicates=True)

            Turret = ParameterTemplate(dtype=str)
            TurretPitch = ParameterTemplate(dtype=str)
            TurretArtAngle = ParameterTemplate(dtype=int)
            TurretArtPitch = ParameterTemplate(dtype=int)

            AltTurret = ParameterTemplate(dtype=str)
            AltTurretPitch = ParameterTemplate(dtype=str)
            AltTurretArtAngle = ParameterTemplate(dtype=int)
            AltTurretArtPitch = ParameterTemplate(dtype=int)

            Flags = ParameterTemplate(dtype=list)
            TransitionKey = ParameterTemplate(dtype=str, allow_clobber=True)  # bug in CINE China
            WaitForStateToFinishIfPossible = ParameterTemplate(dtype=str)

        class ConditionState(DefaultConditionState, allow_duplicates=True):
            pass

        class TransitionState(DefaultConditionState, allow_duplicates=True):
            pass

        AliasConditionState = ParameterTemplate(dtype=list, allow_duplicates=True)  # keyword, multiple
        IgnoreConditionStates = ParameterTemplate(dtype=list)

        AnimationsRequirePower = ParameterTemplate(dtype=bool)
        MinLODRequired = ParameterTemplate(dtype=list)
        OkToChangeModelColor = ParameterTemplate(dtype=bool)
        ReceivesDynamicLights = ParameterTemplate(dtype=bool)
        ParticlesAttachedToAnimatedBones = ParameterTemplate(dtype=bool)
        ExtraPublicBone = ParameterTemplate(validator=str, allow_duplicates=True)
        ProjectileBoneFeedbackEnabledSlots = ParameterTemplate(dtype=list)

        TrackMarks = ParameterTemplate(dtype=str)
        AttachToBoneInAnotherModule = ParameterTemplate(dtype=str)

        InitialRecoilSpeed = ParameterTemplate(dtype=float)
        MaxRecoilDistance = ParameterTemplate(dtype=float)
        RecoilSettleSpeed = ParameterTemplate(dtype=float)
        RecoilDamping = ParameterTemplate(dtype=float)

    class W3DScienceModelDraw(W3DModelDraw):
        RequiredScience = ParameterTemplate(dtype=str)

    class W3DTruckDraw(W3DModelDraw):
        RotationDamping = ParameterTemplate(dtype=float)
        TrailerRotationMultiplier = ParameterTemplate(dtype=float)
        TrailerBone = ParameterTemplate(dtype=str)
        CabRotationMultiplier = ParameterTemplate(dtype=float)
        CabBone = ParameterTemplate(dtype=str)

        PowerslideRotationAddition = ParameterTemplate(dtype=float)
        TireRotationMultiplier = ParameterTemplate(dtype=float)
        MidRightMidTireBone = ParameterTemplate(dtype=str)
        MidLeftMidTireBone = ParameterTemplate(dtype=str)
        MidRightRearTireBone = ParameterTemplate(dtype=str)
        MidLeftRearTireBone = ParameterTemplate(dtype=str)
        MidRightFrontTireBone = ParameterTemplate(dtype=str)
        MidLeftFrontTireBone = ParameterTemplate(dtype=str)
        RightRearTireBone = ParameterTemplate(dtype=str)
        LeftRearTireBone = ParameterTemplate(dtype=str)
        RightFrontTireBone = ParameterTemplate(dtype=str)
        LeftFrontTireBone = ParameterTemplate(dtype=str)

        PowerslideSpray = ParameterTemplate(dtype=str)
        DirtSpray = ParameterTemplate(dtype=str)
        Dust = ParameterTemplate(dtype=str)

    class W3DTankDraw(W3DModelDraw):
        TreadDriveSpeedFraction = ParameterTemplate(dtype=float)
        TreadPivotSpeedFraction = ParameterTemplate(dtype=float)
        TreadAnimationRate = ParameterTemplate(dtype=float)

        TreadDebrisLeft = ParameterTemplate(dtype=str)  # broken in W3DTankTruckDraw
        TreadDebrisRight = ParameterTemplate(dtype=str)  # broken in W3DTankTruckDraw

        InitialRecoilSpeed = ParameterTemplate(dtype=float)
        MaxRecoilDistance = ParameterTemplate(dtype=float)
        RecoilDamping = ParameterTemplate(dtype=float)
        RecoilSettleSpeed = ParameterTemplate(dtype=float)

    class W3DTankTruckDraw(W3DTankDraw, W3DTruckDraw):
        pass

    class W3DOverlordTankDraw(W3DModelDraw):
        TreadDriveSpeedFraction = ParameterTemplate(dtype=float)
        TreadPivotSpeedFraction = ParameterTemplate(dtype=float)
        TreadAnimationRate = ParameterTemplate(dtype=float)
        TreadDebrisLeft = ParameterTemplate(dtype=str)
        TreadDebrisRight = ParameterTemplate(dtype=str)

    class W3DOverlordTruckDraw(W3DTruckDraw):  # W3DModelDraw?
        pass

    class W3DOverlordAircraftDraw(W3DModelDraw):
        pass

    class W3DDependencyModelDraw(W3DModelDraw):
        AttachToBoneInContainer = ParameterTemplate(dtype=str)

    class W3DSupplyDraw(W3DModelDraw):
        SupplyBonePrefix = ParameterTemplate(dtype=str)

    class W3DPoliceCarDraw(W3DTruckDraw):  # W3DModelDraw?
        pass

    class W3DPropDraw(W3DModelDraw):
        ModelName = ParameterTemplate(dtype=str)

    class W3DDebrisDraw(ModuleTemplate):
        pass

    class W3DTreeDraw(ModuleTemplate):
        ModelName = ParameterTemplate(dtype=str)
        TextureName = ParameterTemplate(dtype=str)
        MinimumToppleSpeed = ParameterTemplate(dtype=str)
        DoTopple = ParameterTemplate(dtype=bool)
        DoShadow = ParameterTemplate(dtype=bool, allow_clobber=True)  # @todo, bug Generic Tree
        ToppleFX = ParameterTemplate(dtype=str)
        BounceFX = ParameterTemplate(dtype=str)
        KillWhenFinishedToppling = ParameterTemplate(dtype=bool)
        SinkDistance = ParameterTemplate(dtype=float)
        SinkTime = ParameterTemplate(dtype=int)
        DarkeningFactor = ParameterTemplate(dtype=int)
        MoveInwardTime = ParameterTemplate(dtype=int)
        MoveOutwardTime = ParameterTemplate(dtype=int)
        MoveOutwardDistanceFactor = ParameterTemplate(dtype=float)

    class W3DTracerDraw(ModuleTemplate):
        pass

    class W3DLaserDraw(ModuleTemplate):
        Texture = ParameterTemplate(dtype=str)
        NumBeams = ParameterTemplate(dtype=int)
        InnerBeamWidth = ParameterTemplate(dtype=float)
        OuterBeamWidth = ParameterTemplate(dtype=float)
        InnerColor = ParameterTemplate(dtype=list)  # @todo, rgba
        OuterColor = ParameterTemplate(dtype=list)  # @todo, rgba
        MaxIntensityLifetime = ParameterTemplate(dtype=int)
        FadeLifetime = ParameterTemplate(dtype=int)
        Tile = ParameterTemplate(dtype=bool)
        Segments = ParameterTemplate(dtype=int)
        SegmentOverlapRatio = ParameterTemplate(dtype=float)
        ArcHeight = ParameterTemplate(dtype=float)
        TilingScalar = ParameterTemplate(dtype=float)

        ScrollRate = ParameterTemplate(dtype=float)

    class W3DProjectileStreamDraw(ModuleTemplate):
        Texture = ParameterTemplate(dtype=str)
        Width = ParameterTemplate(dtype=float)
        TileFactor = ParameterTemplate(dtype=float)
        ScrollRate = ParameterTemplate(dtype=float)
        MaxSegments = ParameterTemplate(dtype=int)

    class W3DRopeDraw(ModuleTemplate):
        pass
