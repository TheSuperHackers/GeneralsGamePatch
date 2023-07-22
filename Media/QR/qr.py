import os
import qrcode
from pathlib import Path

def build_abs_path(relative_path: str) -> Path:
    dir: str = os.path.dirname(os.path.realpath(__file__))
    return Path(dir).joinpath(relative_path).absolute()


def run():
    sources: list[Path] = [
        build_abs_path("crypto.txt"),
    ]

    out_path = build_abs_path("generated")
    out_path.mkdir(exist_ok=True)

    for source in sources:
        with open(source, "r", encoding="ascii") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                code: str = line
                kvpair: list = line.split(":")
                if len(kvpair) == 2:
                    address = kvpair[1]
                else:
                    address = code
                img = qrcode.make(code, box_size = 6)
                dest: Path = build_abs_path(f"generated/{address}.png")
                img.save(str(dest))


if __name__ == "__main__":
    run()
