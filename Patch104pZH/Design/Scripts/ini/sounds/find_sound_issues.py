import os
from pathlib import Path
from sound_list import available_sounds


def build_abs_path(relative_path: str) -> Path:
    dir: str = os.path.dirname(os.path.realpath(__file__))
    return Path(dir).joinpath(relative_path).absolute()


def run():
    out_path: Path = build_abs_path("generated")
    out_path.mkdir(exist_ok=True)

    ini_paths = [
        build_abs_path("../../../../GameFilesEdited/Data/INI/SoundEffects.ini"),
        build_abs_path("../../../../GameFilesEdited/Data/INI/Voice.ini"),
    ]

    referenced_sounds: list[str] = []
    audio_events_with_duplicates: list[str] = []

    for ini_path in ini_paths:
        with open(ini_path) as ini_file:
            lines = ini_file.readlines()
            audio_event_name = ""

            for line in lines:
                line = line.strip().split(";", 1)[0]

                if line.startswith("AudioEvent"):
                    key_value_pair: list[str] = line.split(" ", 1)
                    if len(key_value_pair) != 2:
                        continue

                    value_str = key_value_pair[1]
                    audio_event_name = value_str.strip()

                if line.startswith("Sounds") or line.startswith("Attack") or line.startswith("Decay"):
                    key_value_pair: list[str] = line.split("=", 1)
                    if len(key_value_pair) != 2:
                        continue

                    value_str = key_value_pair[1]
                    value_str = value_str.strip()
                    value_list: list[str] = value_str.split(" ")
                    value_set = set()

                    for value in value_list:
                        if value:
                            referenced_sounds.append(value)
                            if value in value_set:
                                audio_events_with_duplicates.append(audio_event_name + " " + value)
                            else:
                                value_set.add(value)

    overlap = list(set(referenced_sounds) & set(available_sounds))

    invalid_referenced_sounds = list(set(referenced_sounds) - set(overlap))
    invalid_referenced_sounds.sort()
    out_txt_path = build_abs_path("generated/invalid_sounds.txt")
    with open(out_txt_path, "w", encoding="ascii") as txt_file:
        for name in invalid_referenced_sounds:
            txt_file.write(name)
            txt_file.write("\n")

    unused_available_sounds = list(set(available_sounds) - set(overlap))
    unused_available_sounds.sort()
    out_txt_path = build_abs_path("generated/unused_sounds.txt")
    with open(out_txt_path, "w", encoding="ascii") as txt_file:
        for name in unused_available_sounds:
            txt_file.write(name)
            txt_file.write("\n")

    out_txt_path = build_abs_path("generated/duplicate_sounds.txt")
    with open(out_txt_path, "w", encoding="ascii") as txt_file:
        for name in audio_events_with_duplicates:
            txt_file.write(name)
            txt_file.write("\n")

    return


if __name__ == "__main__":
    run()
