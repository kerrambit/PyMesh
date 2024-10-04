import numpy as np


class Color:

    def __init__(self, red: float, green: float, blue: float, alpha: float) -> None:
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def __init__(self, red: float, green: float, blue: float) -> None:
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = 256

    def get_normalized_color_array(self) -> np.ndarray[float]:
        return np.array(
            [self.red / 256, self.green / 256, self.blue / 256, self.alpha / 256]
        )
