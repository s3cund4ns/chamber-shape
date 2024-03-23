from dataclasses import dataclass

from cshape_objects.cshape_object import CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.surfaces.surface import SurfacesTypes, Surface

import numpy as np



@dataclass
class Properties(CShapeObjectProperties):
    Object = 'Object'
    Name = 'Name'
    Position = 'Position'


class Plane(Surface):
    def __init__(self):
        super().__init__()
        self.surface_type = SurfacesTypes.Plane
        self.properties = Properties()

        self.vertices = np.array((
            np.array([-0.5, 0.5, 0.0], dtype=np.float32),
            np.array([-0.5, -0.5, 0.0], dtype=np.float32),
            np.array([0.5, -0.5, 0.0], dtype=np.float32),
            np.array([0.5, 0.5, 0.0], dtype=np.float32)
        ), dtype=np.float32)

        self.indices = np.array((
            0, 1, 2,
            0, 2, 3
        ), dtype=np.uint32)

    def set_parameters(self, parameters: list):
        pass

    def get_data(self):
        return {self.properties.Name: (CShapeTypes.String, self.name),
        self.properties.Position: (CShapeTypes.Vector3DFloat, list(np.array(self.position, dtype=float)))}

    def set_data(self, properties: tuple):
        print(properties)
        name, value = properties
        match name:
            case self.properties.Name:
                name = value
                self.name = name
            case Properties.Position:
                self.position[0:3] = value
