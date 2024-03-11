from dataclasses import dataclass

from cshape_objects.cshape_object import CShapeObject, CShapeObjectTypes, CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.material import Material
from cshape_objects.surfaces.surface import Surface


@dataclass
class Properties(CShapeObjectProperties):
    Name = 'Name'
    Fill = 'Fill'
    Surfaces = 'Surfaces'
    SurfaceSide = 'SurfaceSide'

    def get(self):
        return [self.Fill, self.Surfaces]


@dataclass
class SpecialEntires:
    Void = 'Void'
    Outside = 'Outside'

    def get(self):
        return [self.Void, self.Outside]


class Cell(CShapeObject):
    def __init__(self):
        super().__init__()
        self.type = CShapeObjectTypes.Cell
        self.properties = Properties()
        self.name: str = 'NewCell'
        self.universe_number: int = 0
        self.entires: dict = {'Void': 'Void', 'Outside': 'Outside'}
        self.fill: str = self.entires['Void']
        self.surfaces: list[list[Surface | str]] = []
        self.surface_side: tuple = ('In', 'Out')

    def get_type(self):
        return self.type

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def set_universe_number(self, number: int):
        self.universe_number = number

    def set_fill(self, fill):
        self.fill = fill

    def get_fill(self):
        return self.fill

    def get_fill_name(self):
        if type(self.fill) is str:
            return self.fill
        elif type(self.fill) is Material:
            material: Material = self.fill
            return material.get_name()

    def add_surface(self, surface: Surface):
        self.surfaces.append([surface, -1])

    def delete_surface(self, surface: Surface):
        self.surfaces.remove(surface)

    def set_surface_side(self, index, side: int):
        self.surfaces[index][1] = side

    def get_surfaces(self):
        return self.surfaces

    def get_data(self):
        return {self.properties.Name: (CShapeTypes.String, self.name),
                self.properties.Fill: (CShapeTypes.Enum, [self.entires, self.fill]),
                self.properties.Surfaces: (CShapeTypes.Table, self.surfaces)}

    def set_data(self, parameters: dict):
        name, value = parameters
        match name:
            case self.properties.Name:
                self.name = value
            case self.properties.Fill:
                fill = value
                self.fill = self.entires[fill]
