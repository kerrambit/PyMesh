from matplotlib.colors import ListedColormap
import numpy as np
import pyvista

plotter = pyvista.Plotter(title="Pumpkin example")

mesh = pyvista.read("pumpkin.stl")
mesh.rotate_z(angle = 180, inplace = True)
mesh.points /= 1.5
mesh.compute_normals(inplace=True)

mesh['scalars'] = mesh.points[:, 1]

orange = np.array([255 / 256, 140 / 256, 0 / 256, 1.0])
dark_orange = np.array([255 / 256, 150 / 256, 10 / 256, 1.0])
light_orange = np.array([239 / 256, 136 / 256, 0 / 256, 1.0])

mapping = np.linspace(mesh['scalars'].min(), mesh['scalars'].max(), 256)
newcolors = np.empty((256, 4))
newcolors[mapping < -50] = dark_orange
newcolors[mapping < -55] = orange
newcolors[mapping < -80] = light_orange

my_colormap = ListedColormap(newcolors)
plotter.add_mesh(mesh, scalars="scalars", cmap=my_colormap, show_scalar_bar=False)
# plotter.add_background_image("background.png")
plotter.background_color = np.array([0, 0, 0, 1.0])

camera = pyvista.Camera()
camera.position = (-90.0, 70.0, 130.0)
camera.focal_point = (-15.0, -40.0, 20.0)

plotter.camera = camera

light = pyvista.Light()
light.SetPosition(-110.0, 70.0, 130.0)
light.SetColor(1.0, 1.0, 1.0)
light.SetIntensity(1.0)

plotter.add_light(light)
plotter.show_axes()

plotter.show()
