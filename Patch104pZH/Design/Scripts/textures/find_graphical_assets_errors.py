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


def get_mapped_images(folder_path):
    textures_files_mapped_images_dictionary = {}  # Dictionary to map texture files to their mapped images
    mapped_images = set()  # Set of unique mapped images
    textures = set()  # Set of unique texture files
    duplicate_images = []  # List of duplicate mapped images

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
                    matches = re.findall(r"MappedImage (\S+)\s*(?:;.*?\n)?\s*Texture\s*=\s*(\S+)", content)
                    for image, texture in matches:
                        textures_files_mapped_images_dictionary.setdefault(texture, []).append(image)
                        texture_base_name, _ = os.path.splitext(texture)
                        textures.add(texture_base_name)
                        if image not in mapped_images:
                            mapped_images.add(image)
                        else:
                            duplicate_images.append((filename, image))

    return textures_files_mapped_images_dictionary, list(mapped_images), list(textures), duplicate_images


def get_textures_models_from_csv(csv_file_path, languages):
    """Get all the texture and model files listed in the CSV,
     excluding paths starting with 'maps' and paths containing language names."""
    textures = set()
    models = set()
    csv_content = read_file_content(csv_file_path)
    if not csv_content:
        return textures, models

    for line in csv_content.splitlines():
        texture_file = line.split(',')[0]

        if (texture_file.lower().startswith("maps/") or
                any(language.lower() in texture_file.lower() for language in languages)):
            continue

        file_name = re.sub(r'.*/', '', texture_file)
        if file_name.lower().endswith(('.tga', '.dds', '.w3d')):
            base_name, ext = os.path.splitext(file_name)
            if ext.lower() == '.w3d':
                models.add(base_name)
            else:
                textures.add(base_name)

    return textures, models


def get_files_from_folder(files_folder_path=None):
    """Get all the texture files in a folder."""
    files = set()
    if files_folder_path:
        for root, _, files_list in os.walk(files_folder_path):
            for file in files_list:
                if file.lower().endswith(('.tga', '.dds', '.psd', '.w3d')):
                    base_name, _ = os.path.splitext(file)
                    files.add(base_name)

    return files


def extract_images_from_wnd_files(wnd_folder_path):
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
                            images_in_wnd.add(image)

    return sorted(list(images_in_wnd))


def extract_textures_from_w3d_files(w3d_folder_path):
    w3d_file_manager = W3dFileManager()
    textures_in_w3d_files = set()

    for root, _, files in os.walk(w3d_folder_path):
        for file in files:
            if file.lower().endswith('.w3d'):
                w3d_file_path = os.path.join(root, file)
                w3d_file_path = os.path.normpath(w3d_file_path)
                textures_in_w3d = w3d_file_manager.get_textures(w3d_file_path)
                textures_in_w3d = [os.path.splitext(texture)[0] for texture in textures_in_w3d]
                textures_in_w3d_files.update(textures_in_w3d)

    return list(textures_in_w3d_files)


def extract_graphical_assets_from_ini_files(folder_path):
    regex_patterns = {
        "image": {
            "Animation2D.ini": r'^\s*Image\s*(?:=\s*([^\s;]+))?\s*(?:;.*)?$',
            "ChallengeMode.ini": r'^\s*(BioPortraitSmall|BioPortraitLarge|DefeatedImage|VictoriousImage)\s*(?:=\s*([^\s;]+))?\s*(?:;.*)?$',
            "ControlBarScheme.ini": r'^\s*(?!;)(?!(?:ControlBarScheme|AnimatingPart|CHALLENGE|End|ImagePart|Side|Layer)\b)(\S+)\s+([^\s;]+)\s*(?:;.*)?$',
            "CommandButton.ini": r'^\s*ButtonImage\s*(?:=\s*([^\s;]+))?\s*(?:;.*)?$',
            # "Mouse.ini": r'^\s*Image\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$',
            "PlayerTemplate.ini": r'^\s*(ScoreScreenImage|LoadScreenImage|GeneralImage|FlagWaterMark|EnabledImage|SideIconImage|MedallionRegular|MedallionHilite|MedallionSelect)\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$',
            "Upgrade.ini": r'^\s*ButtonImage\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$',
        },
        "texture": {
            "InGameUI.ini": r'^\s*Texture\s*(?:=\s*)?(\S+)\s*(?:;.*)?$',
            # "Mouse.ini": r'^\s*Texture\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$',
            "ObjectCreationList.ini": r'^\s*Texture\s*(?:=\s*)?((?:[^\s;]+\s*)+)(?:;.*)?$',
            "ParticleSystem.ini": r'^\s*ParticleName\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$',
            "Roads.ini": r'^\s*(Texture|TextureDamaged|TextureReallyDamaged|TextureBroken)\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$',
            "Terrain.ini": r'^\s*Texture\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$',
            "Water.ini": r'^\s*(SkyTexture|WaterTexture|StandingWaterTexture)\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$',
            "Weather.ini": r'^\s*SnowTexture\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$',
        },
        "model": {
            "Crate.ini": r'^\s*Model\s*(?:=\s*)?(\S+)\s*(?:;.*)?$',
            "GameData.ini": r'^\s*MoveHintName\s*(?:=\s*)?(\S+)\s*(?:;.*)?$',
            "ObjectCreationList.ini": r'^\s*ModelNames\s*(?:=\s*)?((?:[^\s;]+\s*)+)(?:;.*)?$',
            "Roads.ini": r'^\s*(BridgeModelName|BridgeModelNameDamaged|BridgeModelNameReallyDamaged|BridgeModelNameBroken)\s*(?:=\s*)?(\S+)\s*(?:;.*)?$',

        },
        "default_folder": {
            "ControlBarScheme.ini": r'^\s*(?!;)(?!(?:ControlBarScheme|AnimatingPart|CHALLENGE|End|ImagePart|Side|Layer)\b)(\S+)\s+([^\s;]+)\s*(?:;.*)?$',
            "Upgrade.ini": r'^\s*ButtonImage\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$'
        },
        "object_folder": {
            "image": r'^\s*(SelectPortrait|ButtonImage)\s*(?:=\s*)?([^\s;]+)\s*(?:;.*)?$',
            "texture": r'^\s*(Texture|TrackMarks|ShadowTexture)\s*(?:=\s*)?([^.\s;]+)(?:\.[^\s;]+)?\s*(?:;.*)?$',
            "model_signal": r'^\s*Model\s*(?:=\s*)?(\S+)\s*(?:;.*)?$',
            "model_double": r'^\s*(IdleAnimation|Animation)\s*(?:=\s*)?([^\s;]+\.[^\s;]+)(?:\s+.*)?(?:;.*)?$'
        }
    }

    images = set()
    textures = set()
    models = set()

    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            relative_path = os.path.relpath(file_path, folder_path)

            if filename.lower().endswith(".ini"):
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
                                    images.add(item.strip())
                    continue

                # Object folder
                if relative_path.startswith("Object\\"):
                    for line in lines:
                        image_pattern = regex_patterns["object_folder"]["image"]
                        texture_pattern = regex_patterns["object_folder"]["texture"]
                        model_signal_pattern = regex_patterns["object_folder"]["model_signal"]
                        model_double_pattern = regex_patterns["object_folder"]["model_double"]

                        matches_image = re.findall(image_pattern, line)
                        for match in matches_image:
                            if isinstance(match, tuple):
                                match = match[1]
                            for item in match.split():
                                images.add(item.strip())
                        matches_texture_single = re.findall(texture_pattern, line)
                        for match in matches_texture_single:
                            if isinstance(match, tuple):
                                match = match[1]
                            for item in match.split():
                                textures.add(item.strip())
                        matches_model_signal = re.findall(model_signal_pattern, line)
                        for match in matches_model_signal:
                            if isinstance(match, tuple):
                                match = match[1]
                            for item in match.split():
                                models.add(item.strip())
                        matches_model_double = re.findall(model_double_pattern, line)
                        for match in matches_model_double:
                            if isinstance(match, tuple):
                                match = match[1]
                            for item in match.split('.'):
                                models.add(item.strip())
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
                                images.add(item.strip())

                if filename in regex_patterns["texture"]:
                    texture_pattern = regex_patterns["texture"][filename]
                    for line in lines:
                        matches = re.findall(texture_pattern, line)
                        for match in matches:
                            if isinstance(match, tuple):
                                match = match[1]
                            for item in match.split():
                                textures.add(item.strip())
                if filename in regex_patterns["model"]:
                    model_pattern = regex_patterns["model"][filename]
                    for line in lines:
                        matches = re.findall(model_pattern, line)
                        for match in matches:
                            if isinstance(match, tuple):
                                match = match[1]
                            for item in match.split():
                                models.add(item.strip())

    return sorted(list(images)), sorted(list(textures)), sorted(list(models))


def check_strings_in_dat_file(strings, file_path):
    not_found_strings = []
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            lower_content = content.lower()

            for string in strings:
                lower_byte_string = string.lower().encode('ascii')
                if lower_byte_string not in lower_content:
                    not_found_strings.append(string)
    except FileNotFoundError:
        print(f'File not found: {file_path}')
        return []
    except Exception as e:
        print(f'An error occurred: {e}')
        return []

    return not_found_strings


def analyze_language_graphical_assets(base_folder, languages, language_assets, output_folder,
                           ini_textures_scraping, ini_models_scraping, mapped_textures, textures_files,
                           original_base_folder_paths=None):
    os.makedirs(os.path.join(output_folder, 'languages'), exist_ok=True)

    for language in languages:
        output_file_path = os.path.join(output_folder, 'languages', f'{language}.txt')

        textures_path = os.path.join(base_folder, 'Data', language, 'Art', 'Textures')
        w3d_path = os.path.join(base_folder, 'Data', language, 'Art', 'W3D')

        edited_textures_path = os.path.join(original_base_folder_paths, 'Data', language, 'Art', 'Textures') if original_base_folder_paths else None
        edited_w3d_path = os.path.join(original_base_folder_paths, 'Data', language, 'Art', 'W3D') if original_base_folder_paths else None

        with open(output_file_path, 'w') as f:
            f.write(f"Report for language: {language}\n\n")

            # Collect assets
            language_textures = get_files_from_folder(textures_path)
            language_models = get_files_from_folder(w3d_path)
            if original_base_folder_paths:
                language_textures = language_textures.union(get_files_from_folder(edited_textures_path))
                language_models = language_models.union(get_files_from_folder(edited_w3d_path))

            # ============= Unused assets (INI) ==============
            f.write("============== Unused Textures (INI) ==============\n\n")
            unused_textures = unused_assets_in_assets_list(language_textures,
                                                           language_assets['textures_mapped_images'] + ini_textures_scraping + mapped_textures)

            if unused_textures:
                for texture in unused_textures:
                     f.write(f"{texture}\n")
            else:
                f.write("None\n")

            f.write("\n============== Unused Models (INI) ==============\n\n")
            unused_models = unused_assets_in_assets_list(language_models, language_assets['models'] + ini_models_scraping)
            if unused_models:
                for model in unused_models:
                    f.write(f"{model}\n")
            else:
                f.write("None\n")


            # =============== Invalid Language Assets ================
            f.write("\n============== Invalid Models Assets ==============\n\n")
            invalid_models = invalid_given_assets_in_assets_list(language_assets['models'], language_models)
            if invalid_models:
                for model in invalid_models:
                    f.write(f"{model}\n")
            else:
                f.write("None\n")

            f.write("\n============== Invalid Textures in Mapped Images Assets ==============\n\n")
            invalid_textures_mapped = invalid_given_assets_in_assets_list(language_assets['textures_mapped_images'], language_textures)
            if invalid_textures_mapped:
                for texture in invalid_textures_mapped:
                    f.write(f"{texture}\n")
            else:
                f.write("None\n")


            # ============= Invalid textures in W3D ==============
            f.write("\n============== Invalid Textures in W3D Files ==============\n\n")
            invalid_w3d_textures = invalid_textures_in_w3d(textures_files.union(language_textures), w3d_path)
            if invalid_w3d_textures:
                for w3d_file, invalid_textures in invalid_w3d_textures:
                    f.write(f"{w3d_file}: {', '.join(invalid_textures)}\n")
            else:
                f.write("None\n")


def invalid_textures_in_w3d(textures_files, w3d_folder_path):
    w3d_file_manager = W3dFileManager()
    invalid_w3d_textures = []

    textures_files_lower = {texture.lower() for texture in textures_files}

    for root, _, files in os.walk(w3d_folder_path):
        for file in files:
            if file.lower().endswith('.w3d'):
                w3d_file_path = os.path.join(root, file)
                w3d_file_path = os.path.normpath(w3d_file_path)
                textures_in_w3d = w3d_file_manager.get_textures(w3d_file_path)
                invalid_textures = []

                for texture in textures_in_w3d:
                    texture_name, _ = os.path.splitext(texture)
                    if texture_name.lower() not in textures_files_lower:
                        invalid_textures.append(texture)
                if invalid_textures:
                    invalid_w3d_textures.append((file, invalid_textures))

    return invalid_w3d_textures


def invalid_given_assets_in_assets_list(assets, assets_list):
    invalid_assets = set()

    # Convert all assets_list to lowercase for case-insensitive comparison
    assets_list_lower = {asset.lower() for asset in assets_list}

    for asset in assets:
        if asset.lower() not in assets_list_lower:
            invalid_assets.add(asset)

    return sorted(list(invalid_assets))


def unused_assets_in_assets_list(assets, assets_list):
    # Convert both lists to lowercase sets for case-insensitive comparison
    assets_lower = {asset.lower() for asset in assets}
    assets_list_lower = {asset.lower() for asset in assets_list}

    unused_assets = assets_lower - assets_list_lower
    unused_assets_original_case = [asset for asset in assets if asset.lower() in unused_assets]

    return sorted(unused_assets_original_case)


def write_to_file(output_path, data, format_func=None, warning=False):
    warning_message = '''
=================================================================================================
# WARNING: The list of unused mapped images may not be entirely accurate!                       #
# Many of the "unused" images are actually used, but are assembled by combining                 #
# multiple string components (e.g., "Rank_" + "Colonel" + "_USA", "Rank" + "Major" + "_GLA").   #
# These combined names might not appear as complete strings in the executable file,             #
# causing them to be falsely flagged as unused.                                                 #
# Manual review of the list is required to verify the actual usage of some images.              # 
=================================================================================================

'''

    with open(output_path, 'w') as f:
        f.write(warning_message) if warning else None
        for item in data:
            f.write(f"{format_func(item) if format_func else item}\n")


def main():
    # Ask the user for both version and function selection
    print("Available functions to execute:")
    print("0. Run all functions")
    print("1. find_invalid_models_textures_images_from_ini_folder")
    print("2. get_mapped_images_and_textures_from_MappedImages_folder")
    print("3. find_duplicate_mapped_images.txt")
    print("4. invalid_textures_in_MappedImages_folder")
    print("5. invalid_images_in_wnd_files")
    print("6. invalid_textures_in_w3d_files")
    print("7. find_unused_models_and_textures_and_images_in_game_files")
    print("8. analyze_language_files")

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
        print("Selected version: Edited")
    else:
        is_original = True
        print("Selected version: Original")

    # The rest are function choices
    function_choices = user_input_parts[1:]
    if function_choices[0] == "0":
        function_choices = [str(i) for i in range(1, 9)]

    edited_folder_path = '../../../GameFilesEdited'
    edited_folder_paths = {
        'images': f'{edited_folder_path}/Data/INI/MappedImages',
        'ini': f'{edited_folder_path}/Data/INI',
        'wnd': f'{edited_folder_path}/Window',
        'w3d': f'{edited_folder_path}/Art/W3D',
        'ani': f'{edited_folder_path}/Data/Cursors',
        'textures': f'{edited_folder_path}/Art/Textures',
        'csv': '../../../Resources/FileHashRegistry/Generals-108-GeneralsZH-104.csv',
        'dat': r"C:\Program Files (x86)\Steam\steamapps\common\Command & Conquer Generals - Zero Hour\game.dat"
    }

    original_folder_path = '../../../GameFilesOriginal'
    original_folder_paths = {
        'images': f'{original_folder_path}/Data/INI/MappedImages',
        'ini': f'{original_folder_path}/Data/INI',
        'wnd': f'{original_folder_path}/Window',
        'w3d': f'{original_folder_path}/Art/W3D',
        'ani': f'{original_folder_path}/Data/Cursors',
        'textures': f'{original_folder_path}/Art/Textures',
        'csv': '../../../Resources/FileHashRegistry/Generals-108-GeneralsZH-104.csv',
        'dat': r"C:\Program Files (x86)\Steam\steamapps\common\Command & Conquer Generals - Zero Hour\game.dat"
    }

    folder_paths = original_folder_paths if is_original else edited_folder_paths

    output_folder = 'generated_original' if is_original else 'generated_edited'
    os.makedirs(output_folder, exist_ok=True)

    languages = [
        "Brazilian",
        "Chinese",
        "English",
        "French",
        "German",
        "Italian",
        "Korean",
        "Polish",
        "Spanish"
    ]

    # Process the data
    textures_files_mapped_images_dictionary, images, mapped_textures, duplicate_images = get_mapped_images(
        folder_paths['images'])
    textures, models = get_textures_models_from_csv(folder_paths['csv'], languages)
    textures_files = textures.union(
        get_files_from_folder(folder_paths['textures']))
    models_files = models.union(get_files_from_folder(folder_paths['w3d']))
    ini_images_scraping, ini_textures_scraping, ini_models_scraping = extract_graphical_assets_from_ini_files(
        folder_paths['ini'])

    language_assets = {
            "models": ["UITER_Local_A1", "UITER_Local_A2", "UITER_Local_A4", "UITER_Local_A5", "UITRST_SKNP", "UITer_Local_SKL", "UITer_Local_SKN"],
            "textures_mapped_images": ["Defeated", "GameOver", "SAUserInterface512_004", "SAUserInterface512_005", "SCGenChallengeSelect512_001",
                                    "SCGenChallengeWinLoss512_001", "SCGenChallengeWinLoss512_002", "SCGenChallengeWinLoss512_003",
                                    "SCGenChallengeWinLoss512_004", "SCGenChallengeWinLoss512_005", "SCGenChallengeWinLoss512_006",
                                    "SCGenChallengeWinLoss512_007", "SCGenChallengeWinLoss512_008", "SCGenChallengeWinLoss512_009",
                                    "SCGenChallengeWinLoss512_010", "SCGenChallengeWinLoss512_011", "SCGenChallengeWinLoss512_012",
                                    "SCGenChallengeWinLoss512_013", "SCGenChallengeWinLoss512_014", "SCGenChallengeWinLoss512_015",
                                    "SCGenChallengeWinLoss512_016", "SCGenChallengeWinLoss512_017", "SCGenChallengeWinLoss512_018",
                                    "SCGenChallengeWinLoss512_019", "SCGenChallengeWinLoss512_020", "SCGenChallengeWinLoss512_021",
                                    "SCGenChallengeWinLoss512_022", "SCGenChallengeWinLoss512_023", "SCGenChallengeWinLoss512_024",
                                    "SCGenChallengeWinLoss512_025", "SCGenChallengeWinLoss512_026", "SCGenChallengeWinLoss512_027",
                                    "SCGenChallengeWinLoss512_028", "SCGenChallengeWinLoss512_029", "SCGenChallengeWinLoss512_030",
                                    "SNUserInterface512_004", "SSUserInterface512_002", "SUUserInterface512_004", "Victorious"]
        }
    # Filter out language-specific assets from ini scraping
    ini_textures_scraping = [item for item in ini_textures_scraping if
                             item not in language_assets["textures_mapped_images"]]
    ini_models_scraping = [item for item in ini_models_scraping if item not in language_assets["models"]]
    mapped_textures = [item for item in mapped_textures if item not in language_assets["textures_mapped_images"]]

    # Call the selected functions
    for function_choice in function_choices:
        if function_choice == "1":
            print("Calling function: find_invalid_models_textures_images_from_ini_folder")
            invalid_textures = invalid_given_assets_in_assets_list(ini_textures_scraping, textures_files)
            invalid_images = invalid_given_assets_in_assets_list(ini_images_scraping, images)
            invalid_models = invalid_given_assets_in_assets_list(ini_models_scraping, models_files)
            write_to_file(os.path.join(output_folder, 'invalid_textures_in_ini_files.txt'), invalid_textures)
            write_to_file(os.path.join(output_folder, 'invalid_mapped_images_in_ini_files.txt'), invalid_images)
            write_to_file(os.path.join(output_folder, 'invalid_models_in_ini_files.txt'), invalid_models)

        elif function_choice == "2":
            print("Calling function: get_mapped_images_and_textures_from_MappedImages_folder")
            mapped_images_list = [(texture, image) for texture, images in
                                  textures_files_mapped_images_dictionary.items() for image in images]
            write_to_file(os.path.join(output_folder, 'mapped_images_list.txt'), mapped_images_list,
                          lambda x: f"{x[0]} {x[1]}")

        elif function_choice == "3":
            print("Calling function: write_to_file (duplicate_mapped_images.txt)")
            write_to_file(os.path.join(output_folder, 'duplicate_mapped_images.txt'), duplicate_images,
                          lambda x: f"{x[0]} {x[1]}")

        elif function_choice == "4":
            print("Calling function: invalid_textures_files_in_mapped_images")
            invalid_textures_files = invalid_given_assets_in_assets_list(mapped_textures, textures_files)
            write_to_file(os.path.join(output_folder, 'invalid_textures_in_mapped_images_folder.txt'),
                          invalid_textures_files)

        elif function_choice == "5":
            print("Calling function: invalid_images_in_wnd")
            wnd_images = extract_images_from_wnd_files(folder_paths['wnd'])
            invalid_wnd_images = invalid_given_assets_in_assets_list(wnd_images, images)
            write_to_file(os.path.join(output_folder, 'invalid_mapped_images_in_wnd_files.txt'), invalid_wnd_images)

        elif function_choice == "6":
            print("Calling function: invalid_textures_in_w3d")
            invalid_textures_in_w3d_files = invalid_textures_in_w3d(textures_files, folder_paths['w3d'])
            write_to_file(os.path.join(output_folder, 'invalid_textures_in_w3d_files.txt'),
                          [f"{w3d_file} {', '.join(textures)}" for w3d_file, textures in invalid_textures_in_w3d_files])

        elif function_choice == "7":
            print("Calling function: find_unused_models_textures_images_in_game_files")
            w3d_textures = extract_textures_from_w3d_files(folder_paths['w3d'])
            if not is_original:
                textures_files = textures_files.union(
                    get_files_from_folder(original_folder_paths['textures']))
                w3d_textures += extract_textures_from_w3d_files(original_folder_paths['w3d'])
            unused_textures_list = ini_textures_scraping + mapped_textures + w3d_textures
            unused_textures = unused_assets_in_assets_list(textures_files, unused_textures_list)
            unused_textures = check_strings_in_dat_file(unused_textures, folder_paths['dat'])
            write_to_file(os.path.join(output_folder, 'unused_textures.txt'), unused_textures)

            unused_models = unused_assets_in_assets_list(models, ini_models_scraping)
            unused_models = check_strings_in_dat_file(unused_models, folder_paths['dat'])
            write_to_file(os.path.join(output_folder, 'unused_models.txt'), unused_models)

            wnd_images = extract_images_from_wnd_files(folder_paths['wnd'])
            unused_images = unused_assets_in_assets_list(images, ini_images_scraping + wnd_images)
            unused_images = check_strings_in_dat_file(unused_images, folder_paths['dat'])
            write_to_file(os.path.join(output_folder, 'unused_mapped_images.txt'), unused_images, warning=True)

        elif function_choice == "8":
            print("Calling function: analyze_language_files")
            analyze_language_graphical_assets(folder_paths['ini'].replace('/Data/INI', ''), languages, language_assets, output_folder,
                                   ini_textures_scraping, ini_models_scraping, mapped_textures, textures_files,
                                   original_base_folder_paths=original_folder_path if not is_original else None)
        else:
            print(f"Invalid choice: {function_choice}. No function executed.")


if __name__ == "__main__":
    main()
