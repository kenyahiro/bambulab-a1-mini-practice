import cadquery as cq

key_pitch = 17.0
key_hole = 14.0 # 13.95
frame = 2

key_x_num = 10
key_y_num = 4
height = key_pitch * key_x_num + frame
width = key_pitch * key_y_num + frame
thickness = 1.2

margin = 1


sw_t = 5.3 - 3.1
pcb_t = 1.6
socket_t = 1.8
sw_pcb_thickness = sw_t + pcb_t + socket_t

case_frame = 1
case_height = height + margin + case_frame * 2
case_width = width + margin + case_frame * 2
case_thickness = thickness + sw_pcb_thickness + 1 + 0.4



# make the base
result = cq.Workplane("XY").box(case_height, case_width, case_thickness)

result = (result.edges("|Z")
          .fillet(2))

result = (result.faces(">Z")
          .workplane()
          .rect(height + margin, width + margin)
          .cutBlind(-thickness))

result = (result.faces(">Z[-1]")
          .workplane()
          .rect(height-1, width-1)
          .cutBlind(-sw_pcb_thickness)
          .edges("|Z")
          .fillet(2))


# Render the solid
show_object(result)


# Export
cq.exporters.export(result, "choc_test02.stl")
cq.exporters.export(result.section(), "choc_test02.dxf")
cq.exporters.export(result, "choc_test02.step")