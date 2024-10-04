from .mesh_types import InputMeshFile, OutputMeshFile
from abc import ABC, abstractmethod
from utils import Debugger


class Convertor(ABC):

    @classmethod
    @abstractmethod
    def convert_mesh(
        input_file: InputMeshFile,
        output_file: OutputMeshFile,
        debugger: Debugger | None = None,
    ):
        pass
