from dataclasses import dataclass

import numpy as np

from cshape_objects.cshape_object import CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.surfaces.surface import SurfacesTypes, Surface


@dataclass
class Properties(CShapeObjectProperties):
    Object = 'Object'
    Name = 'Name'
    Position = 'Position'
    Radius = 'Radius'
    Length = 'Length'
    Color = 'Color'


class YCylinder(Surface):
    def __init__(self):
        super().__init__()
        self.surface_type = SurfacesTypes.YCylinder
        self.properties = Properties()
        self.center_position = np.array([0.0, 0.0], dtype=np.float32)
        self.radius: float = 5.0
        self.length: float = 50.0

    def set_parameters(self, parameters: list):
        self.parameters_values = parameters

    def set_radius(self, radius: float):
        self.radius = radius

    def get_data(self):
        return {self.properties.Name: (CShapeTypes.String, self.name),
                Properties.Position: (
                CShapeTypes.Vector2DFloat, [list(np.array(self.center_position, dtype=float)), (-99999.9999, 99999.9999)]),
                Properties.Radius: (CShapeTypes.Float, [self.radius, (0.0001, 99999.9999)]),
                Properties.Length: (CShapeTypes.Float, [self.length, (0.0001, 99999.9999)]),
                self.properties.Color: (CShapeTypes.Color, self.color)
                }

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case self.properties.Name:
                name = value
                self.name = name
            case Properties.Position:
                self.center_position[0:2] = value
                self.position[0] = self.center_position[0]
                self.position[2] = self.center_position[1]
            case Properties.Radius:
                self.radius = value
            case Properties.Length:
                self.length = value
            case Properties.Color:
                self.color = value

    def dump_data(self) -> dict:
        return {
            'Type': self.surface_type,
            self.properties.Name: self.name,
            self.properties.Position: list(np.array(self.center_position, dtype=float)),
            self.properties.Radius: self.radius,
            self.properties.Length: self.length,
            self.properties.Color: self.color
        }
