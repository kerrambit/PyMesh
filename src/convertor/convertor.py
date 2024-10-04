from .mesh_types import InputMeshFile, OutputMeshFile
from abc import ABC, abstractmethod

class Convertor(ABC):
    
    @classmethod
    @abstractmethod
    def convert_mesh(input_file: InputMeshFile, output_file: OutputMeshFile):
        pass

