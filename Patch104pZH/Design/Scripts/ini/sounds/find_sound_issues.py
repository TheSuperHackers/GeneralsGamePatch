import os
from pathlib import Path
from sound_list import available_sounds


def run():
    this_dir = os.path.dirname(os.path.realpath(__file__))

    ini_paths = [
        Path(this_dir).joinpath("../../../GameFilesOriginalZH/Data/INI/SoundEffects.ini").absolute().resolve(),
        Path(this_dir).joinpath("../../../GameFilesOriginalZH/Data/INI/Voice.ini").absolute().resolve(),
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
    out_txt_path = Path(this_dir).joinpath("invalid_sounds.txt").absolute().resolve()
    with open(out_txt_path, "w") as txt_file:
        for name in invalid_referenced_sounds:
            txt_file.write(name)
            txt_file.write("\n")

    unused_available_sounds = list(set(available_sounds) - set(overlap))
    unused_available_sounds.sort()
    out_txt_path = Path(this_dir).joinpath("unused_sounds.txt").absolute().resolve()
    with open(out_txt_path, "w") as txt_file:
        for name in unused_available_sounds:
            txt_file.write(name)
            txt_file.write("\n")

    out_txt_path = Path(this_dir).joinpath("duplicate_sounds.txt").absolute().resolve()
    with open(out_txt_path, "w") as txt_file:
        for name in audio_events_with_duplicates:
            txt_file.write(name)
            txt_file.write("\n")

    return


if __name__ == "__main__":
    run()
