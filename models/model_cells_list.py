from cshape_objects.cell import Cell
from cshape_objects.cshape_types import CShapeTypes
from project_data.model import Model


class ModelCellsList(Model):
    def __init__(self):
        super(ModelCellsList, self).__init__()
        self.data: list[Cell] = []
        self.selected_item_index = -1

        self.materials_model = None
        self.universes_model = None
        self.surfaces_model = None
        self.input_data_model = None

    def add_item(self, index, type):
        item: Cell = Cell()
        item.all_materials = self.materials_model.data
        item.all_universes = self.universes_model.data
        item.all_elements = self.surfaces_model.data
        self.data.insert(index, item)
        item_text = f'{item.get_name()}'
        self.view_model.add_item_to_views(index, item_text, item)
        self.input_data_model.update_cells_data(self.dump_data(), self.surfaces_model.data)

    def select_item(self, index):
        self.selected_item_index = index
        selected_item: Cell = self.data[self.selected_item_index]
        selected_item.all_universes = self.universes_model.data
        self.view_model.select_item_in_views(index, selected_item.get_data())

    def delete_item(self):
        self.data.pop(self.selected_item_index)
        self.view_model.delete_item_in_views(self.selected_item_index)
        self.input_data_model.update_cells_data(self.dump_data(), self.surfaces_model.data)

    def change_data(self, value):
        self.data[self.selected_item_index].set_data(value)
        self.view_model.change_item_in_views(self.data[self.selected_item_index].get_name())
        self.input_data_model.update_cells_data(self.dump_data(), self.surfaces_model.data)

    def clear_data(self):
        self.data.clear()
        self.view_model.clear_views()

    def dump_data(self):
        data = []
        for cell in self.data:
            data.append(cell.dump_data())
        return data

    def load_data(self, cells_data: list):
        for cell in cells_data:
            cell_index = cells_data.index(cell)
            self.add_item(cell_index, None)
            self.select_item(cell_index)
            cell_tuple = tuple(cell.items())
            for cell_property in cell_tuple:
                if cell_property[0] == 'Surfaces':
                    if cell_property[1] == []:
                        continue
                    for surface in cell_property[1]:
                        self.change_data(('Add', [surface[0], surface[1]]))
                    continue
                self.change_data(cell_property)

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item
