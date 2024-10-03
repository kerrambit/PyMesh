import pymeshlab
from enum import Enum
from pathlib import Path
from abc import ABC


class FileFormat(Enum):
    STL = 0
    OBJ = 1
    PLY = 2

    def __str__(self):
        if self == FileFormat.STL:
            return "stl"
        elif self == FileFormat.OBJ:
            return "obj"
        elif self == FileFormat.PLY:
            return "ply"


class OutputMeshFile(ABC):

    def __init__(
        self, file_format: FileFormat, directory_path: Path, filename: str
    ) -> None:
        self.__type: FileFormat = file_format
        self.path: Path = directory_path
        self.filename: str = filename

    def get_export_file_path(self) -> str:
        return str(self.path / f"{self.filename}.{self.get_type()}")

    def get_type(self) -> FileFormat:
        return self.__type


class STLOutputMeshFile(OutputMeshFile):
    def __init__(
        self,
        path: Path,
        filename: str,
        binary: bool = False,
        colormode: bool = False,
        save_face_color: bool = False,
    ) -> None:
        super().__init__(FileFormat.STL, path, filename)
        self.binary: bool = binary
        self.colormode: bool = colormode
        self.save_face_color: bool = save_face_color


class OBJOutputMeshFile(OutputMeshFile):
    def __init__(self, path: Path, filename: str) -> None:
        super().__init__(FileFormat.OBJ, path, filename)


def convert_mesh(input_file_path: Path, output_file: OutputMeshFile):

    mesh_set = pymeshlab.MeshSet()
    mesh_set.load_new_mesh(str(input_file_path))

    full_path = output_file.get_export_file_path()
    mesh_set.save_current_mesh(full_path)

