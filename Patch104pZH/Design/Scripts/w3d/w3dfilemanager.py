import os

g_this_dir = os.path.dirname(os.path.abspath(__file__))

class W3dFile:
    path: str
    data: bytes


class W3dFileManager:
    file_dict: dict[str, W3dFile]


    def __init__(self):
        self.file_dict = dict[str, W3dFile]()


    def get_or_create_w3d_file(self, file_path: str) -> W3dFile:
        if not os.path.exists(file_path):
            file_path = os.path.join(g_this_dir, file_path)
        if not os.path.exists(file_path):
            file_path = os.path.join(os.getcwd(), file_path)
        if not os.path.exists(file_path):
            raise FileNotFoundError(file_path)

        w3dfile: W3dFile = self.file_dict.get(file_path)
        if w3dfile == None:
            w3dfile = W3dFile()
            with open(file_path, "rb") as file:
                w3dfile.path = file_path
                w3dfile.data = file.read()
            self.file_dict[file_path] = w3dfile

        return w3dfile


    def rename_texture(self, file_path: str, replace_from: str, replace_to: str) -> None:
        w3dfile: W3dFile = self.get_or_create_w3d_file(file_path)
        if not w3dfile.data.find(replace_from):
            raise AttributeError(replace_from, "not found")
        if len(replace_from) != len(replace_to):
            raise AttributeError(replace_from, replace_to, "mismatching lengths")
        w3dfile.data = w3dfile.data.replace(replace_from, replace_to)


    def write_out(self):
        w3dfile: W3dFile
        for w3dfile in self.file_dict.values():
            old_file_root = os.path.dirname(w3dfile.path)
            old_file_name = os.path.basename(w3dfile.path)
            new_file_root = os.path.join(old_file_root, "edited")
            new_file_path = os.path.join(new_file_root, old_file_name)
            os.makedirs(new_file_root, exist_ok=True)
            with open(new_file_path, "wb") as new_file:
                new_file.write(w3dfile.data)
