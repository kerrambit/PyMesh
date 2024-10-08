from pathlib import Path
import pyvista
from .mesh import Mesh
from .camera import Camera
from .color import Color
from .light import Light


class Plotter:
    def __init__(self, title: str) -> None:
        self.title = title
        self.__plotter = pyvista.Plotter(title=self.title)
        self.show_bounds: bool = False
        self.show_axes: bool = False

    def add_mesh(self, mesh: Mesh):
        self.__plotter.add_mesh(
            mesh.get_mesh_copy(), rgb=True, show_edges=mesh.edges_visible, line_width=1
        )

    def add_mesh(self, mesh: Mesh, scalar_key: str):
        self.__plotter.add_mesh(
            mesh.get_mesh_copy(),
            scalars=scalar_key,
            rgb=True,
            show_edges=mesh.edges_visible,
            line_width=1,
        )

    def add_camera(self, camera: Camera):
        self.__plotter.camera = camera.camera

    def set_background_color(self, color: Color):
        self.__plotter.background_color = color.get_normalized_color_array()

    def add_background_image(self, path: Path):
        self.__plotter.add_background_image(str(path))

    def add_light_source(self, light: Light):
        self.__plotter.add_light(light.light)

    def render(self):
        if self.show_axes:
            self.__plotter.show_axes()
        if self.show_bounds:
            self.__plotter.show_bounds()

        self.__plotter.show()
