from random import randint

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Sequence

import numpy as np

from cshape_objects.cshape_object import CShapeObject, CShapeObjectTypes, CShapeObjectProperties


@dataclass
class CShapeObjects:
    Material = 'Material'
    Surface = 'Surface'


@dataclass
class SurfacesTypes:
    NoneType = None
    XPlane = 'XPlane'
    YPlane = 'YPlane'
    ZPlane = 'ZPlane'
    XCylinder = 'XCylinder'
    YCylinder = 'YCylinder'
    ZCylinder = 'ZCylinder'
    Sphere = 'Sphere'
    Cone = 'Cone'
    XTorus = 'XTorus'
    YTorus = 'YTorus'
    ZTorus = 'ZTorus'
    TriangularPrism = 'TriangularPrism'
    RectangularPrism = 'RectangularPrism'
    YHexagonalPrism = 'YHexagonalPrism'
    OctagonalPrism = 'OctagonalPrism'
    DodecagonalPrism = 'DodecagonalPrism'

    Default = ZPlane

    def get(self) -> Sequence[str]:
        return [self.XPlane, self.YPlane, self.ZPlane,
                self.XCylinder, self.YCylinder, self.ZCylinder,
                self.Sphere, self.Cone,
                self.XTorus, self.YTorus, self.ZTorus,
                self.TriangularPrism, self.RectangularPrism,
                self.YHexagonalPrism, self.OctagonalPrism, self.DodecagonalPrism]

    def get_field_name_by_value(self, value):
        for attr_name, attr_value in self.__dict__.items():
            if attr_value == value:
                return attr_name
        return None


@dataclass
class Properties(CShapeObjectProperties):
    Position = 'Position'
    Color = 'Color'
    Parameters = 'Parameters'

    def get(self):
        return [self.Position, self.Color, self.Parameters]


class Surface(CShapeObject):
    def __init__(self):
        super().__init__()
        self.type = CShapeObjectTypes.Surface
        self.surface_type: SurfacesTypes = SurfacesTypes.NoneType
        self.name: str = 'NewSurface'
        self.position = np.array([0.0, 0.0, 0.0], dtype=np.float32)
        self.color: list = [139, 0, 255]
        self.parameters_names: list = []
        self.parameters_values: list = []

    def set_position(self, position: list[float, float, float]):
        self.position[0:3] = position

    def get_position(self):
        return self.position[0:3]

    def set_color(self, color: list[int, int, int, int]):
        self.color = color

    def get_type(self):
        return self.surface_type

    def get_name(self):
        return self.name

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

    def dump_data(self) -> dict:
        pass
