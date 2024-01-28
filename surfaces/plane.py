from typing import Set, Dict

from surfaces.surface import SurfacesTypes, Surface

import numpy as np


class Plane(Surface):
    def __init__(self, position: list[float, float, float], color: list[float, float, float, float]):
        super().__init__(position, color)
        self.type = SurfacesTypes.Plane
        self.parameters_names = []
        self.parameters_values = []

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





