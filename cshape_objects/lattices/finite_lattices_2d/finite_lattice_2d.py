import numpy as np

from cshape_objects.cshape_object import CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.lattices.lattice import Lattice, LatticeTypes


class Properties(CShapeObjectProperties):
    Name = 'Name'
    Position = 'Position'
    Size = 'Size'
    Pitch = 'Pitch'
    UniverseMatrix = 'Universe Matrix'


class FiniteLattice2D(Lattice):
    def __init__(self):
        super().__init__()
        self.lattice_type = LatticeTypes.FiniteLattice2D
        self.properties = Properties()
        self.size = np.array([5, 5], dtype=np.uint32)
        self.pitch: float = 5.0
        self.universes_matrix = np.array([[-1, -1]], dtype=np.int16)
        self.universes_matrix.resize(self.size[0], self.size[1])
        self.universes_matrix[:] = -1

    def get_data(self):
        all_universes: list = []
        for universe in self.all_universes:
            all_universes.append(str(self.all_universes.index(universe)))

        return {self.properties.Name: (CShapeTypes.String, self.name),
                self.properties.Position: (CShapeTypes.Vector3DFloat, list(np.array(self.position, dtype=float))),
                self.properties.Size: (CShapeTypes.Vector2DInt, list(np.array(self.size, dtype=int))),
                self.properties.Pitch: (CShapeTypes.Float, self.pitch),
                self.properties.UniverseMatrix: (CShapeTypes.Array2DInt, [self.universes_matrix, all_universes])}

    def set_data(self, properties: tuple):
        name, value = properties
        match name:
            case self.properties.Name:
                self.name = value
            case self.properties.Position:
                self.position[0:3] = value
            case self.properties.Size:
                self.size[0:2] = value
            case self.properties.Pitch:
                self.pitch = value
            case self.properties.UniverseMatrix:
                universe_index_str, universe_value = value
                universe_index = universe_index_str.split('_')
                self.universes_matrix[int(universe_index[0]), int(universe_index[1])] = universe_value
