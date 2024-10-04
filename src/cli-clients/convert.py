import argparse
from convertor import (
    FileFormat,
    TrimeshConvertor,
    InputMeshFile,
    OutputMeshFile,
    STLInputMeshFile,
    OBJInputMeshFile,
    STLOutputMeshFile,
    OBJOutputMeshFile,
)
from pathlib import Path
from utils import Debugger
from sys import stdout
from typing import Tuple


def prepare_input_file(args) -> Tuple[Path, str]:

    input_file = Path(args.input_file_path)
    input_extension = input_file.suffix.lower()[1:]
    if args.input_file_path_format is not None:
        input_extension = args.input_file_path_format

    return input_file, input_extension


def prepare_output_file(args) -> Tuple[Path, str, str]:

    output_folder = Path(args.output_folder_path)
    output_file = args.output_filename
    output_extension = args.output_file_format

    return output_folder, output_file, output_extension


def generate_arguments(parser: argparse.ArgumentParser):
    choises = FileFormat.get_string_array()
    parser.add_argument(
        "--input_file_path",
        type=str,
        required=True,
        help="The path to the file with the mesh.",
    )
    parser.add_argument(
        "--input_file_path_format",
        type=str,
        required=False,
        help="Overrides INPUT_FILE_PATH extension.",
        choices=choises,
    )
    parser.add_argument(
        "--output_folder_path",
        type=str,
        required=True,
        help="The path to the output directory.",
    )
    parser.add_argument(
        "--output_file_format",
        type=str,
        required=True,
        help="Defines the output mesh format.",
        choices=choises,
    )
    parser.add_argument(
        "--output_filename",
        type=str,
        required=False,
        help="Defines the name of the export file. Default is 'export'.",
        default="export",
    )
    parser.add_argument(
        "--debugging_info",
        type=bool,
        required=False,
        help="Send the debug information into stdout.",
    )


def get_input_mesh_file(input_extension: str, input_file: Path) -> InputMeshFile:

    input_format = FileFormat.get_file_format_from_string(input_extension)
    if input_format == FileFormat.STL:
        input = STLInputMeshFile(input_file)
    elif input_format == FileFormat.OBJ:
        input = OBJInputMeshFile(input_file)
    else:
        input = STLInputMeshFile(input_file)

    return input


def get_output_mesh_file(
    output_extension: str, output_folder: Path, output_file: str
) -> OutputMeshFile:
    output_format = FileFormat.get_file_format_from_string(output_extension)
    if output_format == FileFormat.STL:
        output = STLOutputMeshFile(
            output_folder,
            output_file,
            binary=False,
            colormode=False,
            save_face_color=False,
        )
    elif output_format == FileFormat.OBJ:
        output = OBJOutputMeshFile(output_folder, output_file)
    else:
        output = STLOutputMeshFile(output_folder, output_file, binary=True)

    return output


def main():

    parser = argparse.ArgumentParser(
        prog="PyMesh",
        description="Python library for meshes conversions and utilities for colouring the meshes.",
    )
    generate_arguments(parser)
    args = parser.parse_args()

    input_file, input_extension = prepare_input_file(args)
    output_folder, output_file, output_extension = prepare_output_file(args)

    if args.debugging_info is not None and args.debugging_info:
        debugger = Debugger(stdout)
    else:
        debugger = None

    input = get_input_mesh_file(input_extension, input_file)
    output = get_output_mesh_file(output_extension, output_folder, output_file)

    convertor = TrimeshConvertor()
    convertor.convert_mesh(input, output, debugger)


if __name__ == "__main__":
    main()
