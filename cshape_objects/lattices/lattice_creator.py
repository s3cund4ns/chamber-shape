from cshape_objects.lattices.finite_lattices_2d.lattice_square import LatticeSquare
from cshape_objects.lattices.finite_lattices_2d.lattice_x_hexagonal import LatticeXHexagonal
from cshape_objects.lattices.lattice import Lattices

lattices = {
    Lattices.LatticeSquare: LatticeSquare,
    Lattices.LatticeXHexagonal: LatticeXHexagonal
}


def create_lattice(lattice):
    return lattices[lattice]()
