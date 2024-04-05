from abc import ABC, abstractmethod
from dataclasses import dataclass

from cshape_objects.cshape_object import CShapeObject, CShapeObjectTypes, CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.material import Material
from cshape_objects.surfaces.surface import Surface
from cshape_objects.universe import Universe


@dataclass
class Properties(CShapeObjectProperties):
    Name = 'Name'
    Fill = 'Fill'
    Set = 'Set'
    Entire = ''
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


class FillFlow(ABC):
    def __init__(self, all_materials: list, all_universes: list):
        self.all_materials: list[Material] = all_materials
        self.all_universes: list[Universe] = all_universes

    @abstractmethod
    def get_entire_name(self) -> str:
        pass

    @abstractmethod
    def get_entire(self, entire: tuple) -> tuple:
        pass

    @abstractmethod
    def set_entire(self, index):
        pass


class VoidFillFlow(FillFlow):
    def __init__(self, all_materials: list, all_universes: list):
        super().__init__(all_materials, all_universes)

    def get_entire_name(self) -> str:
        return ''

    def get_entire(self, entire) -> tuple:
        return CShapeTypes.Reference, None

    def set_entire(self, index):
        pass


class OutsideFillFlow(FillFlow):
    def __init__(self, all_materials: list, all_universes: list):
        super().__init__(all_materials, all_universes)

    def get_entire_name(self) -> str:
        return ''

    def get_entire(self, entire) -> tuple:
        return CShapeTypes.Reference, None

    def set_entire(self, index):
        pass


class MaterialFillFlow(FillFlow):
    def __init__(self, all_materials: list, all_universes: list):
        super().__init__(all_materials, all_universes)

    def get_entire_name(self) -> str:
        return 'Material'

    def get_entire(self, entire) -> tuple:
        entire_tuple = entire
        current_material = entire_tuple[1]

        materials_info: list = []
        for material in self.all_materials:
            material = f'{material.get_name()} {material.get_density()}'
            materials_info.append(material)

        current_material_info = ''
        if current_material != 'Empty':
            current_material_info = f'{current_material.get_name()} {current_material.get_density()}'

        return (entire_tuple[0], [current_material_info, materials_info])

    def set_entire(self, index):
        return self.all_materials[index]


class UniverseFillFlow(FillFlow):
    def __init__(self, all_materials: list, all_universes: list):
        super().__init__(all_materials, all_universes)

    def get_entire_name(self) -> str:
        return 'Universe'

    def get_entire(self, entire) -> tuple:
        entire_tuple = entire
        current_universe = entire_tuple[1]

        universes_info: list = []
        for universe in self.all_universes:
            universe = f'{self.all_universes.index(universe)}'
            universes_info.append(universe)

        current_universe_info = ''
        if current_universe != 'Empty':
            current_universe_info = f'{self.all_universes.index(current_universe)}'

        return (entire_tuple[0], [current_universe_info, universes_info])

    def set_entire(self, index):
        return self.all_universes[index]


class Cell(CShapeObject):
    def __init__(self):
        super().__init__()
        self.type = CShapeObjectTypes.Cell
        self.properties = Properties()
        self.name: str = 'NewCell'
        self.universe_number: int = 0
        self.all_elements = []
        self.all_materials = []
        self.all_universes = []
        self.entires: dict = {'Void': 'Void', 'Outside': 'Outside', 'Material': 'Material', 'Universe': 'Universe'}
        self.fill: str = self.entires['Void']
        self.fill_flows: dict = {
            Entire.Void: VoidFillFlow,
            Entire.Outside: OutsideFillFlow,
            Entire.Material: MaterialFillFlow,
            Entire.Universe: UniverseFillFlow
        }
        self.fill_flow: FillFlow = self.__create_fill_flow()
        self.entire = 'Empty'
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

        self.properties.Entire = self.fill_flow.get_entire_name()
        entire = self.fill_flow.get_entire((CShapeTypes.Reference, self.entire))

        return {self.properties.Name: (CShapeTypes.String, self.name),
                self.properties.Fill: (CShapeTypes.Enum, [self.entires, self.fill]),
                self.properties.Entire: entire,
                self.properties.Surfaces: (CShapeTypes.CompositeList, [surfaces, all_elements])}

    def set_data(self, parameters: dict):
        name, value = parameters
        match name:
            case self.properties.Name:
                self.name = value
            case self.properties.Fill:
                fill = value
                self.fill = self.entires[fill]
                self.fill_flow = self.__create_fill_flow()
                self.entire = 'Empty'
            case self.properties.Set:
                index = value
                self.entire = self.fill_flow.set_entire(index)
                print(self.entire)
            case self.properties.Add:
                surface_index, surface_side = value
                print(surface_index, surface_side)
                surface = self.all_elements[surface_index]
                self.surfaces.append([surface, surface_side])
            case self.properties.SurfaceSide:
                surface_index, surface_side = value
                self.surfaces[surface_index][1] = surface_side
            case self.properties.Delete:
                index = value
                self.surfaces.pop(index)
