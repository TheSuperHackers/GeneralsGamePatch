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
                        textures.add(texture)
                        if image not in mapped_images:
                            mapped_images.add(image)
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
        if file_name.endswith(('.tga', '.dds')):
            base_name, _ = os.path.splitext(file_name)
            textures.add(base_name)

    return textures

def get_textures_from_folder(texture_folder_path=None):
    """Get all the texture files in a folder."""
    textures = set()
    if texture_folder_path:
        for root, _, files in os.walk(texture_folder_path):
            for file in files:
                if file.lower().endswith(('.tga', '.dds', '.psd')):
                    base_name, _ = os.path.splitext(file.lower())
                    textures.add(base_name)

    return textures

def missing_textures_in_files(textures, textures_files):
    missing_textures = []
    for texture in textures:
        texture_name, _ = os.path.splitext(texture.lower())
        if texture_name not in textures_files:
            missing_textures.append(texture)

    return sorted(missing_textures)

def invalid_images_in_wnd(wnd_folder_path, images):
    invalid_images = set()
    for root, _, files in os.walk(wnd_folder_path):
        for filename in files:
            if filename.lower().endswith('.wnd'):
                file_path = os.path.join(root, filename)
                content = read_file_content(file_path)
                if content:
                    found_images = re.findall(r"IMAGE:\s*([^\s,]+)", content)
                    for image in found_images:
                        if image != 'NoImage' and image not in images:
                            invalid_images.add(image)

    return sorted(list(invalid_images))

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

def write_to_file(output_path, data, format_func=None):
    with open(output_path, 'w') as f:
        for item in data:
            f.write(f"{format_func(item) if format_func else item}\n")

def main():
    # Select whether to scan the original or edited files.
    is_original = False

    folder_paths = {
        'ini': '../../../GameFilesOriginalZH/Data/INI/MappedImages' if is_original else '../../../GameFilesEdited/Data/INI/MappedImages',
        'wnd': '../../../GameFilesOriginalZH/Window' if is_original else '../../../GameFilesEdited/Window',
        'w3d': '../../../GameFilesOriginalZH/Art/W3D' if is_original else '../../../GameFilesEdited/Art/W3D',
        'textures': None if is_original else '../../../GameFilesEdited/Art/Textures',
        'csv': '../../../Resources/FileHashRegistry/Generals-108-GeneralsZH-104.csv'
    }

    output_folder = 'generated_original' if is_original else 'generated_edited'
    os.makedirs(output_folder, exist_ok=True)

    texture_and_images, images, textures, duplicate_images = get_mapped_images_and_textures(folder_paths['ini'])
    textures_files = get_textures_from_csv(folder_paths['csv']).union(
        get_textures_from_folder(folder_paths['textures']))

    write_to_file(os.path.join(output_folder, 'mapped_images_list.txt'), texture_and_images, lambda x: f"{x[0]} {x[1]}")
    write_to_file(os.path.join(output_folder, 'duplicate_mapped_images.txt'), duplicate_images, lambda x: f"{x[0]} {x[1]}")

    missing_textures = missing_textures_in_files(textures, textures_files)
    write_to_file(os.path.join(output_folder, 'missing_textures_files.txt'), missing_textures)

    invalid_wnd_images = invalid_images_in_wnd(folder_paths['wnd'], images)
    write_to_file(os.path.join(output_folder, 'invalid_wnd_images.txt'), invalid_wnd_images)

    invalid_textures_in_w3d_files = invalid_textures_in_w3d(textures_files, folder_paths['w3d'])
    write_to_file(os.path.join(output_folder, 'invalid_textures_in_w3d_files.txt'),
                  [f"{w3d_file} {', '.join(textures)}" for w3d_file, textures in invalid_textures_in_w3d_files])


if __name__ == "__main__":
    main()
