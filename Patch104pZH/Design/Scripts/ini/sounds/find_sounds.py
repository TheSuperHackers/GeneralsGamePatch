from copy import copy
from enum import Enum, Flag, auto
import os
from pathlib import Path


class Priority(Enum):
    Unknown = auto()
    Lowest = auto()
    Low = auto()
    Normal = auto()
    High = auto()
    Critical = auto()

    @staticmethod
    def from_str(label: str):
        upperlabel = label.lower()
        for modifier in Priority:
            if upperlabel == modifier.name.lower():
                return modifier
        return Priority.Unknown


class Control(Flag):
    Zero = 0
    Loop = auto()
    Random = auto()
    All = auto()
    Postdelay = auto()
    Interrupt = auto()

    @staticmethod
    def from_str(label: str):
        upperlabel = label.lower()
        for modifier in Control:
            if upperlabel == modifier.name.lower():
                return modifier
        return Control.Zero


class AudioEvent:
    name: str
    priority: Priority
    controls: list[Control]

    def __init__(self):
        self.clear()

    def clear(self):
        self.name = ""
        self.priority = Priority.High
        self.controls = [Control.Random]

# AudioEvent DefaultSoundEffect
#   Volume = 100
#   Priority  = high
#   MinVolume = 40
#   Control = random
#   Limit = 4
#   MinRange = 175.00
#   MaxRange = 800.00
#   PitchShift = -0 0
#   Type = ui player
# End


def startswith_nocase(s: str, startswith: str) -> bool:
    return s.lower().startswith(startswith.lower())


def build_abs_path(relative_path: str) -> Path:
    dir: str = os.path.dirname(os.path.realpath(__file__))
    return Path(dir).joinpath(relative_path).absolute()


def find_audio_events(soundeffects_ini: Path, include_priorities: list[Priority], include_controls: list[Control]) -> list[AudioEvent]:
    events: list[str] = []

    with open(soundeffects_ini, mode="r", encoding="ascii") as file:
        lines = file.readlines()
        event = AudioEvent()

        for line in lines:
            line = line.strip()
            line = line.split(";", 1)[0]

            if startswith_nocase(line, "AudioEvent"):
                event.clear()
                key_value_pair: list[str] = line.split(" ")
                if len(key_value_pair) != 2:
                    continue
                value_str = key_value_pair[1].strip()
                event.name = value_str

            elif event.name and startswith_nocase(line, "Priority"):
                key_value_pair: list[str] = line.split("=")
                if len(key_value_pair) != 2:
                    continue
                value_str = key_value_pair[1].strip()
                event.priority = Priority.from_str(value_str)

            elif event.name and startswith_nocase(line, "Control"):
                key_value_pair: list[str] = line.split("=", 1)
                if len(key_value_pair) != 2:
                    continue
                values_str: str = key_value_pair[1].strip()
                values: list[str] = values_str.split(" ")
                event.controls = []
                for value in values:
                    control = Control.from_str(value)
                    event.controls.append(control)

            elif event.name and startswith_nocase(line, "End"):
                if event.priority in include_priorities:
                    control_overlap = list(set(event.controls) & set(include_controls))
                    if control_overlap:
                        events.append(copy(event))
                event.clear()

    return events


def dump_event_list(out_txt: Path, events: list[AudioEvent]) -> None:
    with open(out_txt, "w", encoding="ascii") as txt_file:
        event: AudioEvent
        for event in events:
            txt_file.write(f"{event.name}")
            txt_file.write("\n")


def run():
    soundeffects_ini = build_abs_path("../../../../GameFilesEdited/Data/INI/SoundEffects.ini")
    low_priority_loop_sounds_txt = build_abs_path(f"generated/low_priority_loop_sounds.txt")
    high_priority_loop_sounds_txt = build_abs_path(f"generated/high_priority_loop_sounds.txt")

    assert soundeffects_ini.is_file()

    out_path = build_abs_path("generated")
    out_path.mkdir(exist_ok=True)

    low_priority_loop_events: list[str] = find_audio_events(soundeffects_ini, [Priority.Lowest, Priority.Low], [Control.Loop])
    high_priority_loop_events: list[str] = find_audio_events(soundeffects_ini, [Priority.Lowest, Priority.Low, Priority.Normal, Priority.High], [Control.Loop])

    dump_event_list(low_priority_loop_sounds_txt, low_priority_loop_events)
    dump_event_list(high_priority_loop_sounds_txt, high_priority_loop_events)

    pass


if __name__ == "__main__":
    run()
