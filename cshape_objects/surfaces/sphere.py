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


class Sphere(Surface):
    def __init__(self):
        super().__init__()
        self.surface_type = SurfacesTypes.Sphere
        self.properties = Properties()
        self.radius: float = 5.0

    def set_parameters(self, parameters: list):
        self.parameters_values = parameters

    def set_radius(self, radius: float):
        self.radius = radius

    def get_radius(self) -> float:
        return self.radius

    def get_data(self):
        return {self.properties.Name: (CShapeTypes.String, self.name),
                Properties.Position: (CShapeTypes.Vector3DFloat, [list(np.array(self.position, dtype=float)), (-99999.9999, 99999.9999)]),
                Properties.Radius: (CShapeTypes.Float, [self.radius, (0.0001, 99999.9999)])}

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case self.properties.Name:
                name = value
                self.name = name
            case Properties.Position:
                self.position[0:3] = value
            case Properties.Radius:
                self.radius = value
