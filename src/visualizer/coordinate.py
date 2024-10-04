from typing import Tuple, List


class Coordinate:

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def get_as_tuple(self) -> Tuple[float, float, float]:
        return self.x, self.y, self.z

    def get_as_array(self) -> List[float]:
        return [self.x, self.y, self.z]
