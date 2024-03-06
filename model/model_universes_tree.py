from data_structs.tree import Tree
from model.model import Model
from preprocessor.cell import Cell
from preprocessor.universe import Universe


class ModelUniversesTree(Model):
    def __init__(self):
        super(ModelUniversesTree, self).__init__()
        self.data: Tree = Tree()
        self.key_of_selected_item: str = ''
        self.selected_item_index = -1
        self.elements_amount = 0

    def add_item(self, item_type):
        universe_element, element_type = item_type
        match universe_element:
            case 'Universe':
                self.add_universe()
            case 'Cell':
                self.add_cell()
            case 'Pin':
                pass

    def add_universe(self):
        item: Universe = Universe(self.elements_amount)
        self.present_item = item
        self.data.insert_node('root', str(item), item)
        item_text = ('Universe', str(self.elements_amount))
        self.elements_amount += 1
        self.view_model.add_item_to_views('root', item_text, str(item))

    def add_cell(self):
        # index = self.selected_item_index
        # selected_item = self.data[index]
        # level = selected_item[0] + 1
        item: Cell = Cell()
        self.data.insert_node(self.key_of_selected_item, str(item), item)
        item_text = (item.get_type(), item.get_name())
        self.view_model.add_item_to_views(self.key_of_selected_item, item_text, str(item))

    def select_item(self, key):
        self.key_of_selected_item = str(self.data.get_node(key)[0])
        print(self.key_of_selected_item)

    def delete_item(self):
        self.data.delete_node(self.key_of_selected_item)
        self.view_model.delete_item_in_views(self.key_of_selected_item)
        self.key_of_selected_item = ''
        print(self.data.get())

    def change_data(self, value):
        self.data[self.selected_item_index].set_data(value)
        self.view_model.change_item_in_views([self.data[self.selected_item_index].get_name(),
                                              self.data[self.selected_item_index].get_density()])
