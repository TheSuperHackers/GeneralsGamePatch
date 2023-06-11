from w3dfilemanager import W3dFileManager

if __name__ == "__main__":
    manager = W3dFileManager()
    manager.rename_texture("NBPwrPtI_E.W3D", b"NTPwrPlantSlab_D.tga", b"NTPwrPlantSlab_E.tga")
    manager.rename_texture("NBPwrPtI_EN.W3D", b"NTPwrPlantSlab_D.tga", b"NTPwrPlantSlab_E.tga")
    manager.write_out()
