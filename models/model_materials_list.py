from project_data.model import Model
from cshape_objects.material import Material


class ModelMaterialsList(Model):
    def __init__(self):
        super(ModelMaterialsList, self).__init__()
        self.data: list = []
        self.selected_item_index = -1

        self.input_data_model = None

    def add_item(self, index, type):
        item: Material = Material()
        self.data.insert(index, item)
        item_text = f'{item.get_name()}: {item.get_density()}'
        self.view_model.add_item_to_views(index, item_text, item)
        self.input_data_model.update_materials_data(self.dump_data())

    def select_item(self, index):
        self.selected_item_index = index
        selected_item: Material = self.data[self.selected_item_index]
        self.view_model.select_item_in_views(index, selected_item.get_data())

    def delete_item(self):
        self.data.pop(self.selected_item_index)
        self.view_model.delete_item_in_views(self.selected_item_index)
        self.input_data_model.update_materials_data(self.dump_data())

    def change_data(self, value):
        self.data[self.selected_item_index].set_data(value)
        self.view_model.change_item_in_views([self.data[self.selected_item_index].get_name(),
                                              self.data[self.selected_item_index].get_density()])
        self.input_data_model.update_materials_data(self.dump_data())

    def clear_data(self):
        self.data.clear()
        self.view_model.clear_views()

    def dump_data(self):
        data = []
        for material in self.data:
            data.append(material.dump_data())
        return data

    def load_data(self, materials_data: list):
        for material in materials_data:
            material_index = materials_data.index(material)
            self.add_item(material_index, None)
            self.select_item(material_index)
            material_tuple = tuple(material.items())
            for material_property in material_tuple:
                if material_property[0] == 'Nuclides':
                    if material_property[1] == []:
                        continue
                    for nuclide in material_property[1]:
                        self.change_data(('Add', [material_property[1].index(nuclide), nuclide[0], nuclide[1]]))
                    continue
                self.change_data(material_property)

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item
