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

    input_file_path = Path(args.input_file_path)
    input_extension = input_file_path.suffix.lower()[1:]

    return input_file_path, input_extension


def prepare_output_file(args) -> Tuple[Path, str, str]:

    output_file_path = Path(args.output_file_path)
    output_extension = output_file_path.suffix.lower()[1:]

    return output_file_path, output_extension


def split_path(path: str) -> Tuple[str, str]:

    path = Path(path)
    directory = path.parent
    filename = path.stem

    return str(directory), str(filename)


def generate_arguments(parser: argparse.ArgumentParser):

    parser.add_argument(
        "--input_file_path",
        type=str,
        required=True,
        help="The path to the file with the mesh.",
    )
    parser.add_argument(
        "--output_file_path",
        type=str,
        required=True,
        help="The path to the exported file (used extension defines the format).",
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


def get_output_mesh_file(output_extension: str, output_file: Path) -> OutputMeshFile:

    output_format = FileFormat.get_file_format_from_string(output_extension)
    directory, filename = split_path(str(output_file))
    directory = Path(directory)

    if output_format == FileFormat.STL:
        output = STLOutputMeshFile(
            directory,
            filename,
            binary=False,
            colormode=False,
            save_face_color=False,
        )
    elif output_format == FileFormat.OBJ:
        output = OBJOutputMeshFile(directory, filename)
    else:
        output = STLOutputMeshFile(directory, filename, binary=True)

    return output


def main():

    parser = argparse.ArgumentParser(
        prog="PyMesh.Convertor",
        description="Python library for meshes conversions and utilities for colouring the meshes.",
    )
    generate_arguments(parser)
    args = parser.parse_args()

    input_file_path, input_extension = prepare_input_file(args)
    output_file_path, output_extension = prepare_output_file(args)

    if args.debugging_info is not None and args.debugging_info:
        debugger = Debugger(stdout)
    else:
        debugger = None

    input = get_input_mesh_file(input_extension, input_file_path)
    output = get_output_mesh_file(output_extension, output_file_path)

    convertor = TrimeshConvertor()
    convertor.convert_mesh(input, output, debugger)


if __name__ == "__main__":
    main()
