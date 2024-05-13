from dataclasses import dataclass
from typing import Sequence

import numpy as np

from cshape_objects.cshape_object import CShapeObject, CShapeObjectTypes
from cshape_objects.pin import Pin
from cshape_objects.universe import Universe


@dataclass
class LatticeTypes:
    NoneType = None
    SquareLattice = 'SquareLattice'
    XHexagonalLattice = 'XHexagonalLattice'
    YHexagonalLattice = 'YHexagonalLattice'

    def get(self) -> Sequence[str]:
        return [self.SquareLattice, self.XHexagonalLattice, self.YHexagonalLattice]


class Lattice(CShapeObject):
    def __init__(self):
        super().__init__()
        self.type: str = CShapeObjectTypes.Lattice
        self.lattice_type = LatticeTypes.NoneType
        self.name: str
        self.universe: Universe | None = None
        self.position = np.array([0.0, 0.0, 0.0], dtype=np.float32)
        self.all_pins: list[Pin] = []
        self.all_universes: list[Universe] = []

    def get_type(self):
        return self.lattice_type

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_size(self):
        pass

    def get_universe_matrix(self):
        return self.universes_matrix

    def set_universe_number(self, universe_number: int):
        self.universe_number = universe_number

    def get_universe_number(self):
        return self.universe_number

    def get_position(self):
        return self.position

    def set_x_number(self, x_number: int):
        self.x_number = x_number
        self.universes_matrix.resize(self.x_number, self.y_number)

    def get_x_number(self):
        return self.x_number

    def set_y_number(self, y_number: int):
        self.y_number = y_number
        self.universes_matrix.resize(self.x_number, self.y_number)

    def get_y_number(self):
        return self.y_number

    def set_pitch(self, pitch: float):
        self.pitch = pitch

    def get_pitch(self):
        return self.pitch

    def get_universe_position(self, x_number: int, y_number: int):
        pass

    def get_universe_from_matrix(self, x_number: int, y_number: int):
        return self.universes_matrix[y_number][x_number]

    def set_universe_in_matrix(self, row, column, universe):
        self.universes_matrix[row][column] = universe

    def get_universe_index(self):
        if self.universe is None:
            return ''
        else:
            return self.universe.get_index()

    def set_data(self, data):
        pass

    def get_data(self):
        pass

    def dump_data(self) -> dict:
        pass
