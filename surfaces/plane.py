from dataclasses import dataclass
from typing import Set, Dict

from PySide6.Qt3DCore import Qt3DCore
from PySide6.Qt3DExtras import Qt3DExtras

from surfaces.surface import SurfacesTypes, Surface

import numpy as np


@dataclass
class Properties:
    Object = 'Object'
    Position = 'Position'


class Plane(Surface):
    def __init__(self):
        super().__init__()
        self.type = SurfacesTypes.Plane

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
        return {Properties.Position: list(self.position)}

    def set_data(self, properties: tuple):
        print(properties)
        name, value = properties
        match name:
            case Properties.Position:
                self.position[0:3] = value
