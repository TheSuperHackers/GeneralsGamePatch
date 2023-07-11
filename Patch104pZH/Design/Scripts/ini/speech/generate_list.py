import os
from pathlib import Path


def build_abs_path(relative_path: str) -> Path:
    this_dir = os.path.dirname(os.path.realpath(__file__))
    return Path(this_dir).joinpath(relative_path).absolute().resolve()


def run(input: Path, output: Path):
    dialog_names: list[str] = []
    file_names: list[str] = []

    with open(input) as input_file:
        lines = input_file.readlines()
        dialog_event_name = ""

        for line in lines:
            line = line.strip().split(";", 1)[0]

            if line.startswith("DialogEvent"):
                key_value_pair: list[str] = line.split(" ", 1)
                if len(key_value_pair) != 2:
                    continue

                value_str = key_value_pair[1]
                dialog_event_name = value_str.strip()

            elif line.startswith("End"):
                dialog_event_name = ""

            elif line.startswith("Filename"):
                key_value_pair: list[str] = line.split("=", 1)
                if len(key_value_pair) != 2:
                    continue

                value_str = key_value_pair[1]
                value_str = value_str.strip()
                value_list: list[str] = value_str.split(" ")

                for value in value_list:
                    if value and dialog_event_name:
                        dialog_names.append(dialog_event_name)
                        file_names.append(value)

    with open(output, "w") as output_file:
        for dialog_name, file_name in zip(dialog_names, file_names):
            output_file.write(file_name)
            for i in range(len(file_name), 15):
                output_file.write(" ")
            output_file.write(dialog_name)
            output_file.write("\n")

    return


if __name__ == "__main__":
    input1 = build_abs_path("generals_unit_descript_lin.txt")
    output1 = build_abs_path("generals_unit_descript_lin_format.txt")
    run(input1, output1)

    input2 = build_abs_path("generals_mission_dialog.txt")
    output2 = build_abs_path("generals_mission_dialog_format.txt")
    run(input2, output2)
