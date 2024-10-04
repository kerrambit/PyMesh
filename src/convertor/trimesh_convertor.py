from trimesh import load
from .mesh_types import InputMeshFile, OutputMeshFile
from .convertor import Convertor


class TrimeshConvertor(Convertor):
    
    def __init__(self) -> None:
        pass
    
    def convert_mesh(self, input_file: InputMeshFile, output_file: OutputMeshFile):

        mesh = load(input_file.get_full_import_filepath())
        mesh.export(output_file.get_full_export_filepath())
