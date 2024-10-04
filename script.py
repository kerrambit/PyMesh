import numpy as np
import pyvista
from visualizer import Color, Mesh, Camera, Coordinate, Light
import sys


def main():

    if len(sys.argv) != 3:
        print(
            "Two arguments are mandatory for this script: mesh filepath and window title!"
        )
        sys.exit(1)

    mesh_filepath = sys.argv[1]
    window_title = sys.argv[2]

    # -------------------------------------------------------------------------------------

    plotter = pyvista.Plotter(title=window_title)

    mesh = Mesh(mesh_filepath)
    mesh.rotate_x(-90)
    mesh.scale(1.5)
    mesh.compute_normals()

    colors = np.zeros((mesh.get_cells_count(), 4))
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

    for i, center in enumerate(mesh.get_cell_centers().points):
        x = center[0]
        y = center[1]
        z = center[2]

        if y_min_for_stalk <= y <= y_max_for_stalk:
            x_offset = abs(x - mesh.get_center_of_mesh()[0])
            z_offset = abs(z - mesh.get_center_of_mesh()[2])
            if x_offset < x_radius_for_stalk and z_offset < z_radius_for_stalk:
                colors[i] = green
            else:
                colors[i] = dark_orange
        elif y_min_for_lower_stalk <= y <= y_max_for_lower_stalk:
            x_offset = abs(x - mesh.get_center_of_mesh()[0])
            z_offset = abs(z - mesh.get_center_of_mesh()[2])
            if (
                x_offset < x_radius_for_lower_stalk
                and z_offset < z_radius_for_lower_stalk
            ):
                colors[i] = brown
            else:
                colors[i] = dark_orange
        else:
            colors[i] = orange

    # plotter.add_background_image("background.png")
    key = "colors"
    mesh.assign_cell_data(key, colors)
    plotter.add_mesh(
        mesh.get_mesh_copy(), scalars=key, rgb=True, show_edges=False, line_width=1
    )
    plotter.background_color = Color(0, 0, 0).get_normalized_color_array()

    camera = Camera(Coordinate(-90.0, 70.0, 130.0), Coordinate(-15.0, -40.0, 20.0))
    plotter.camera = camera.camera

    """
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
    """

    light = Light(Coordinate(-110.0, 70.0, 130.0), Color(1.0, 1.0, 1.0), 1.0)

    plotter.add_light(light.light)
    plotter.show_axes()

    plotter.show()


if __name__ == "__main__":
    main()
