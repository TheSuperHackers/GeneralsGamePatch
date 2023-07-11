import os
from pathlib import Path
from speech_list import available_speech


def build_abs_path(relative_path: str) -> Path:
    dir: str = os.path.dirname(os.path.realpath(__file__))
    return Path(dir).joinpath(relative_path).absolute()


def run():
    out_path: Path = build_abs_path("generated")
    out_path.mkdir(exist_ok=True)

    ini_paths = [
        build_abs_path("../../../../GameFilesEdited/Data/INI/Speech.ini")
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
    out_txt_path = build_abs_path("generated/invalid_speech.txt")
    with open(out_txt_path, "w", encoding="ascii") as txt_file:
        for name in invalid_referenced_sounds:
            txt_file.write(name)
            txt_file.write("\n")

    unused_available_speech = list(set(available_speech) - set(overlap))
    unused_available_speech.sort()
    out_txt_path = build_abs_path("generated/unused_speech.txt")
    with open(out_txt_path, "w", encoding="ascii") as txt_file:
        for name in unused_available_speech:
            txt_file.write(name)
            txt_file.write("\n")

    return


if __name__ == "__main__":
    run()
