from dataclasses import dataclass

from cshape_objects.cshape_object import CShapeObject, CShapeObjectTypes, CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes


@dataclass
class Properties(CShapeObjectProperties):
    Name = 'Name'
    Density = 'Density'
    Mode = 'Mode'
    Nuclides = 'Nuclides'
    Add = 'Add'
    Delete = 'Delete'


@dataclass
class Mode:
    Atomic = 'Atomic'
    Massive = 'Massive'
    Summary = 'Summary'


class Material(CShapeObject):
    def __init__(self):
        super().__init__()
        self.type = CShapeObjectTypes.Material
        self.name: str = 'NewMaterial'
        self.properties = Properties()
        self.density: float = 0.0
        self.modes: dict = {'Atomic': 'Atomic', 'Massive': 'Massive', 'Summary': 'Summary'}
        self.mode = self.modes['Atomic']
        self.nuclides: list[list[str | float]] = []

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def set_density(self, density: float):
        self.density = density

    def get_density(self):
        return self.density

    def add_nuclide(self):
        self.nuclides.append(['NewNuclide', 0.0])

    def delete_nuclide(self, nuclide_id: int):
        self.nuclides.pop(nuclide_id)

    def get_nuclide(self, index):
        return self.nuclides[index]

    def set_nuclide(self, index, name: str, density: float):
        self.nuclides[index] = [name, density]

    def get_nuclides(self):
        return self.nuclides

    def get_nuclides_count(self):
        return len(self.nuclides)

    def get_data(self):
        return {self.properties.Name: (CShapeTypes.String, self.name),
                self.properties.Density: (CShapeTypes.Float, self.density),
                self.properties.Mode: (CShapeTypes.Enum, [self.modes, self.mode]),
                self.properties.Nuclides: (CShapeTypes.List, self.nuclides)}

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case self.properties.Name:
                name = value
                self.name = name
            case self.properties.Density:
                density = value
                self.set_density(density)
            case self.properties.Mode:
                mode = value
                self.mode = self.modes[mode]
            case self.properties.Nuclides:
                index, name, density = value
                self.set_nuclide(index, name, density)
            case self.properties.Add:
                index, name, density = value
                self.add_nuclide()
                self.set_nuclide(index, name, density)
            case self.properties.Delete:
                index = value
                self.delete_nuclide(index)