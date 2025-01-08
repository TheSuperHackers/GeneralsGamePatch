import os
import re
from Patch104pZH.Design.Scripts.w3d.w3dfilemanager import W3dFileManager


def read_file_content(file_path):
    """Helper function to read file content once and return it."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None


def get_mapped_images_and_textures(folder_path):
    mapped_images = set()  # Set of unique mapped images
    textures = set()  # Set of unique textures files
    mapped_images_and_textures_files = []  # List of (texture, mapped_image)
    duplicate_images = []  # List of duplicate mapped_images

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
                    for image, texture in matches:
                        mapped_images_and_textures_files.append((texture, image))
                        texture_base_name, _ = os.path.splitext(texture)
                        textures.add(texture_base_name.lower())
                        if image not in mapped_images:
                            mapped_images.add(image.lower())
                        else:
                            duplicate_images.append((filename, image))

    return mapped_images_and_textures_files, list(mapped_images), list(textures), duplicate_images


def get_textures_from_csv(csv_file_path):
    """Get all the texture files listed in the CSV and optionally from a folder."""
    textures = set()
    csv_content = read_file_content(csv_file_path)
    if not csv_content:
        return textures

    for line in csv_content.splitlines():
        texture_file = line.split(',')[0]
        file_name = re.sub(r'.*/', '', texture_file).lower()
        if file_name.endswith(('.tga', '.dds', '.w3d', '.ani')):
            base_name, _ = os.path.splitext(file_name)
            textures.add(base_name)

    return textures


def get_textures_from_folder(texture_folder_path=None):
    """Get all the texture files in a folder."""
    textures = set()
    if texture_folder_path:
        for root, _, files in os.walk(texture_folder_path):
            for file in files:
                if file.lower().endswith(('.tga', '.dds', '.psd', '.w3d', '.ani')):
                    base_name, _ = os.path.splitext(file.lower())
                    textures.add(base_name)

    return textures


def find_ini_files_with_images(images, folder_path):
    """
    Scans Igiven ini folder and returns a list of files containing at least one image from the provided images list.
    """
    image_files = []

    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith('.ini'):
                file_path = os.path.join(root, filename)
                content = read_file_content(file_path)
                if content:
                    for line in content.splitlines():
                        match = re.search(r"^\s*\S+\s*=\s*(\S+)", line)
                        if match:
                            found_image = match.group(1) or match.group(3)
                            if found_image in images:
                                image_files.append(file_path)
                                break

    return image_files


def extract_images_from_wnd(wnd_folder_path):
    images_in_wnd = set()
    for root, _, files in os.walk(wnd_folder_path):
        for filename in files:
            if filename.lower().endswith('.wnd'):
                file_path = os.path.join(root, filename)
                content = read_file_content(file_path)
                if content:
                    found_images = re.findall(r"IMAGE:\s*([^\s,]+)", content)
                    for image in found_images:
                        if image != 'NoImage':
                            images_in_wnd.add(image.lower())

    return sorted(list(images_in_wnd))


def extract_textures_from_w3d(w3d_folder_path):
    w3d_file_manager = W3dFileManager()
    textures_in_w3d_files = set()

    for root, _, files in os.walk(w3d_folder_path):
        for file in files:
            if file.lower().endswith('.w3d'):
                w3d_file_path = os.path.join(root, file)
                w3d_file_path = os.path.normpath(w3d_file_path)
                textures_in_w3d = w3d_file_manager.get_textures(w3d_file_path)
                textures_in_w3d = [os.path.splitext(texture)[0].lower() for texture in textures_in_w3d]
                textures_in_w3d_files.update(textures_in_w3d)

    return list(textures_in_w3d_files)


def extract_textures_and_images_from_ini_files(folder_path):
    regex_patterns = {
        "image": {
            "Animation2D.ini": r'^\s*Image\s*(?:=\s*([^\s;]+))?\s*(?:;.*)?$',
            "ChallengeMode.ini": r'^\s*(BioPortraitSmall|BioPortraitLarge|DefeatedImage|VictoriousImage)\s*(?:=\s*([^\s;]+))?\s*(?:;.*)?$',
            "ControlBarScheme.ini": r'^\s*(?!(?:ControlBarScheme|Side|GenBarButtonIn|GenBarButtonOn)\b)(\S+)\s+([^\s;]+)\s*(?:;.*)?$',
            "CommandButton.ini": r'^\s*ButtonImage\s*(?:=\s*([^\s;]+))?\s*(?:;.*)?$',
            # "Mouse.ini": r'^\s*Image\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$',
            "PlayerTemplate.ini": r'^\s*(ScoreScreenImage|LoadScreenImage|GeneralImage|FlagWaterMark|EnabledImage|SideIconImage|MedallionRegular|MedallionHilite|MedallionSelect)\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$',
            "Upgrade.ini": r'^\s*ButtonImage\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$',
        },
        "texture": {
            "Crate.ini": r'^\s*Model\s*(?:=\s*)?(\S+)\s*(?:;.*)?$',
            "GameData.ini": r'^\s*MoveHintName\s*(?:=\s*)?(\S+)\s*(?:;.*)?$',
            "InGameUI.ini": r'^\s*Texture\s*(?:=\s*)?(\S+)\s*(?:;.*)?$',
            "Mouse.ini": r'^\s*Texture\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$',
            "ObjectCreationList.ini": r'^\s*(ModelNames|Texture)\s*(?:=\s*)?((?:[^\s;]+\s*)+)(?:;.*)?$',
            "ParticleSystem.ini": r'^\s*ParticleName\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$',
            "Roads.ini": r'^\s*(Texture|TextureDamaged|TextureReallyDamaged|TextureBroken|BridgeModelName|BridgeModelNameDamaged|BridgeModelNameReallyDamaged|BridgeModelNameBroken)\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$',
            "Terrain.ini": r'^\s*Texture\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$',
            "Water.ini": r'^\s*(SkyTexture|WaterTexture|StandingWaterTexture)\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$',
            "Weather.ini": r'^\s*SnowTexture\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$',
        },
        "default_folder": {
            "ControlBarScheme.ini": r'^\s*(?!(?:ControlBarScheme|Side|GenBarButtonIn|GenBarButtonOn)\b)(\S+)\s+([^\s;]+)\s*(?:;.*)?$',
            "Upgrade.ini": r'^\s*ButtonImage\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$'
        },
        "object_folder": {
            "image": r'^\s*(SelectPortrait|ButtonImage)\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$',
            "texture_single": r'^\s*(Texture|Model|TrackMarks|ShadowTexture)\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$',
            "texture_double": r'^\s*(IdleAnimation|Animation)\s*(?:=\s*)?([^\s;]+\.[^\s;]+)\s*(?:;.*)?$'
        }
    }

    images = set()
    textures = set()

    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            relative_path = os.path.relpath(file_path, folder_path)

            if filename.endswith(".ini"):
                file_content = read_file_content(file_path)
                lines = file_content.splitlines()

                # Default folder
                if relative_path.startswith("Default\\"):
                    if filename in regex_patterns["default_folder"]:
                        image_pattern = regex_patterns["default_folder"][filename]
                        for line in lines:
                            matches = re.findall(image_pattern, line)
                            for match in matches:
                                if isinstance(match, tuple):
                                    match = match[1]
                                for item in match.split():
                                    images.add(item.strip().lower())
                    continue

                # Object folder
                if relative_path.startswith("Object\\"):
                    for line in lines:
                        image_pattern = regex_patterns["object_folder"]["image"]
                        texture_single_pattern = regex_patterns["object_folder"]["texture_single"]
                        texture_double_pattern = regex_patterns["object_folder"]["texture_double"]
                        matches_image = re.findall(image_pattern, line)
                        for match in matches_image:
                            if isinstance(match, tuple):
                                match = match[1]
                            for item in match.split():
                                images.add(item.strip().lower())
                        matches_texture_single = re.findall(texture_single_pattern, line)
                        for match in matches_texture_single:
                            if isinstance(match, tuple):
                                match = match[1]
                            for item in match.split():
                                textures.add(item.strip().lower())
                        matches_texture_double = re.findall(texture_double_pattern, line)
                        for match in matches_texture_double:
                            if isinstance(match, tuple):
                                match = match[1]
                            for item in match.split('.'):
                                textures.add(item.strip().lower())
                    continue

                # Main folder
                if filename in regex_patterns["image"]:
                    image_pattern = regex_patterns["image"][filename]
                    for line in lines:
                        matches = re.findall(image_pattern, line)
                        for match in matches:
                            if isinstance(match, tuple):
                                match = match[1]
                            for item in match.split():
                                images.add(item.strip().lower())

                if filename in regex_patterns["texture"]:
                    texture_pattern = regex_patterns["texture"][filename]
                    for line in lines:
                        matches = re.findall(texture_pattern, line)
                        for match in matches:
                            if isinstance(match, tuple):
                                match = match[1]
                            for item in match.split():
                                textures.add(item.strip().lower())

    return sorted(list(images)), sorted(list(textures))


def missing_textures_in_files(textures, textures_files):
    missing_textures = []
    for texture in textures:
        texture_name, _ = os.path.splitext(texture.lower())
        if texture_name not in textures_files:
            missing_textures.append(texture)

    return sorted(missing_textures)


def invalid_textures_in_w3d(textures_files, w3d_folder_path):
    w3d_file_manager = W3dFileManager()
    invalid_w3d_textures = []

    for root, _, files in os.walk(w3d_folder_path):
        for file in files:
            if file.lower().endswith('.w3d'):
                w3d_file_path = os.path.join(root, file)
                w3d_file_path = os.path.normpath(w3d_file_path)
                textures_in_w3d = w3d_file_manager.get_textures(w3d_file_path)
                invalid_textures = []

                for texture in textures_in_w3d:
                    texture_name, _ = os.path.splitext(texture.lower())
                    if texture_name not in textures_files:
                        invalid_textures.append(texture)
                if invalid_textures:
                    invalid_w3d_textures.append((file, invalid_textures))

    return invalid_w3d_textures


def invalid_given_assets_in_assets_list(assets, assets_list):
    invalid_assets = set()
    for asset in assets:
        if asset.lower() not in assets_list:
            invalid_assets.add(asset)

    return sorted(list(invalid_assets))


def unused_assets_in_assets_list(assets, assets_list):
    unused_assets = set(assets) - set(assets_list)
    return sorted(list(unused_assets))


def write_to_file(output_path, data, format_func=None):
    with open(output_path, 'w') as f:
        for item in data:
            f.write(f"{format_func(item) if format_func else item}\n")


def main():
    # Ask the user for both version and function selection
    print("Available functions to execute:")
    print("0. Run all functions")
    print("1. find_invalid_textures_and_images_from_ini_folder")
    print("2. get_mapped_images_and_textures")
    print("3. get_textures_files")
    print("4. find_images_ini")
    print("5. mapped_images_list.txt")
    print("6. duplicate_mapped_images.txt")
    print("7. missing_textures_in_files")
    print("8. invalid_images_in_wnd")
    print("9. invalid_textures_in_w3d")
    print("10. find_unused_textures_and_images_from_ini_folder")
    user_input = input(
        "Enter the version (1 for original, 2 for edited) followed by function numbers (1-9), separated by spaces: ").strip()

    # Split the input into the version choice and function choices
    user_input_parts = user_input.split()

    if len(user_input_parts) < 2:
        print("Invalid input. You must enter at least the version and one function.")
        return

    # First value is the version choice
    version_choice = user_input_parts[0]
    if version_choice == "2":
        is_original = False
        folder = 'Edited'
        print("Selected version: Edited")
    else:
        is_original = True
        folder = 'OriginalZH'
        print("Selected version: Original")

    # The rest are function choices
    function_choices = user_input_parts[1:]
    if function_choices[0] == "0":
        function_choices = [str(i) for i in range(1, 10)]

    folder_paths = {
        'images': f'../../../GameFiles{folder}/Data/INI/MappedImages',
        'ini': f'../../../GameFiles{folder}/Data/INI',
        'wnd': f'../../../GameFiles{folder}/Window',
        'w3d': f'../../../GameFiles{folder}/Art/W3D',
        'ani': f'../../../GameFiles{folder}/Data/Cursors',
        'textures': f'../../../GameFiles{folder}/Art/Textures',
        'csv': '../../../Resources/FileHashRegistry/Generals-108-GeneralsZH-104.csv'
    }

    output_folder = 'generated_original' if is_original else 'generated_edited'
    os.makedirs(output_folder, exist_ok=True)

    # Process the data
    texture_and_images, images, textures, duplicate_images = get_mapped_images_and_textures(folder_paths['images'])
    textures_files = get_textures_from_csv(folder_paths['csv']).union(
        get_textures_from_folder(folder_paths['textures'])).union(
        get_textures_from_folder(folder_paths['ani'])).union(
        get_textures_from_folder(folder_paths['w3d']))
    ini_images_scraping, ini_textures_scraping = extract_textures_and_images_from_ini_files(folder_paths['ini'])

    # Call the selected functions
    for function_choice in function_choices:
        if function_choice == "1":
            print("Calling function: find_invalid_textures_and_images_from_ini_folder")
            ini_files_scraping = extract_textures_and_images_from_ini_files(folder_paths['ini'])
            invalid_textures = invalid_given_assets_in_assets_list(ini_textures_scraping, textures_files)
            invalid_images = invalid_given_assets_in_assets_list(ini_images_scraping, images)
            write_to_file(os.path.join(output_folder, 'invalid_textures_in_ini_files.txt'), invalid_textures)
            write_to_file(os.path.join(output_folder, 'invalid_images_in_ini_files.txt'), invalid_images)
        elif function_choice == "2":
            print("Calling function: get_mapped_images_and_textures")
            texture_and_images, images, textures, duplicate_images = get_mapped_images_and_textures(
                folder_paths['images'])
        elif function_choice == "3":
            print("Calling function: get_textures_files")
            textures_files = get_textures_from_csv(folder_paths['csv']).union(
                get_textures_from_folder(folder_paths['textures']))
        elif function_choice == "4":
            print("Calling function: find_ini_files_with_images")
            print(find_ini_files_with_images(images, folder_paths['ini']))
        elif function_choice == "5":
            print("Calling function: write_to_file (mapped_images_list.txt)")
            write_to_file(os.path.join(output_folder, 'mapped_images_list.txt'), texture_and_images,
                          lambda x: f"{x[0]} {x[1]}")
        elif function_choice == "6":
            print("Calling function: write_to_file (duplicate_mapped_images.txt)")
            write_to_file(os.path.join(output_folder, 'duplicate_mapped_images.txt'), duplicate_images,
                          lambda x: f"{x[0]} {x[1]}")
        elif function_choice == "7":
            print("Calling function: missing_textures_in_files")
            missing_textures = missing_textures_in_files(textures, textures_files)
            write_to_file(os.path.join(output_folder, 'missing_textures_files.txt'), missing_textures)
        elif function_choice == "8":
            print("Calling function: invalid_images_in_wnd")
            wnd_images = extract_images_from_wnd(folder_paths['wnd'])
            invalid_wnd_images = invalid_given_assets_in_assets_list(wnd_images, images)
            write_to_file(os.path.join(output_folder, 'invalid_wnd_images.txt'), invalid_wnd_images)
        elif function_choice == "9":
            print("Calling function: invalid_textures_in_w3d")
            invalid_textures_in_w3d_files = invalid_textures_in_w3d(textures_files, folder_paths['w3d'])
            write_to_file(os.path.join(output_folder, 'invalid_textures_in_w3d_files.txt'),
                          [f"{w3d_file} {', '.join(textures)}" for w3d_file, textures in invalid_textures_in_w3d_files])
        elif function_choice == "10":
            print("Calling function: find_unused_textures_and_images_from_ini_folder")
            wnd_textures = extract_textures_from_w3d(folder_paths['w3d'])
            unused_textures = unused_assets_in_assets_list(textures_files,
                                                           ini_textures_scraping + textures + wnd_textures)
            wnd_images = extract_images_from_wnd(folder_paths['wnd'])
            unused_images = unused_assets_in_assets_list(images, ini_images_scraping + wnd_images)
            write_to_file(os.path.join(output_folder, 'unused_textures_files.txt'), unused_textures)
            write_to_file(os.path.join(output_folder, 'unused_images_files.txt'), unused_images)
        else:
            print(f"Invalid choice: {function_choice}. No function executed.")


if __name__ == "__main__":
    main()
