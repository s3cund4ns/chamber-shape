from abc import ABC, abstractmethod
from dataclasses import dataclass

from cshape_objects.cshape_object import CShapeObject, CShapeObjectTypes, CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.fill_flow import VoidOrOutsideFillFlow, MaterialFillFlow, UniverseFillFlow, FillFlow
from cshape_objects.material import Material
from cshape_objects.surfaces.surface import Surface
from cshape_objects.universe import Universe


@dataclass
class Properties(CShapeObjectProperties):
    Name = 'Name'
    Universe = 'Belongs to universe'
    Fill = 'Fill'
    Set = 'Set'
    Entire = ''
    Color = 'Color'
    Add = 'Add'
    Surfaces = 'Surfaces'
    SurfaceSide = 'SurfaceSide'
    Delete = 'Delete'

    def get(self):
        return [self.Fill, self.Surfaces]


@dataclass
class Entire:
    Void = 'Void'
    Outside = 'Outside'
    Material = 'Material'
    Universe = 'Universe'

    def get(self):
        return [self.Void, self.Outside]


class Cell(CShapeObject):
    def __init__(self):
        super().__init__()
        self.type = CShapeObjectTypes.Cell
        self.properties = Properties()
        self.name: str = 'NewCell'
        self.universe: Universe | None = None
        self.all_elements = []
        self.all_materials = []
        self.all_universes = []
        self.entires: dict = {'Void': 'Void', 'Outside': 'Outside', 'Material': 'Material', 'Universe': 'Universe'}
        self.fill: str = self.entires['Void']
        self.fill_flows: dict = {
            Entire.Void: VoidOrOutsideFillFlow,
            Entire.Outside: VoidOrOutsideFillFlow,
            Entire.Material: MaterialFillFlow,
            Entire.Universe: UniverseFillFlow
        }
        self.fill_flow: FillFlow = self.__create_fill_flow()
        self.entire = 'Empty'
        self.color: list[int] = [255, 255, 255]
        self.surfaces: list = []
        self.surface_side: tuple = ('In', 'Out')

    def __create_fill_flow(self):
        return self.fill_flows[self.fill](self.all_materials, self.all_universes)

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

    def get_entire(self):
        if self.entire == 'Empty':
            return self.entire
        if type(self.entire) is Material:
            return self.entire.get_name()
        else:
            return self.all_universes.index(self.entire)

    def get_surfaces_indices(self):
        indices = []
        for surface in self.surfaces:
            indices.append([self.all_elements.index(surface[0]), surface[1]])
        return indices

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

    def dump_surfaces(self):
        surfaces = []
        for surface in self.surfaces:
            surface_index = self.all_elements.index(surface[0])
            surfaces.append([surface_index, surface[1]])
        return surfaces


    def get_universe_index(self):
        if self.universe is None:
            return ''
        else:
            return self.universe.get_index()

    def get_data(self):
        all_universes = []
        for universe in self.all_universes:
            all_universes.append(str(universe.get_index()))

        surfaces: list = []
        for surface in self.surfaces:
            surface_object, surface_side = surface
            surface_info = [surface_object.get_type(), surface_object.get_name(), surface_side]
            surfaces.append(surface_info)

        all_elements: list[str] = []
        for element in self.all_elements:
            if ([element, 'In'] in self.surfaces) or ([element, 'Out'] in self.surfaces):
                continue
            all_elements.append(f'{self.all_elements.index(element)} {element.get_type()} {element.get_name()}')

        self.properties.Entire = self.fill_flow.get_fill_name()
        entire = self.fill_flow.get_entire((CShapeTypes.Reference, self.entire))

        return {self.properties.Name: (CShapeTypes.String, self.name),
                self.properties.Universe: (CShapeTypes.Reference, [str(self.get_universe_index()), all_universes]),
                self.properties.Fill: (CShapeTypes.Enum, [self.entires, self.fill]),
                self.properties.Entire: entire,
                self.properties.Color: (CShapeTypes.Color, self.color),
                self.properties.Surfaces: (CShapeTypes.CompositeList, [surfaces, all_elements])}

    def set_data(self, parameters: dict):
        name, value = parameters
        match name:
            case self.properties.Name:
                self.name = value
            case self.properties.Universe:
                index = value
                self.universe = self.all_universes[index]
            case self.properties.Fill:
                fill = value
                self.fill = self.entires[fill]
                self.fill_flow = self.__create_fill_flow()
            case self.properties.Entire:
                index = value
                self.entire = self.fill_flow.set_entire(index)
            case self.properties.Color:
                self.color = value
            case self.properties.Add:
                surface_index, surface_side = value
                surface = self.all_elements[surface_index]
                self.surfaces.append([surface, surface_side])
            case self.properties.SurfaceSide:
                surface_index, surface_side = value
                self.surfaces[surface_index][1] = surface_side
            case self.properties.Delete:
                index = value
                self.surfaces.pop(index)

    def dump_data(self) -> dict:
        return {
            self.properties.Name: self.name,
            self.properties.Universe: self.get_universe_index(),
            self.properties.Fill: self.fill,
            self.properties.Entire: self.get_entire(),
            self.properties.Surfaces: self.dump_surfaces()
        }
