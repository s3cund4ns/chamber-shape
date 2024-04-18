from cshape_objects.lattices.finite_lattices_2d.lattice_square import LatticeSquare
from cshape_objects.lattices.finite_lattices_2d.lattice_x_hexagonal import LatticeXHexagonal
from cshape_objects.lattices.lattice import Lattice

lattices = {
    Lattice.LatticeSquare: LatticeSquare,
    Lattice.LatticeXHexagonal: LatticeXHexagonal
}


def create_lattice(lattice):
    return lattices[lattice]()
