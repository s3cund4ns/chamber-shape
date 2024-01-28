from reactor_elements.material import Material
from surfaces.surface import Surface
from typing import ClassVar



class Cell:
    def __init__(self, name: str, universe, fill):
        self.name: str = name
        self.universe: Cell = universe
        self.fill: Material | Cell = fill
        self.special_entires: ClassVar = ['void', 'outside']
        self.surfaces: list[Surface] = []

    def set_name(self, name: str):
        self.name = name

    def set_universe(self, universe):
        self.universe = universe

    def fill(self, fill):
        self.fill = fill

    def add_surface(self, surface: Surface):
        self.surfaces.append(surface)

    def delete_surface(self, surface: Surface):
        self.surfaces.remove(surface)
