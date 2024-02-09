from dataclasses import dataclass

import numpy as np
from PySide6.QtWidgets import QTreeWidgetItem

from preprocessor.cell import Cell
from preprocessor.pin import Pin


@dataclass
class UniverseElementsTypes:
    NoneType = None
    Cell = 'Cell'
    Lattice = 'Lattice'


@dataclass
class UniverseProperties:
    Position = 'Position'
    Elements = 'Elements'

    def get(self):
        return [self.Position, self.Elements]


class Universe(QTreeWidgetItem):
    def __init__(self, text: str, id: int, parent=None):
        super().__init__(parent)
        self.position = np.array([0.0, 0.0, 0.0], dtype=np.float32)
        self.elements: list[Cell | Pin] = []

        self.setText(0, text)
        self.setText(1, str(id))

    def add_element(self, element: Cell):
        self.elements.append(element)

    def delete_element(self, element_id):
        self.elements.pop(element_id)

    def get_names(self):
        position_names = ['x', 'y', 'z']
        return position_names

    def get_values(self):
        return self.position, self.elements
