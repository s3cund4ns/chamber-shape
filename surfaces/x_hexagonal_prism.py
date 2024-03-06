from dataclasses import dataclass
from typing import Set, Dict

from surfaces.surface import SurfacesTypes, Surface

import numpy as np


@dataclass
class Properties:
    Object = 'Object'
    Position = 'Position'
    HalfWidth = 'HalfWidth'


class XHexagonalPrism(Surface):
    def __init__(self):
        super().__init__()
        self.type = SurfacesTypes.XHexagonalPrism
        self.half_width: float = 5.0

    def set_parameters(self, parameters: list):
        self.parameters_values = parameters

    def set_half_width(self, half_width: float):
        self.half_width = half_width

    def get_half_width(self) -> float:
        return self.half_width

    def get_data(self):
        return {Properties.Position: list(self.position), Properties.HalfWidth: self.half_width}

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case Properties.Position:
                self.position[0:3] = value
            case Properties.HalfWidth:
                self.half_width = value





