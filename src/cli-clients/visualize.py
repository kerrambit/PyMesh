import argparse
import subprocess


def generate_arguments(parser: argparse.ArgumentParser):

    parser.add_argument(
        "--input_mesh_filepath",
        type=str,
        required=True,
        help="The path to the file with the mesh.",
    )

    parser.add_argument(
        "--input_script_filepath",
        type=str,
        required=True,
        help="The path to the file with the script.",
    )
    parser.add_argument(
        "--window_title",
        type=str,
        required=False,
        help="Title of the window.",
    )


def main():

    parser = argparse.ArgumentParser(
        prog="PyMesh.Visualizer",
        description="Python library for meshes conversions and utilities for colouring the meshes.",
    )
    generate_arguments(parser)
    args = parser.parse_args()

    window_title = "Visualizer"
    if args.window_title is not None:
        window_title = args.window_title

    try:
        subprocess.Popen(
            [
                "python3",
                args.input_script_filepath,
                args.input_mesh_filepath,
                window_title,
            ],
            shell=False,
        )
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the script. Details: '{e}'.")


if __name__ == "__main__":
    main()
