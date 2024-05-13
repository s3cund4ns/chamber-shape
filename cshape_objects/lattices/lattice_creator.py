from cshape_objects.lattices.square_lattice import SquareLattice
from cshape_objects.lattices.lattice import LatticeTypes
from cshape_objects.lattices.x_hexagonal_lattice import XHexagonalLattice

lattices = {
    LatticeTypes.SquareLattice: SquareLattice,
    LatticeTypes.XHexagonalLattice: XHexagonalLattice
}


def create_lattice(lattice):
    return lattices[lattice]()
