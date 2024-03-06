from random import randint

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Sequence, List, Any, Type

import numpy as np

from model.model import Model


@dataclass
class CShapeObjects:
    Material = 'Material'
    Surface = 'Surface'



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

    def get_field_name_by_value(self, value):
        for attr_name, attr_value in self.__dict__.items():
            if attr_value == value:
                return attr_name
        return None


@dataclass
class SurfacesProperties:
    Position = 'Position'
    Color = 'Color'
    Parameters = 'Parameters'

    def get(self):
        return [self.Position, self.Color, self.Parameters]


class Surface(ABC):
    def __init__(self):
        super().__init__()
        self.object = CShapeObjects.Surface
        self.type: SurfacesTypes = SurfacesTypes.NoneType
        self.position = np.array([0.0, 0.0, 0.0], dtype=np.float32)
        self.color = np.array([randint(100, 255), randint(100, 255), randint(100, 255), 255], dtype=np.float16)
        self.parameters_names: list = []
        self.parameters_values: list = []

    def set_position(self, position: list[float, float, float]):
        self.position[0:3] = position

    def get_position(self):
        return self.position[0:3]

    def set_color(self, color: list[int, int, int, int]):
        self.color = color

    def get_type(self):
        return self.type

    def get_names(self):
        position_names = ['x', 'y', 'z']
        color_names = ['Red', 'Green', 'Blue', 'Alpha']
        parameters_names = self.parameters_names
        return position_names, color_names, parameters_names

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_data(self, properties):
        pass


    # def get_values(self):
    #     position, color, parameters_values = (self.position, self.color, self.parameters_values)
    #     return position, color, parameters_values
    #
    # def get_properties(self):
    #     return self.type, self.position, self.color, self.parameters_values



