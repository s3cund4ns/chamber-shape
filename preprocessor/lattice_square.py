import numpy as np
from PySide6.QtWidgets import QTreeWidgetItem

from preprocessor.lattice import Lattice, LatticeTypes


class LatticeSquare(Lattice):
    def __init__(self, position: list[float, float, float], x_number: int, y_number: int, pitch: float, parent=None):
        super().__init__(position, x_number, y_number, pitch, parent)
        self.type = LatticeTypes.Square

        self.setText(1, 'New Square Lattice')

    def get_universe_position(self, x_number: int, y_number: int):
        x_position = self.position[0] + x_number * self.pitch
        y_position = self.position[1] - y_number * self.pitch
        return np.array([x_position, y_position, self.position[2]], dtype=np.float32)
