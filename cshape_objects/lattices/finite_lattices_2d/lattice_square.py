import numpy as np

from cshape_objects.lattices.finite_lattices_2d.finite_lattice_2d import FiniteLattice2D
from cshape_objects.lattices.lattice import Lattice, LatticeTypes, Lattices


class LatticeSquare(FiniteLattice2D):
    def __init__(self):
        super().__init__()
        self.name: str = 'NewLatticeSquare'
        self.lattice_type: int = Lattices.LatticeSquare

    def get_universe_position(self, x_number: int, y_number: int):
        x_position = self.position[0] + x_number * self.pitch
        y_position = self.position[1] - y_number * self.pitch
        return np.array([x_position, y_position, self.position[2]], dtype=np.float32)