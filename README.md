# PyMesh
Python library for meshes conversions and utilities for colouring the meshes.

## Build and launch

Clone the repo.
```
git clone https://github.com/kerrambit/PyMesh/tree/dev & cd PyMesh
```

Install needed dependencies.
```
pip install -e .
```

Use *convert.py* CLI application to easily convert different mesh formats.
```
python3 .\src\cli-clients\convert.py --input_file_path .\example_data\pumpkin_tall_10k.obj --output_folder_path ./example_data --output_file_format stl --debugging_info true
```

Use *visualize.py* CLI application to easily display the mesh. You can write your own script using PyMesh library to e.g. color the mesh.
```
python3 .\src\cli-clients\visualize.py --input_mesh_filepath .\example_data\export.stl --input_script_filepath .\example_scripts\script.py --window_title "Pumpkin visualizer"
```

Run the tests suites.
```
python3 -m pytest
```

## Comments

*Find the appropriate Python library for conversion of “.obj” file with mesh data to “.stl” file.*
- I have chosen [Trimesh](https://trimesh.org/) as the default Python library for this task. However, I tried to make code modular in the sense that any other library can be used. For example, the repository also contains *PyMeshLabConvertor* class to convert files using [PyMeshLab](https://pymeshlab.readthedocs.io/en/latest/) library.
- The code has abtract classes *InputMeshFile* and *OutputMeshFile* from which individual format classes can inherit (**note**: in the current state, the library supports only two types, OBJ and STL files, but there is no issue in adding more - the system enables this with just writing another specified format class). The reason for this hierarchy is that e.g. *PyMeshLab* enables to specify users more detailed imports/exports arguments other than just filepath, [see](https://pymeshlab.readthedocs.io/en/latest/io_format_list.html).

*Visualize the obtained “.stl” file with another Python library. Color the mesh such that the object it represents looks as much similar as possible to its real-world counterpart.*
- For this part I have chosen [PyVista library](https://docs.pyvista.org/). It is a Python high-level API to the Visualization Toolkit (VTK). I have created simple wrapper objects around PyVista objects so the user may use only a few classes for a simple visualiztion, which is the aim of Pymesh.

*Develop a python CLI application based on your solution, that allows the user to have more control over the process of conversion and visualization.*
- This library contains two CLI applications using *argparse* library. First application *convert.py* helps with the different file format conversions. The application *visualize.py* takes a special Python script file and the mesh file. Then it runs the script with the mesh object. Users can write their own simple script using *Pymesh* library without any need of knowledge of *PyVista* or other libraries.


*Create a publicly available google colab notebook (or alternative) with your solution so that anyone can run the code and obtain the visualization right in the web browser.*
- TODO

*Find errors and mistakes related to the task content itself (if any) and suggest possible improvements.*
- The only thing is that I am not sure if the attached .obj file could be publicly shared inside the GitHub repository (so the user can run the example script without any problem).