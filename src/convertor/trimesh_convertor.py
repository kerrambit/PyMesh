from trimesh import load
from .mesh_types import InputMeshFile, OutputMeshFile
from .convertor import Convertor
from utils import Debugger


class TrimeshConvertor(Convertor):

    def __init__(self) -> None:
        pass

    def convert_mesh(
        self,
        input_file: InputMeshFile,
        output_file: OutputMeshFile,
        debugger: Debugger | None = None,
    ):

        self.__print(
            f"Import filepath: '{input_file.get_full_import_filepath()}'.", debugger
        )
        mesh = load(input_file.get_full_import_filepath())
        self.__print(f"Mesh was loaded.", debugger)
        self.__print(
            f"Export filepath: '{output_file.get_full_export_filepath()}'.", debugger
        )
        mesh.export(output_file.get_full_export_filepath())
        self.__print("Export and conversion was succesfully finished.", debugger)

    def __print(self, message: str, debugger: Debugger | None):
        if debugger is not None:
            debugger.write(message)
