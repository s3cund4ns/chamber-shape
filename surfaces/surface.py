from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Sequence


@dataclass
class SurfacesTypes:
    NoneType = None
    Infinity = 'Infinity'
    Plane = 'Plane'
    Cylinder = 'Cylinder'
    Sphere = 'Sphere'
    Cone = 'Cone'

    Default = Plane

    def get(self) -> Sequence[str]:
        return [self.Infinity, self.Plane, self.Cylinder, self.Sphere, self.Cone]



@dataclass
class SurfacesProperties:
    Position = 'Position'
    Rotation = 'Rotation'
    Parameters = 'Parameters'

    def get(self):
        return [self.Position, self.Rotation, self.Parameters]


class Surface(ABC):
    def __init__(self, pos_x, pos_y, pos_z, rot_x, rot_y, rot_z):
        self.position: dict = {'x': pos_x, 'y': pos_y, 'z': pos_z}
        self.rotation: dict = {'x': rot_x, 'y': rot_y, 'z': rot_z}
        self.type: SurfacesTypes = SurfacesTypes.NoneType
        self.parameters: dict = {}

    @abstractmethod
    def set_properties(self, position: list, rotation: list, parameters: list):
        pass

    def get_type(self):
        return self.type

    def get_names(self):
        position_names = list(self.position.keys())
        rotation_names = list(self.rotation.keys())
        parameters_names = list(self.parameters.keys())
        return position_names, rotation_names, parameters_names

    def get_values(self):
        position, rotation, parameters = (list(self.position.values()), list(self.rotation.values()),
                                          list(self.parameters.values()))
        return position, rotation, parameters

    def get_properties(self):
        return self.type, self.position, self.rotation, self.parameters

