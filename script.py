from visualizer import Color, Mesh, Camera, Coordinate, Light, Plotter
import numpy as np
import sys

ORANGE = Color(255, 140, 0).get_normalized_color_array()
DARK_ORANGE = Color(248, 130, 0).get_normalized_color_array()
GREEN = Color(1, 50, 32).get_normalized_color_array()
BROWN = Color(111, 78, 55).get_normalized_color_array()


def main():

    if len(sys.argv) != 3:
        print(
            "Two arguments are mandatory for this script: mesh filepath and window title!"
        )
        sys.exit(1)

    mesh_filepath = sys.argv[1]
    window_title = sys.argv[2]

    # ------------------------------------------------------------------------------------- #

    plotter = Plotter(window_title)

    mesh = Mesh(mesh_filepath)
    mesh.rotate_x(-90)
    mesh.scale(1.5)
    mesh.compute_normals()

    colors = np.zeros((mesh.get_cells_count(), 4))

    x_radius_for_stalk = 5
    y_min_for_stalk = -57
    y_max_for_stalk = -50
    z_radius_for_stalk = 5

    x_radius_for_lower_stalk = 2.5
    y_min_for_lower_stalk = -95
    y_max_for_lower_stalk = -91.5
    z_radius_for_lower_stalk = 2.5

    for i, center in enumerate(mesh.get_cell_centers().points):
        x = center[0]
        y = center[1]
        z = center[2]

        if y_min_for_stalk <= y <= y_max_for_stalk:
            x_offset = abs(x - mesh.get_center_of_mesh()[0])
            z_offset = abs(z - mesh.get_center_of_mesh()[2])
            if x_offset < x_radius_for_stalk and z_offset < z_radius_for_stalk:
                colors[i] = GREEN
            else:
                colors[i] = DARK_ORANGE
        elif y_min_for_lower_stalk <= y <= y_max_for_lower_stalk:
            x_offset = abs(x - mesh.get_center_of_mesh()[0])
            z_offset = abs(z - mesh.get_center_of_mesh()[2])
            if (
                x_offset < x_radius_for_lower_stalk
                and z_offset < z_radius_for_lower_stalk
            ):
                colors[i] = BROWN
            else:
                colors[i] = DARK_ORANGE
        else:
            colors[i] = ORANGE

    key = "colors"
    mesh.assign_cell_data(key, colors)
    plotter.add_mesh(mesh, scalar_key=key)
    plotter.set_background_color(Color(0, 0, 0))

    camera = Camera(Coordinate(-90.0, 70.0, 130.0), Coordinate(-15.0, -40.0, 20.0))
    plotter.add_camera(camera)

    light = Light(Coordinate(-110.0, 70.0, 130.0), Color(1.0, 1.0, 1.0), 1.0)
    plotter.add_light_source(light)

    plotter.show_axes = True
    plotter.render()
    sys.exit(0)


if __name__ == "__main__":
    main()
