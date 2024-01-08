import bpy

# Unit: 1mm
baseValue = 0.3
maxValue = 1 / 3 * 20

img_path = "/Users/alessioantonucci/Downloads/grafico-grigio-inv.png"
export_path = "/Users/alessioantonucci/Downloads/grafico_3D.stl"

# Load image and get width and height
img = bpy.data.images.load(img_path)
width, height = img.size[0], img.size[1]

for i in range(width):
    for j in range(height):
        # Create plane in the current pixel position.
        bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=True, align='WORLD', location=(j, i, 0))
        # Extrude plane according with the gray intencity: black pixel = 0 + baseValue; white pixel = 1 * maxValue + baseValue; intermediate value...
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, img.pixels[(i * width + j) * 4] * maxValue + baseValue)})

bpy.ops.object.mode_set(mode='OBJECT')

model = bpy.context.active_object
model.select_set(True)
bpy.context.view_layer.objects.active = model

# Export in stl format
bpy.ops.export_mesh.stl(filepath=export_path, check_existing=True, use_selection=True)