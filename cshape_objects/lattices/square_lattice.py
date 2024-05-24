import numpy as np

from cshape_objects.cshape_object import CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.lattices.lattice import Lattice, LatticeTypes


class Properties(CShapeObjectProperties):
    Name = 'Name'
    Universe = 'Belongs to universe'
    Position = 'Position'
    Size = 'Size'
    Pitch = 'Pitch'
    UniverseMatrix = 'Universe Matrix'


class SquareLattice(Lattice):
    def __init__(self):
        super().__init__()
        self.lattice_type = LatticeTypes.SquareLattice
        self.properties = Properties()
        self.name = 'NewLattice'
        self.center_position = np.array([0.0, 0.0], dtype=np.float32)
        self.size: list[int] = [5, 5]
        self.pitch: float = 5.0
        self.universes_matrix: list[list[int | float]] = [[-1, -1, -1, -1, -1],
                                                          [-1, -1, -1, -1, -1],
                                                          [-1, -1, -1, -1, -1],
                                                          [-1, -1, -1, -1, -1],
                                                          [-1, -1, -1, -1, -1]]

    def get_universe_position(self, x_number: int, y_number: int):
        x_position = self.position[0] + x_number * self.pitch
        y_position = self.position[1] - y_number * self.pitch
        return np.array([x_position, y_position, self.position[2]], dtype=np.float32)

    def get_size(self):
        return self.size

    def get_pitch(self):
        return self.pitch

    def resize(self, rows: int, columns: int) -> None:
        new_matrix = [[0 for column in range(columns)] for row in range(rows)]

        for i in range(min(len(self.universes_matrix), rows)):
            for j in range(min(len(self.universes_matrix[0]), columns)):
                new_matrix[i][j] = self.universes_matrix[i][j]

        self.universes_matrix = new_matrix

    def set_universe(self, row: int, column: int, value: int | float) -> None:
        self.universes_matrix[row][column] = value

    def get_data(self):
        all_universes = []
        for universe in self.all_universes:
            all_universes.append(str(universe.get_index()))

        all_pins: list = []
        for pin in self.all_pins:
            all_pins.append(f'{pin.get_name()} {pin.get_universe_index()}')

        return {self.properties.Name: (CShapeTypes.String, self.name),
                self.properties.Universe: (CShapeTypes.Reference, [str(self.get_universe_index()), all_universes]),
                self.properties.Position: (CShapeTypes.Vector2DFloat, [list(np.array(self.center_position, dtype=float)), (-99999.9999, 99999.9999)]),
                self.properties.Size: (CShapeTypes.Vector2DInt, self.size),
                self.properties.Pitch: (CShapeTypes.Float, [self.pitch, (0.0001, 99999.9999)]),
                self.properties.UniverseMatrix: (CShapeTypes.Array2DInt, [self.universes_matrix, all_pins])}

    def set_data(self, properties: tuple):
        name, value = properties
        match name:
            case self.properties.Name:
                self.name = value
            case self.properties.Universe:
                index = value
                self.universe = self.all_universes[index]
            case self.properties.Position:
                self.center_position[0:2] = value
                self.position[0] = self.center_position[0]
                self.position[1] = self.center_position[1]
            case self.properties.Size:
                self.size[0:2] = value
                self.resize(self.size[0], self.size[1])
            case self.properties.Pitch:
                self.pitch = value
            case self.properties.UniverseMatrix:
                universe_index, universe_value = value
                row, column = universe_index
                self.set_universe(row, column, int(universe_value))

    def dump_data(self) -> dict:
        return {
            'Type': self.lattice_type,
            self.properties.Name: self.name,
            self.properties.Universe: self.get_universe_index(),
            self.properties.Position: list(np.array(self.center_position, dtype=float)),
            self.properties.Size: self.size,
            self.properties.Pitch: self.pitch,
            self.properties.UniverseMatrix: self.universes_matrix
        }
