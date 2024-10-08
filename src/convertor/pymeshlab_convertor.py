from .convertor import Convertor
from .mesh_types import InputMeshFile, OutputMeshFile, FileFormat
from typing import Tuple
from pymeshlab import MeshSet
from utils import Debugger


class PyMeshLabConvertor(Convertor):

    def __init__(self) -> None:
        pass

    def convert_mesh(
        self,
        input_file: InputMeshFile,
        output_file: OutputMeshFile,
        debugger: Debugger | None = None,
    ):

        mesh_set = MeshSet()
        full_input_path = input_file.get_full_import_filepath()

        if input_file.get_type() == FileFormat.OBJ:
            mesh_set.load_new_mesh(full_input_path)
        else:
            mesh_set.load_new_mesh(full_input_path)

        full_output_path = output_file.get_full_export_filepath()
        basic_properties: Tuple[str, bool, int] = (
            full_output_path,
            output_file.save_textures,
            output_file.texture_quality,
        )

        if output_file.get_type() == FileFormat.STL:
            mesh_set.save_current_mesh(
                *basic_properties,
                binary=output_file.binary,
                colormode=output_file.colormode,
                save_face_color=output_file.save_face_color,
            )
        else:
            mesh_set.save_current_mesh(*basic_properties)
