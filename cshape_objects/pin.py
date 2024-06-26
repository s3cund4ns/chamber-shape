from dataclasses import dataclass

from PySide6.QtWidgets import QTreeWidgetItem

from cshape_objects.cshape_object import CShapeObject, CShapeObjectTypes, CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.material import Material
from cshape_objects.universe import Universe


@dataclass
class Properties(CShapeObjectProperties):
    Name = 'Name'
    Universe = 'Belongs to universe'
    Regions = 'Regions'
    Add = 'Add'
    Change = 'Change'
    Set = 'Set'
    Delete = 'Delete'


class Pin(CShapeObject):
    def __init__(self):
        super().__init__()
        self.type = CShapeObjectTypes.Pin
        self.properties = Properties()
        self.universe: Universe | None = None
        self.name: str = 'NewPin'
        self.all_materials: list[Material] = []
        self.all_universes: list[Universe] = []
        self.material_regions: list = []

    def get_type(self):
        return self.type

    def set_universe(self, universe):
        self.universe = universe

    def get_universe(self):
        return self.universe

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def get_materials_indices(self):
        indices = []
        for region in self.material_regions:
            indices.append([self.all_materials.index(region[0]), region[1]])
        return indices

    def add_region(self, material):
        self.material_regions.append([material, None])

    def set_region(self, index, radius):
        if index == len(self.material_regions)-1:
            return
        else:
            self.material_regions[index][1] = radius

    def get_regions(self):
        return self.material_regions

    def get_regions_count(self):
        return len(self.material_regions)

    def dump_regions(self):
        regions = []
        for region in self.material_regions:
            material_index = self.all_materials.index(region[0])
            regions.append([material_index, region[1]])
        return regions

    def get_universe_index(self):
        if self.universe is None:
            return ''
        else:
            return self.universe.get_index()

    def get_data(self):
        all_universes = []
        for universe in self.all_universes:
            all_universes.append(str(universe.get_index()))

        regions: list = []
        for region in self.material_regions:
            material_name = region[0].get_name()
            radius = region[1]
            regions.append([material_name, radius])

        all_materials: list[str] = []
        for material in self.all_materials:
            all_materials.append(f'{material.get_name()}')

        return {self.properties.Name: (CShapeTypes.String, self.name),
                self.properties.Universe: (CShapeTypes.Reference, [str(self.get_universe_index()), all_universes]),
                self.properties.Regions: (CShapeTypes.CompositeItems, [regions, all_materials])}

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case self.properties.Name:
                name = value
                self.name = name
            case self.properties.Universe:
                index = value
                if index == '':
                    return
                self.universe = self.all_universes[index]
            case self.properties.Add:
                index = value
                self.material_regions.append([self.all_materials[index], 0.0])
            case self.properties.Change:
                region_index, index_in_all_materials = value
                self.material_regions[region_index][0] = self.all_materials[index_in_all_materials]
            case self.properties.Set:
                region_index, radius = value
                self.material_regions[region_index][1] = radius
            case self.properties.Delete:
                index = value
                self.material_regions.pop(index)

    def dump_data(self):
        return {
            self.properties.Name: self.name,
            self.properties.Universe: self.get_universe_index(),
            self.properties.Regions: self.dump_regions()
        }


