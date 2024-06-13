from cshape_objects.cell import Cell
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.pin import Pin
from cshape_objects.universe import Universe
from solvers.solver_dict import serpent_dict
from project_data.model import Model


class ModelUniversesList(Model):
    def __init__(self):
        super(ModelUniversesList, self).__init__()
        self.data: list[Universe] = []
        self.selected_item_index = -1

    def add_item(self, index, type):
        item: Universe = Universe(len(self.data))
        self.data.insert(index, item)
        item_text = f'{item.get_type()} {item.get_index()}'
        self.view_model.add_item_to_views(index, item_text, item)

    def select_item(self, index):
        self.selected_item_index = index
        selected_item: Universe = self.data[self.selected_item_index]
        self.view_model.select_item_in_views(index, selected_item.get_data())

    def delete_item(self):
        self.data.pop(self.selected_item_index)
        self.view_model.delete_item_in_views(self.selected_item_index)
        for item in self.data:
            index = self.data.index(item)
            item.set_index(index)
            self.view_model.change_item_in_views(item.get_type(), item.get_index())

    def change_data(self, value):
        self.data[self.selected_item_index].set_data(value)
        self.view_model.change_item_in_views([self.data[self.selected_item_index].get_type(),
                                              self.data[self.selected_item_index].get_index()])

    def clear_data(self):
        self.data.clear()
        self.view_model.clear_views()

    def dump_data(self):
        data = []
        for universe in self.data:
            universe_index = universe.get_index()
            data.append(universe_index)
        return data

    def load_data(self, universes_data: list):
        for universe in universes_data:
            universe_index = universes_data.index(universe)
            self.add_item(universe_index, None)

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item
