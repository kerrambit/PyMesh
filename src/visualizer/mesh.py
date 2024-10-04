import pyvista
from pathlib import Path
import numpy as np


class Mesh:
    def __init__(self, file_path: Path) -> None:
        self.__file_path = file_path
        self.__mesh = pyvista.read(str(self.__file_path))

    def get_cell_centers(self):
        return self.__mesh.cell_centers()

    def get_center_of_mesh(self):
        return self.__mesh.center

    def get_cells_count(self):
        return self.__mesh.n_cells

    def file_path(self) -> Path:
        return self.__file_path

    def get_cells(self):
        return self.__mesh.cell

    def get_points(self):
        return self.__mesh.points

    def scale(self, factor: float) -> None:
        self.__mesh.points /= factor

    def rotate_x(self, angle: float):
        self.__mesh.rotate_x(angle, inplace=True)

    def rotate_y(self, angle: float):
        self.__mesh.rotate_y(angle, inplace=True)

    def rotate_z(self, angle: float):
        self.__mesh.rotate_z(angle, inplace=True)

    def assign_cell_data(self, key: str, data: np.ndarray[np.float64]):
        self.__mesh.cell_data[key] = data

    def compute_normals(self):
        self.__mesh.compute_normals(inplace=True)

    def get_mesh_copy(self):
        return self.__mesh.copy()
