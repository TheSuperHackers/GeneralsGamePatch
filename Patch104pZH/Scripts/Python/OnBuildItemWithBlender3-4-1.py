import os
import subprocess
from common import *

# https://docs.blender.org/api/3.4/bpy.types.Object.html
# https://docs.blender.org/api/3.4/bpy.types.Mesh.html
# https://docs.blender.org/api/3.4/bpy.types.Material.html
# https://docs.blender.org/api/3.4/bpy.types.NodeTree.html

g_blenderscript = """
import bpy
import math

def IsZeroVec(v):
    return (math.isclose(v.x, 0.0, rel_tol=1e-6) and
            math.isclose(v.y, 0.0, rel_tol=1e-6) and
            math.isclose(v.z, 0.0, rel_tol=1e-6))

def ToDegrees(v):
    v.x = v.x * (180/math.pi)
    v.y = v.y * (180/math.pi)
    v.z = v.z * (180/math.pi)
    return v

totalvertices = 0
totalpolygons = 0

for mesh in bpy.data.meshes:
    totalvertices += len(mesh.vertices)
    totalpolygons += len(mesh.polygons)

print(f'total vertices: {totalvertices}')
print(f'total polygons: {totalpolygons}')

for obj in bpy.data.objects:
    print(f'{obj.name} is {obj.type}')
    vb = obj.matrix_basis.to_translation()
    vl = obj.matrix_local.to_translation()
    vw = obj.matrix_world.to_translation()
    ab = ToDegrees(obj.matrix_basis.to_euler())
    al = ToDegrees(obj.matrix_local.to_euler())
    aw = ToDegrees(obj.matrix_world.to_euler())
    if not IsZeroVec(vb):
        print('  basis.pos: [{:.06f}, {:.06f}, {:.06f}]'.format(vb.x, vb.y, vb.z))
    if not IsZeroVec(vl):
        print('  local.pos: [{:.06f}, {:.06f}, {:.06f}]'.format(vl.x, vl.y, vl.z))
    if not IsZeroVec(vw):
        print('  world.pos: [{:.06f}, {:.06f}, {:.06f}]'.format(vw.x, vw.y, vw.z))
    if not IsZeroVec(ab):
        print('  basis.ang: [{:.06f}, {:.06f}, {:.06f}]'.format(ab.x, ab.y, ab.z))
    if not IsZeroVec(al):
        print('  local.ang: [{:.06f}, {:.06f}, {:.06f}]'.format(al.x, al.y, al.z))
    if not IsZeroVec(aw):
        print('  world.ang: [{:.06f}, {:.06f}, {:.06f}]'.format(aw.x, aw.y, aw.z))
    if obj.type == 'MESH':
        print(f'  MESH {obj.data.name}')
        mesh = obj.data
        if mesh:
            verticescount = len(mesh.vertices)
            polygonscount = len(mesh.vertices)
            print(f'    vertices: {verticescount}')
            print(f'    polygons: {polygonscount}')
        for mat_slot in obj.material_slots:
            mat = mat_slot.material
            if mat:
                print(f'    material: {mat.name}')
                if mat.node_tree:
                    for node in mat.node_tree.nodes:
                        if node.type=='TEX_IMAGE':
                            print(f'      texture: {node.image.name}')
"""


def GetFileExt(file: str) -> str:
    path, ext = os.path.splitext(file)
    if ext and ext[0] == '.':
        ext = ext[1:]
    return ext


def HasFileExt(file: str, expectedExt: str) -> bool:
    fileExt: str = GetFileExt(file)
    return fileExt.lower() == expectedExt.lower()


def RunBlenderScript(exec: str, source: str) -> None:
    args: list[str] = [exec, source, "--background", "--python-expr", g_blenderscript]
    subprocess.run(args)


def OnEvent(**kwargs) -> None:
    print("Script OnBuildItemWithBlender3-4-1.py called ...")

    tools: dict = kwargs.get(TOOLS)
    buildThing = kwargs.get(RAW_BUILD_THING)

    if tools == None:
        raise Exception("Unable to reference '{TOOLS}' in user script")
    if buildThing == None:
        return
        #raise Exception("Unable to reference '{RAW_BUILD_THING}' in user script")

    tool = tools.get("blender")

    if tool == None:
        raise Exception("Unable to reference 'blender' in '{TOOLS}'")

    exec: str = tool.GetExecutable()
    for buildFile in buildThing.files:
        if buildFile.RequiresRebuild():
            source: str = buildFile.AbsSource()
            if HasFileExt(source, "blend"):
                RunBlenderScript(exec, source)
