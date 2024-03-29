from dataclasses import dataclass

from PySide6.QtWidgets import QTreeWidgetItem

from cshape_objects.cshape_object import CShapeObject, CShapeObjectTypes, CShapeObjectProperties


@dataclass
class Properties(CShapeObjectProperties):
    pass


class Pin(CShapeObject):
    def __init__(self):
        super().__init__()
        self.type = CShapeObjectTypes.Pin
        self.properties = Properties()
        self.universe = None
        self.name: str = 'NewPin'
        self.material_regions = []

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

