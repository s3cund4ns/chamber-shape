from typing import Set, Dict

from surfaces.surface import SurfacesTypes, Surface

import numpy as np


class XHexagonalPrism(Surface):
    def __init__(self, position: list[float, float, float], color: list[float, float, float, float], half_width):
        super().__init__(position, color)
        self.type = SurfacesTypes.XHexagonalPrism
        self.parameters_names = ['half_width']
        self.parameters_values = [half_width]

    def set_parameters(self, parameters: list):
        self.parameters_values = parameters





