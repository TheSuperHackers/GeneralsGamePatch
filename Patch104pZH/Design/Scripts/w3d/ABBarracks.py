from w3dfilemanager import W3dFileManager

if __name__ == "__main__":
    manager = W3dFileManager()
    manager.rename_texture("ABBarracks_D.W3D", b"ATBarrSlab_E.tga", b"ATBarrSlab_D.tga")
    manager.rename_texture("ABBarracks_DN.W3D", b"ATBarrSlab_E.tga", b"ATBarrSlab_D.tga")
    manager.rename_texture("ABBarracks_DS.W3D", b"ATBarrSlab_ES.tga", b"ATBarrSlab_DS.tga")
    manager.rename_texture("ABBarracks_DNS.W3D", b"ATBarrSlab_ES.tga", b"ATBarrSlab_DS.tga")
    manager.write_out()
