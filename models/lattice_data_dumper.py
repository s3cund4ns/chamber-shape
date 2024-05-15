from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.lattices.square_lattice import LatticeSquare


class LatticeDataDumper:
    def __init__(self):
        self.item_data: dict = {}

    def dump(self, item: LatticeSquare):
        source_item_data: dict = item.get_data()
        self.item_data = {'Type': item.get_type()}
        for key in source_item_data.keys():
            if source_item_data[key][0] == CShapeTypes.Float:
                self.item_data[key] = source_item_data[key][1][0]
                continue
            if source_item_data[key][0] == CShapeTypes.Vector2DFloat:
                self.item_data[key] = source_item_data[key][1][0]
                continue
            if source_item_data[key][0] == CShapeTypes.Vector3DFloat:
                self.item_data[key] = source_item_data[key][1][0]
                continue
            if key == 'Size':
                size = []
                for size_component in source_item_data[key][1]:
                    size.append(int(size_component))
                self.item_data[key] = size
                continue
            if key == 'Universe Matrix':
                universes = []
                universe_matrix = source_item_data[key][1][0]
                for row in range(universe_matrix.shape[0]):
                    row_in_matrix = []
                    for column in range(universe_matrix.shape[1]):
                        row_in_matrix.append(int(universe_matrix[row, column]))
                    universes.append(row_in_matrix)
                self.item_data[key] = universes
                continue
            self.item_data[key] = source_item_data[key][1]

        return self.item_data
