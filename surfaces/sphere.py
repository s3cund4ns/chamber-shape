from dataclasses import dataclass

from PySide6.Qt3DExtras import Qt3DExtras

from surfaces.surface import SurfacesTypes, Surface


@dataclass
class Properties:
    Object = 'Object'
    Position = 'Position'
    Radius = 'Radius'


class Sphere(Surface):
    def __init__(self):
        super().__init__()
        self.type = SurfacesTypes.Sphere
        self.radius: float = 5.0

    def set_parameters(self, parameters: list):
        self.parameters_values = parameters

    def set_radius(self, radius: float):
        self.radius = radius

    def get_radius(self) -> float:
        return self.radius

    def get_data(self):
        return {Properties.Position: list(self.position), Properties.Radius: self.radius}

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case Properties.Position:
                self.position[0:3] = value
            case Properties.Radius:
                self.radius = value
