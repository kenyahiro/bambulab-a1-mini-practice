import cadquery as cq

key_pitch = 17.0
key_hole = 14.0 # 13.95
frame = 2

key_x_num = 10
key_y_num = 4
height = key_pitch * key_x_num + frame
width = key_pitch * key_y_num + frame
thickness = 1.2


# make the base
result = cq.Workplane("XY").moveTo(height/2, width/2).box(height, width, thickness)
result = (result.edges("|Z")
          .fillet(2))


for y in range(key_y_num):
    for x in range(key_x_num):
        result = (result.faces(">Z")
                  .workplane()
                  .moveTo(key_pitch /2 + key_pitch * x + frame/2, key_pitch / 2 + key_pitch * y + frame/2)
                  .rect(key_hole, key_hole)
                  .cutThruAll())



# Render the solid
show_object(result)


# Export
cq.exporters.export(result, "choc_test01.stl")
cq.exporters.export(result.section(), "choc_test01.dxf")
cq.exporters.export(result, "choc_test01.step")