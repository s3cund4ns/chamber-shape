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
        self.elements_amount = 0

        self.materials_model = None
        self.surfaces_model = None

    def add_item(self, item_type):
        universe_element, element_type = item_type
        match universe_element:
            case 'Universe':
                self.add_universe()
            case 'Cell':
                self.add_cell()
            case 'Pin':
                self.add_pin()

    def add_universe(self):
        item: Universe = Universe(self.elements_amount)
        self.present_item = item
        self.data.insert_node('root', str(item), item)
        item_text = ('Universe', str(self.elements_amount))
        self.elements_amount += 1
        self.view_model.add_item_to_views('root', item_text, str(item))

    def find_universes(self):
        universes = []
        for item_key in self.data.get():
            item_value = self.data.get_node_value(item_key)
            if type(item_value) is Universe:
                universes.append(item_value)

        return universes


    def add_cell(self):
        if type(self.data.get_node_value(self.key_of_selected_item)) != Universe:
            return

        item: Cell = Cell()
        self.data.insert_node(self.key_of_selected_item, str(item), item)
        self.data.get_node_value(self.key_of_selected_item).add_element(item)
        item_text = (item.get_type(), item.get_name())
        self.view_model.add_item_to_views(self.key_of_selected_item, item_text, str(item))

    def add_pin(self):
        if type(self.data.get_node_value(self.key_of_selected_item)) != Universe:
            return
        item: Pin = Pin()

    def select_item(self, key):
        self.key_of_selected_item = key
        selected_item = self.data.get_node_value(self.key_of_selected_item)
        match type(selected_item):
            case Cell:
                selected_item.all_elements = self.surfaces_model.data
                selected_item.all_materials = self.materials_model.data
                selected_item.all_universes = self.find_universes()
                print(self.find_universes())
        self.view_model.select_item_in_views(self.data.get_node(key)[0])

    def delete_item(self):
        self.data.delete_node(self.key_of_selected_item)
        self.view_model.delete_item_in_views(self.key_of_selected_item)
        self.key_of_selected_item = ''
        print(self.data.get())

    def change_data(self, value):
        item = self.data.get_node_value(self.key_of_selected_item)
        item.set_data(value)
        name, item_value = value
        if name == 'Name':
            self.view_model.change_item_in_views(item_value)

    def clear_data(self):
        self.data.clear()
        self.elements_amount = 0
        self.view_model.clear_views()

    def dump_data(self):
        universes_data = []
        print(self.data.get_values_from_nodes())
        cells_data = []
        pins_data = []

        for item in self.data.get_values_from_nodes():
            source_item_data = item.get_data()
            item_data = {'Type': item.get_type()}
            for key in source_item_data.keys():
                item_data[key] = source_item_data[key][1]

            universes_data.append(item_data)

        return universes_data

    def load_data(self):
        pass
