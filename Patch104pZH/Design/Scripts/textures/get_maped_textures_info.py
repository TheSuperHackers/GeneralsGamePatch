import os
import re

def read_file_content(file_path):
    """Helper function to read file content once and return it."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None

def get_tga_and_textures(folder_path):
    texture_and_file = []  # List of (tga, texture)
    textures = set()  # Set of unique textures
    tga_files = set()  # Set of unique tga files
    duplicate_textures = []  # List of duplicate textures

    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith('.ini'):
                if filename.lower() == 'handcreatedmappedimages.ini'.lower():
                    # Skip this file since it contains hand-created image mappings that are not relevant to the scan
                    pass
                    # continue
                file_path = os.path.join(root, filename)
                content = read_file_content(file_path)
                if content:
                    matches = re.findall(r"MappedImage (\S+)\s*Texture\s*=\s*(\S+)", content)
                    for texture, tga in matches:
                        texture_and_file.append((tga, texture))
                        tga_files.add(tga)
                        if texture not in textures:
                            textures.add(texture)
                        else:
                            duplicate_textures.append((filename, texture))

    return texture_and_file, list(textures), list(tga_files), duplicate_textures

def get_csv_files(csv_file_path, texture_folder_path=None):
    """Get all the texture files listed in the CSV and optionally from a folder."""
    textures_in_csv = set()
    csv_content = read_file_content(csv_file_path)
    if not csv_content:
        return textures_in_csv

    for line in csv_content.splitlines():
        tga_file = line.split(',')[0]
        file_name = re.sub(r'.*/', '', tga_file).lower()
        if file_name.endswith(('.tga', '.dds')):
            base_name, _ = os.path.splitext(file_name)
            textures_in_csv.add(base_name)

    if texture_folder_path:
        for root, _, files in os.walk(texture_folder_path):
            for file in files:
                if file.lower().endswith(('.tga', '.dds', '.psd')):
                    base_name, _ = os.path.splitext(file.lower())
                    textures_in_csv.add(base_name)

    return textures_in_csv

def check_tga_in_csv(tga_files, textures_in_csv):
    missing_tga = []
    for tga in tga_files:
        base_name, _ = os.path.splitext(tga.lower())
        if base_name not in textures_in_csv:
            missing_tga.append(tga)

    return sorted(missing_tga)

def check_textures_in_wnd(wnd_folder_path, textures_list):
    missing_textures = set()
    for root, _, files in os.walk(wnd_folder_path):
        for filename in files:
            if filename.lower().endswith('.wnd'):
                file_path = os.path.join(root, filename)
                content = read_file_content(file_path)
                if content:
                    found_textures = re.findall(r"IMAGE:\s*([^\s,]+)", content)
                    for texture in found_textures:
                        if texture != 'NoImage' and texture not in textures_list:
                            missing_textures.add(texture)

    return sorted(list(missing_textures))


def main():
    # Select whether to scan the original or edited files.
    is_original = True

    folder_paths = {
        'ini': '../../../GameFilesOriginalZH/Data/INI/MappedImages' if is_original else '../../../GameFilesEdited/Data/INI/MappedImages',
        'wnd': '../../../GameFilesOriginalZH/Window' if is_original else '../../../GameFilesEdited/Window',
        'w3d': 'D:\\Rufus\\Art\\W3D' if is_original else '../../../GameFilesEdited/Art/W3D',
        'textures': None if is_original else '../../../GameFilesEdited/Art/Textures',
        'csv': '../../../Resources/FileHashRegistry/Generals-108-GeneralsZH-104.csv'
    }

    output_folder = 'generated_original' if is_original else 'generated_edited'
    os.makedirs(output_folder, exist_ok=True)

    texture_and_file, textures, tga_files, duplicate_textures = get_tga_and_textures(folder_paths['ini'])
    textures_in_csv = get_csv_files(folder_paths['csv'], folder_paths['textures'])

    write_to_file(os.path.join(output_folder, 'mapped_textures_list.txt'), texture_and_file, lambda x: f"{x[0]} {x[1]}")
    write_to_file(os.path.join(output_folder, 'duplicate_mapped_textures.txt'), duplicate_textures, lambda x: f"{x[0]} {x[1]}")

    missing_tga = check_tga_in_csv(tga_files, textures_in_csv)
    write_to_file(os.path.join(output_folder, 'missing_tga_files.txt'), missing_tga)

    missing_wnd_textures = check_textures_in_wnd(folder_paths['wnd'], textures)
    write_to_file(os.path.join(output_folder, 'missing_wnd_textures.txt'), missing_wnd_textures)


if __name__ == "__main__":
    main()
