from ._common import ModuleTemplate, ParameterTemplate, SubmoduleTemplate


class ClientUpdate(SubmoduleTemplate):
    class AnimatedParticleSysBoneClientUpdate(ModuleTemplate):
        pass

    class LaserUpdate(ModuleTemplate):
        MuzzleParticleSystem = ParameterTemplate(dtype=str)
        TargetParticleSystem = ParameterTemplate(dtype=str)
        PunchThroughScalar = ParameterTemplate(dtype=float)

    class SwayClientUpdate(ModuleTemplate):
        pass

    class BeaconClientUpdate(ModuleTemplate):
        RadarPulseFrequency = ParameterTemplate(dtype=int)
        RadarPulseDuration = ParameterTemplate(dtype=int)
