from dataclasses import dataclass

import numpy as np

from cshape_objects.cshape_object import CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.surfaces.surface import Surface, SurfacesTypes


@dataclass
class Properties(CShapeObjectProperties):
    Object = 'Object'
    Name = 'Name'
    Position = 'Position'
    MinorRadius = 'Minor radius'
    MajorRadius = 'Major radius'


class ZTorus(Surface):
    def __init__(self):
        super().__init__()
        self.surface_type = SurfacesTypes.ZTorus
        self.properties = Properties()
        self.minor_radius: float = 5.0
        self.major_radius: float = 5.0

    def get_data(self):
        return {
            self.properties.Name: (CShapeTypes.String, self.name),
            self.properties.Position: (CShapeTypes.Vector3DFloat, [list(np.array(self.position, dtype=float)), (-99999.9999, 99999.9999)]),
            self.properties.MinorRadius: (CShapeTypes.Float, [self.minor_radius, (0.0001, 99999.9999)]),
            self.properties.MajorRadius: (CShapeTypes.Float, [self.major_radius, (0.0001, 99999.9999)])
        }

    def set_data(self, properties: tuple):
        name, value = properties
        match name:
            case self.properties.Name:
                name = value
                self.name = name
            case self.properties.Position:
                self.position[0:3] = value
            case self.properties.MinorRadius:
                self.minor_radius = value
            case self.properties.MajorRadius:
                self.major_radius = value
