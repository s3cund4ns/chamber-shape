from abc import ABC, abstractmethod
from dataclasses import dataclass

import numpy as np
from PySide6.QtWidgets import QTreeWidgetItem

from preprocessor.universe import Universe


@dataclass
class LatticeTypes:
    NoneType = 0
    Square = 1
    XTypeHexagonal = 2
    YTypeHexagonal = 3


class Lattice(QTreeWidgetItem):
    def __init__(self, name: str, position: list[float, float, float], x_number: int, y_number: int, pitch: float, parent=None):
        super().__init__(parent)
        self.type: LatticeTypes = LatticeTypes.NoneType
        self.name: str = name
        self.universe_number: int = 0
        self.position = np.array(position, dtype=np.float32)
        self.x_number: int = x_number
        self.y_number: int = y_number
        self.pitch: float = pitch
        self.universes: list[Universe] = []
        self.universes_matrix = np.array([[-1, -1]], dtype=np.int16)
        self.universes_matrix.resize(self.y_number, self.x_number)
        self.universes_matrix[:] = -1

        self.setText(0, 'Lattice')

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

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

    @abstractmethod
    def get_universe_position(self, x_number: int, y_number: int):
        pass

    def get_universe_from_matrix(self, x_number: int, y_number: int):
        return self.universes_matrix[y_number][x_number]

    def set_universe_in_matrix(self, row, column, universe):
        self.universes_matrix[row][column] = universe
