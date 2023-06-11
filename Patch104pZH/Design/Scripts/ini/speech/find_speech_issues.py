import os
from pathlib import Path
from speech_list import available_speech


def run():
    this_dir = os.path.dirname(os.path.realpath(__file__))

    ini_paths = [
        Path(this_dir).joinpath("../../../GameFilesOriginalZH/Data/INI/Speech.ini").absolute().resolve(),
    ]

    referenced_speech: list[str] = []

    for ini_path in ini_paths:
        with open(ini_path) as sounds_ini_file:
            lines = sounds_ini_file.readlines()

            for line in lines:
                line = line.strip().split(";", 1)[0]

                if line.startswith("Filename"):
                    key_value_pair: list[str] = line.split("=", 1)
                    if len(key_value_pair) != 2:
                        continue

                    value_str = key_value_pair[1]
                    value_str = value_str.strip()
                    value_list: list[str] = value_str.split(" ")

                    for value in value_list:
                        if value:
                            referenced_speech.append(value)

    overlap = list(set(referenced_speech) & set(available_speech))

    invalid_referenced_sounds = list(set(referenced_speech) - set(overlap))
    invalid_referenced_sounds.sort()
    out_txt_path = Path(this_dir).joinpath("invalid_speech.txt").absolute().resolve()
    with open(out_txt_path, "w") as txt_file:
        for name in invalid_referenced_sounds:
            txt_file.write(name)
            txt_file.write("\n")

    unused_available_speech = list(set(available_speech) - set(overlap))
    unused_available_speech.sort()
    out_txt_path = Path(this_dir).joinpath("unused_speech.txt").absolute().resolve()
    with open(out_txt_path, "w") as txt_file:
        for name in unused_available_speech:
            txt_file.write(name)
            txt_file.write("\n")

    return


if __name__ == "__main__":
    run()
