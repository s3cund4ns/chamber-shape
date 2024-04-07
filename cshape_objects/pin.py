from dataclasses import dataclass

from PySide6.QtWidgets import QTreeWidgetItem

from cshape_objects.cshape_object import CShapeObject, CShapeObjectTypes, CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.material import Material


@dataclass
class Properties(CShapeObjectProperties):
    Name = 'Name'
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
        self.universe = None
        self.name: str = 'NewPin'
        self.all_materials: list[Material] = []
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

    def get_data(self):
        regions: list = []
        for region in self.material_regions:
            material_name = region[0].get_name()
            radius = region[1]
            regions.append([material_name, radius])

        all_materials: list[str] = []
        for material in self.all_materials:
            all_materials.append(f'{material.get_name()}')

        return {self.properties.Name: (CShapeTypes.String, self.name),
                self.properties.Regions: (CShapeTypes.CompositeItems, [regions, all_materials])}

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case self.properties.Name:
                name = value
                self.name = name
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


