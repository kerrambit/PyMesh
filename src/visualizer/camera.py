import pyvista
from .coordinate import Coordinate

class Camera():
    
    def __init__(self, position: Coordinate, focal_point: Coordinate) -> None:
        self.camera = pyvista.Camera()
        self.camera.position = position.get_as_tuple()
        self.camera.focal_point = focal_point.get_as_tuple()