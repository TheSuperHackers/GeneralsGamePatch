import os
import re


def get_tga_and_textures(folder_path):
    texture_and_file = []  # List of (tga, texture)
    textures = set()  # Set of unique textures
    tga_files = set()  # Set of unique tga files
    duplicate_textures = []  # List of duplicate textures

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith('.ini'):
                if filename.lower() == 'handcreatedmappedimages.ini'.lower():
                    # Skip this file since it contains hand-created image mappings that are not relevant to the scan
                    pass
                    # continue
                file_path = os.path.join(root, filename)
                with open(file_path, 'r') as file:
                    content = file.read()
                    matches = re.findall(r"MappedImage (\S+)\s*Texture\s*=\s*(\S+)", content)
                    for txtur, tga in matches:
                        texture_and_file.append((tga, txtur))
                        if tga not in tga_files:
                            tga_files.add(tga)

                        if txtur not in textures:
                            textures.add(txtur)
                        else:
                            duplicate_textures.append((filename, txtur))

    return texture_and_file, list(textures), list(tga_files), duplicate_textures

def check_tga_in_csv(tga_files, csv_file_path, txtur_folder_path=None):
    missing_tga = []

    try:
        with open(csv_file_path, 'r') as file:
            csv_content = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {csv_file_path} was not found.")
        return []

    csv_files = set()
    for line in csv_content:
        tga_file = line.split(',')[0]
        file_name = re.sub(r'.*/', '', tga_file).lower()
        if file_name.endswith('.tga') or file_name.endswith('.dds'):
            base_name, _ = os.path.splitext(file_name)
            csv_files.add(base_name)

    if txtur_folder_path:
        for root, dirs, files in os.walk(txtur_folder_path):
            for file in files:
                if file.lower().endswith('.tga') or file.lower().endswith('.dds'):
                    base_name, _ = os.path.splitext(file.lower())
                    csv_files.add(base_name)

    for tga in tga_files:
        base_name, _ = os.path.splitext(tga.lower())
        if base_name not in csv_files:
            missing_tga.append(tga)

    return sorted(missing_tga)

def check_textures_in_wnd(wnd_folder_path, images):
    missing_textures = set()

    for root, dirs, files in os.walk(wnd_folder_path):
        for filename in files:
            if filename.lower().endswith('.wnd'):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r') as file:
                        content = file.read()
                except FileNotFoundError:
                    print(f"Error: The file {file_path} was not found.")
                    continue

                found_images = re.findall(r"IMAGE:\s*([^\s,]+)", content)

                for txtur in found_images:
                    if txtur != 'NoImage' and txtur not in images:
                        missing_textures.add(txtur)

    return sorted(list(missing_textures))


def main():
    # Select whether to scan the original or edited files.
    is_original = True

    if is_original:
        ini_folder_path = r'../../../GameFilesOriginalZH/Data/INI/MappedImages'
        wnd_folder_path = '../../../GameFilesOriginalZH/Window'
        txtur_folder_path = None
        csv_file_path = '../../../Resources/FileHashRegistry/Generals-108-GeneralsZH-104.csv'
        output_folder = 'generated_original'
    else:
        ini_folder_path = '../../../GameFilesEdited/Data/INI/MappedImages'
        wnd_folder_path = '../../../GameFilesEdited/Window'
        txtur_folder_path = '../../../GameFilesEdited/Art/Textures'
        csv_file_path = '../../../Resources/FileHashRegistry/Generals-108-GeneralsZH-104.csv'
        output_folder = 'generated_edited'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    texture_and_file, textures, tga_files, duplicate_textures = get_tga_and_textures(ini_folder_path)

    with open(os.path.join(output_folder, 'mapped_textures_list.txt'), 'w') as f:
        for filename, texture in texture_and_file:
            f.write(f"{filename} {texture}\n")

    with open(os.path.join(output_folder, 'duplicate_mapped_textures.txt'), 'w') as f:
        for filename, texture in duplicate_textures:
            f.write(f"{filename} {texture}\n")

    missing_tga = check_tga_in_csv(tga_files, csv_file_path, txtur_folder_path)

    with open(os.path.join(output_folder, 'missing_tga_files.txt'), 'w') as f:
        for tga in missing_tga:
            f.write(f"{tga}\n")

    missing_wnd_textures = check_textures_in_wnd(wnd_folder_path, textures)

    with open(os.path.join(output_folder, 'missing_wnd_textures.txt'), 'w') as f:
        for texture in missing_wnd_textures:
            f.write(f"{texture}\n")


if __name__ == "__main__":
    main()
