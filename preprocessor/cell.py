from dataclasses import dataclass

from PySide6.QtWidgets import QTreeWidgetItem

from preprocessor.material import Material
from surfaces.surface import Surface
from typing import ClassVar


@dataclass
class CellProperties:
    Fill = 'Fill'
    Surfaces = 'Surfaces'

    def get(self):
        return [self.Fill, self.Surfaces]


@dataclass
class SpecialEntires:
    Void = 'Void'
    Outside = 'Outside'

    def get(self):
        return [self.Void, self.Outside]


class Cell(QTreeWidgetItem):
    def __init__(self, name: str, fill, parent=None):
        super().__init__(parent)
        self.type: str = 'Cell'
        self.name: str = name
        self.universe_number: int = 0
        self.fill: str | Material | int = fill
        self.surfaces: list[[Surface | int]] = []

        self.setText(0, 'Cell')
        self.setText(1, name)

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
