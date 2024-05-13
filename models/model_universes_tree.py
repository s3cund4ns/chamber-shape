from cshape_objects.lattices.lattice import Lattice
from data_structs.tree import Tree
from project_data.model import Model
from cshape_objects.cell import Cell
from cshape_objects.pin import Pin
from cshape_objects.universe import Universe


class ModelUniversesTree(Model):
    def __init__(self):
        super(ModelUniversesTree, self).__init__()
        self.data: Tree = Tree()
        self.key_of_selected_item: str = ''
        self.selected_item_index = -1
        self.amount = 0

    def add_item(self):
        item: Universe = Universe(self.amount)
        self.data.insert_node('root', str(item), item)
        item_text = ('Universe', str(self.amount))
        self.amount += 1
        self.view_model.add_item_to_views('root', item_text, str(item))

    def get_universes_list(self):
        universes: list = []
        for item_key in self.data.get():
            item_value = self.data.get_node_value(item_key)
            if type(item_value) is Universe:
                universes.append(item_value)

        return universes

    def insert_universe_element_to_data(self, item: Cell | Pin | Lattice):
        self.data.insert_node(self.key_of_selected_item, str(item), item)
        self.data.get_node_value(self.key_of_selected_item).add_element(item)
        item_text = (item.get_type(), item.get_name())
        self.view_model.add_item_to_views(self.key_of_selected_item, item_text, str(item))

    def select_item(self, key):
        self.key_of_selected_item = key
        selected_item = self.data.get_node_value(self.key_of_selected_item)
        self.view_model.select_item_in_views(self.data.get_node(key)[0])

    def delete_item(self):
        self.data.delete_node(self.key_of_selected_item)
        self.view_model.delete_item_in_views(self.key_of_selected_item)
        self.key_of_selected_item = ''

    def change_data(self, value):
        item = self.data.get_node_value(self.key_of_selected_item)
        item.set_data(value)
        name, item_value = value
        if name == 'Name':
            self.view_model.change_item_in_views(item_value)

    def clear_data(self):
        self.data.clear()
        self.amount = 0
        self.view_model.clear_views()

    def dump_data(self):
        universes_data = []

        for item in self.data.get_values_from_nodes():
            if type(item) is Universe:
                universes_data.append(self.universe_data_dumper.dump(item))
            if type(item) is Cell:
                universes_data.append(self.cell_data_dumper.dump(item))
            if type(item) is Pin:
                universes_data.append(self.pin_data_dumper.dump(item))
            if type(item) is LatticeSquare:
                universes_data.append(self.lattice_data_dumper.dump(item))

        return universes_data

    def load_data(self):
        pass

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item
