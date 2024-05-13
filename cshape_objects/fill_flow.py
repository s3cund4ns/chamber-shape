from abc import abstractmethod, ABC

from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.material import Material
from cshape_objects.universe import Universe


class FillFlow(ABC):
    def __init__(self, all_materials: list, all_universes: list):
        self.all_materials: list[Material] = all_materials
        self.all_universes: list[Universe] = all_universes

    @abstractmethod
    def get_fill_name(self) -> str:
        pass

    @abstractmethod
    def get_entire(self, entire: tuple) -> tuple:
        pass

    @abstractmethod
    def set_entire(self, index):
        pass


class VoidOrOutsideFillFlow(FillFlow):
    def __init__(self, all_materials: list, all_universes: list):
        super().__init__(all_materials, all_universes)

    def get_fill_name(self) -> str:
        return ''

    def get_entire(self, entire) -> tuple:
        return CShapeTypes.Reference, None

    def set_entire(self, index):
        pass


class MaterialFillFlow(FillFlow):
    def __init__(self, all_materials: list, all_universes: list):
        super().__init__(all_materials, all_universes)

    def get_fill_name(self) -> str:
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

        return entire_tuple[0], [current_material_info, materials_info]

    def set_entire(self, index):
        return self.all_materials[index]


class UniverseFillFlow(FillFlow):
    def __init__(self, all_materials: list, all_universes: list):
        super().__init__(all_materials, all_universes)

    def get_fill_name(self) -> str:
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

        return entire_tuple[0], [current_universe_info, universes_info]

    def set_entire(self, index):
        return self.all_universes[index]
