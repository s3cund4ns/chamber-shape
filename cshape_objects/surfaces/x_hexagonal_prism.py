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
    HalfWidth = 'HalfWidth'


class XHexagonalPrism(Surface):
    def __init__(self):
        super().__init__()
        self.surface_type = SurfacesTypes.XHexagonalPrism
        self.properties = Properties()
        self.half_width: float = 5.0

    def set_parameters(self, parameters: list):
        self.parameters_values = parameters

    def set_half_width(self, half_width: float):
        self.half_width = half_width

    def get_half_width(self) -> float:
        return self.half_width

    def get_data(self):
        return {self.properties.Name: (CShapeTypes.String, self.name),
            Properties.Position: (CShapeTypes.Vector3DFloat, list(np.array(self.position, dtype=float))),
                Properties.HalfWidth: (CShapeTypes.Float, self.half_width)}

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case self.properties.Name:
                name = value
                self.name = name
            case Properties.Position:
                self.position[0:3] = value
            case Properties.HalfWidth:
                self.half_width = value





