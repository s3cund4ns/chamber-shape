from cshape_objects.cell import Cell
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.pin import Pin
from cshape_objects.universe import Universe
from solvers.solver_dict import serpent_dict
from project_data.model import Model


class ModelPinsList(Model):
    def __init__(self):
        super(ModelPinsList, self).__init__()
        self.data: list[Pin] = []
        self.selected_item_index = -1

        self.materials_model = None
        self.universes_model = None
        self.input_data_model = None

    def add_item(self, index, type):
        item: Pin = Pin()
        item.all_materials = self.materials_model.data
        item.all_universes = self.universes_model.data
        self.data.insert(index, item)
        item_text = f'{item.get_name()}'
        self.view_model.add_item_to_views(index, item_text, item)
        self.input_data_model.update_pins_data(self.dump_data(), self.materials_model.data)

    def select_item(self, index):
        self.selected_item_index = index
        selected_item: Pin = self.data[self.selected_item_index]
        selected_item.all_materials = self.materials_model.data
        selected_item.all_universes = self.universes_model.data
        self.view_model.select_item_in_views(index, selected_item.get_data())

    def delete_item(self):
        self.data.pop(self.selected_item_index)
        self.view_model.delete_item_in_views(self.selected_item_index)
        self.input_data_model.update_pins_data(self.dump_data(), self.materials_model.data)

    def change_data(self, value):
        self.data[self.selected_item_index].set_data(value)
        self.view_model.change_item_in_views(self.data[self.selected_item_index].get_name())
        self.input_data_model.update_pins_data(self.dump_data(), self.materials_model.data)

    def clear_data(self):
        self.data.clear()
        self.view_model.clear_views()

    def dump_data(self):
        data = []
        for pin in self.data:
            data.append(pin.dump_data())
        return data

    def load_data(self, pins_data: list):
        for pin in pins_data:
            pin_index = pins_data.index(pin)
            self.add_item(pin_index, None)
            self.select_item(pin_index)
            pin_tuple = tuple(pin.items())
            for pin_property in pin_tuple:
                if pin_property[0] == 'Regions':
                    if pin_property[1] == []:
                        continue
                    for region in pin_property[1]:
                        self.change_data(('Add', region[0]))
                        self.change_data(('Set', [pin_property[1].index(region), region[1]]))
                    continue
                self.change_data(pin_property)

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item
