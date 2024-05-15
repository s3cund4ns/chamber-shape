from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.lattices.lattice import Lattice
from cshape_objects.lattices.lattice_creator import create_lattice
from solvers.solver_dict import serpent_dict
from project_data.model import Model


class ModelLatticesList(Model):
    def __init__(self):
        super(ModelLatticesList, self).__init__()
        self.data: list[Lattice] = []
        self.selected_item_index = -1

        self.universes_model = None
        self.pins_model = None
        self.input_data_model = None

    def add_item(self, index: int, lattice_type):
        item: Lattice = create_lattice(lattice_type)
        item.all_pins = self.pins_model.data
        item.all_universes = self.universes_model.data
        self.data.insert(index, item)
        item_text = f'{item.get_type()} {item.get_name()}'
        self.view_model.add_item_to_views(index, item_text, item)
        self.input_data_model.update_lattices_data(self.dump_data())

    def select_item(self, index):
        self.selected_item_index = index
        selected_item: Lattice = self.data[self.selected_item_index]
        selected_item.all_pins = self.pins_model.data
        selected_item.all_universes = self.universes_model.data
        self.view_model.select_item_in_views(index, selected_item.get_data())

    def delete_item(self):
        self.data.pop(self.selected_item_index)
        self.view_model.delete_item_in_views(self.selected_item_index)
        self.input_data_model.update_lattices_data(self.dump_data())

    def change_data(self, value):
        self.data[self.selected_item_index].set_data(value)
        self.view_model.change_item_in_views(self.selected_item_index, value,
                                             [self.data[self.selected_item_index].get_type(),
                                              self.data[self.selected_item_index].get_name()])
        self.input_data_model.update_lattices_data(self.dump_data())

    def clear_data(self):
        self.data.clear()
        self.view_model.clear_views()

    def dump_data(self):
        data = []
        for lattice in self.data:
            data.append(lattice.dump_data())
        return data

    def load_data(self, lattices_data: list):
        for lattice in lattices_data:
            lattice_index = lattices_data.index(lattice)
            lattice_type = lattice['Type']
            self.add_item(lattice_index, lattice_type)
            self.select_item(lattice_index)
            lattice_tuple = tuple(lattice.items())
            for lattice_property in lattice_tuple[1:]:
                if lattice_property[0] == 'Universe Matrix':
                    for row in range(len(lattice_property[1])):
                        for column in range(len(lattice_property[1][row])):
                            self.change_data(('Universe Matrix', [(row, column), lattice_property[1][row][column]]))
                    continue
                self.change_data(lattice_property)

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item
