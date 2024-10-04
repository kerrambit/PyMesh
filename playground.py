import numpy as np
import pyvista
from visualizer import Color

plotter = pyvista.Plotter(title="Pumpkin example")

mesh = pyvista.read("export.stl")
mesh.rotate_x(angle = -90, inplace = True)
mesh.points /= 1.5
mesh.compute_normals(inplace=True)
center_of_mesh = mesh.center

cell_centers = mesh.cell_centers()

colors = np.zeros((mesh.n_cells, 4))
orange = Color(255, 140, 0).get_normalized_color_array()
dark_orange = Color(248, 130, 0).get_normalized_color_array()
green = Color(1, 50, 32).get_normalized_color_array()
brown = Color(111, 78, 55).get_normalized_color_array()

y_min_for_stalk = -57
y_max_for_stalk = -50
x_radius_for_stalk = 5
z_radius_for_stalk = 5

y_min_for_lower_stalk = -95
y_max_for_lower_stalk = -91.5
x_radius_for_lower_stalk = 2.5
z_radius_for_lower_stalk = 2.5

for i, center in enumerate(cell_centers.points):
    y_value = center[1]
    x_value = center[0]
    z_value = center[2]
    
    if y_min_for_stalk <= y_value <= y_max_for_stalk:
        x_offset = abs(x_value - center_of_mesh[0])
        z_offset = abs(z_value - center_of_mesh[2])
        if x_offset < x_radius_for_stalk and z_offset < z_radius_for_stalk:
            colors[i] = green
        else:
            colors[i] = dark_orange
    elif y_min_for_lower_stalk <= y_value <= y_max_for_lower_stalk:
        x_offset = abs(x_value - center_of_mesh[0])
        z_offset = abs(z_value - center_of_mesh[2])
        if x_offset < x_radius_for_lower_stalk and z_offset < z_radius_for_lower_stalk:
            colors[i] = brown
        else:
            colors[i] = dark_orange
    else:
        colors[i] = orange

#plotter.add_background_image("background.png")
mesh.cell_data["colors"] = colors
plotter.add_mesh(mesh, scalars="colors", rgb=True, show_scalar_bar=True, show_edges=True, line_width=1)
plotter.background_color = Color(196, 164, 132).get_normalized_color_array()

camera = pyvista.Camera()
camera.position = (-90.0, 70.0, 130.0)
camera.focal_point = (-15.0, -40.0, 20.0)
plotter.camera = camera


# y-axe line
start_point = np.array([-2, -200, 0]) 
end_point = np.array([-2, 150, 0]) 
line = pyvista.Line(start_point, end_point)
plotter.add_mesh(line, color="green", line_width=5)
arrow = pyvista.Arrow(start_point, end_point - start_point, scale=10)
plotter.add_mesh(arrow, color="red")

# y-axe line
start_point = np.array([-6.5, -200, 0]) 
end_point = np.array([-6.5, 150, 0]) 
line = pyvista.Line(start_point, end_point)
plotter.add_mesh(line, color="green", line_width=5)
arrow = pyvista.Arrow(start_point, end_point - start_point, scale=10)
plotter.add_mesh(arrow, color="red")

# z-axe line
start_point = np.array([-2, -95, -50]) 
end_point = np.array([-2, -95, 200]) 
line = pyvista.Line(start_point, end_point)
plotter.add_mesh(line, color="green", line_width=5)
arrow = pyvista.Arrow(start_point, end_point - start_point, scale=10)
plotter.add_mesh(arrow, color="red")

# z-axe line
start_point = np.array([-2, -50, 0]) 
end_point = np.array([-2, -50, 200]) 
line = pyvista.Line(start_point, end_point)
plotter.add_mesh(line, color="green", line_width=5)
arrow = pyvista.Arrow(start_point, end_point - start_point, scale=10)
plotter.add_mesh(arrow, color="red")

light = pyvista.Light()
light.SetPosition(-110.0, 70.0, 130.0)
light.SetColor(1.0, 1.0, 1.0)
light.SetIntensity(1)

plotter.add_light(light)
plotter.show_axes()

plotter.show()
