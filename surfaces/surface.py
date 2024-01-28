from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Sequence, List, Any, Type

import numpy as np


@dataclass
class SurfacesTypes:
    NoneType = None
    Infinity = 'Infinity'
    Plane = 'Plane'
    Cylinder = 'Cylinder'
    Sphere = 'Sphere'
    Cone = 'Cone'
    XHexagonalPrism = 'XHexagonalPrism'
    YHexagonalPrism = 'YHexagonalPrism'

    Default = Plane

    def get(self) -> Sequence[str]:
        return [self.Infinity, self.Plane, self.Cylinder, self.Sphere, self.Cone, self.XHexagonalPrism,
                self.YHexagonalPrism]


@dataclass
class SurfacesProperties:
    Position = 'Position'
    Color = 'Color'
    Parameters = 'Parameters'

    def get(self):
        return [self.Position, self.Color, self.Parameters]


class Surface(ABC):
    def __init__(self, position: list[float, float, float], color: list[float, float, float, float]):
        self.type: SurfacesTypes = SurfacesTypes.NoneType
        self.position = np.array(position, dtype=np.float32)
        self.color = np.array(color, dtype=np.float16)
        self.parameters_names: list = []
        self.parameters_values: list = []

    def set_position(self, position: list[float, float, float]):
        self.position[0:3] = position

    def set_color(self, color: list[int, int, int, int]):
        self.color = color

    @abstractmethod
    def set_parameters(self, parameters: list):
        pass

    def get_type(self):
        return self.type

    def get_names(self):
        position_names = ['x', 'y', 'z']
        color_names = ['Red', 'Green', 'Blue', 'Alpha']
        parameters_names = self.parameters_names
        return position_names, color_names, parameters_names

    def get_values(self):
        position, color, parameters_values = (self.position, self.color, self.parameters_values)
        return position, color, parameters_values

    def get_properties(self):
        return self.type, self.position, self.color, self.parameters_values


