from dataclasses import dataclass

from cshape_objects.cshape_object import CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.surfaces.surface import SurfacesTypes, Surface

import numpy as np


@dataclass
class Properties(CShapeObjectProperties):
    Object = 'Object'
    Name = 'Name'
    Distance = 'Distance (Y-axis)'
    Size = 'Size'


class YPlane(Surface):
    def __init__(self):
        super().__init__()
        self.surface_type = SurfacesTypes.YPlane
        self.properties = Properties()
        self.distance = 0.0
        self.size = np.array([100.0, 100.0], dtype=np.float32)

    def set_parameters(self, parameters: list):
        pass

    def get_data(self):
        return {self.properties.Name: (CShapeTypes.String, self.name),
                self.properties.Distance: (CShapeTypes.Float, [self.distance, (-99999.9999, 99999.9999)]),
                self.properties.Size: (
                CShapeTypes.Vector2DFloat, [list(np.array(self.size, dtype=float)), (1.0, 99999.9999)])
                }

    def set_data(self, properties: tuple):
        print(properties)
        name, value = properties
        match name:
            case self.properties.Name:
                name = value
                self.name = name
            case Properties.Distance:
                self.distance = value
                self.position[1] = value
            case self.properties.Size:
                self.size[0:2] = value
