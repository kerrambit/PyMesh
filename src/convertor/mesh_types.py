from enum import Enum
from pathlib import Path
from abc import ABC
from typing import List


class FileFormat(Enum):
    STL = 0
    OBJ = 1

    def __str__(self):
        if self == FileFormat.STL:
            return "stl"
        elif self == FileFormat.OBJ:
            return "obj"
        else:
            return "unkown"

    @staticmethod
    def get_string_array() -> List[str]:
        return [str(format_) for format_ in FileFormat]

    @staticmethod
    def get_file_format_from_string(token: str) -> "FileFormat":
        if token in {"STL", "stl"}:
            return FileFormat.STL
        elif token in {"OBJ", "obj"}:
            return FileFormat.OBJ
        else:
            return FileFormat.STL


class InputMeshFile(ABC):

    def __init__(self, file_format: FileFormat, mesh_file_path: Path) -> None:
        self.__file_format = file_format
        self.mesh_file_path = mesh_file_path

    def get_type(self) -> FileFormat:
        return self.__file_format

    def get_full_import_filepath(self) -> str:
        return str(self.mesh_file_path)


class STLInputMeshFile(InputMeshFile):
    def __init__(self, mesh_file_path: Path, unify_vertices: bool = True) -> None:
        super().__init__(FileFormat.STL, mesh_file_path)
        self.unify_vertices = unify_vertices


class OBJInputMeshFile(InputMeshFile):
    def __init__(self, mesh_file_path: Path) -> None:
        super().__init__(FileFormat.OBJ, mesh_file_path)


class OutputMeshFile(ABC):

    def __init__(
        self,
        file_format: FileFormat,
        directory_path: Path,
        filename: str,
        save_textures: bool,
        texture_quality: int,
    ) -> None:
        self.__type: FileFormat = file_format
        self.path: Path = directory_path
        self.filename: str = filename
        self.save_textures: bool = save_textures
        self.texture_quality: int = texture_quality

    def __init__(
        self,
        file_format: FileFormat,
        directory_path: Path,
        filename: str,
    ) -> None:
        self.__type: FileFormat = file_format
        self.path: Path = directory_path
        self.filename: str = filename
        self.save_textures: bool = True
        self.texture_quality: int = -1

    def get_full_export_filepath(self) -> str:
        return str(self.path / f"{self.filename}.{self.get_type()}")

    def get_type(self) -> FileFormat:
        return self.__type


class STLOutputMeshFile(OutputMeshFile):
    def __init__(
        self,
        path: Path,
        filename: str,
        save_textures: bool,
        texture_quality: int,
        binary: bool = False,
        colormode: bool = False,
        save_face_color: bool = False,
    ) -> None:
        super().__init__(FileFormat.STL, path, filename, save_textures, texture_quality)
        self.binary: bool = binary
        self.colormode: bool = colormode
        self.save_face_color: bool = save_face_color

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
    def __init__(
        self, path: Path, filename: str, save_textures: bool, texture_quality: int
    ) -> None:
        super().__init__(FileFormat.OBJ, path, filename, save_textures, texture_quality)

    def __init__(self, path: Path, filename: str) -> None:
        super().__init__(FileFormat.OBJ, path, filename)
