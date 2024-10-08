import pyvista
from .coordinate import Coordinate
from .color import Color


class Light:

    def __init__(self, position: Coordinate, color: Color, intensity: float) -> None:
        self.light = pyvista.Light()
        self.light.SetPosition(position.get_as_tuple())
        self.light.SetColor(color.get_rgb_tuple())
        self.light.SetIntensity(intensity)
