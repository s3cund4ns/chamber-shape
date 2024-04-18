from cshape_objects.material import Material
from project_data.model import Model


class ModelInputData(Model):
    def __init__(self):
        super().__init__()
        self.data = [[], [], []]

    def add_item(self, *args):
        cshape_object_data, index = args
        self.data[index].clear()
        self.data[index] = cshape_object_data
        self.view_model.add_item_to_views(self.data)

    def update_cell_data(self, cells_data: list, surfaces_data: list):
        if len(self.cells_data) > 0:
            self.cells_data = []
        for cell_data in cells_data:
            key_word = self.serpent_dict.get(cell_data.get_type())
            cell_name = cell_data.get_name()
            cell_fill = ''
            if type(cell_data.get_fill()) is str:
                cell_fill = cell_data.get_fill()
            elif type(cell_data.get_fill()) is Material:
                cell_fill = cell_data.get_fill().get_name()
            elif type(cell_data.get_fill()) is int:
                cell_fill = str(cell_data.fill.get_fill())
            surfaces_text = ''
            for surface in cell_data.get_surfaces():
                if surface[0] in surfaces_data:
                    surface_id = surfaces_data.index(surface[0]) + 1
                    surface_id = surface_id * surface[1]
                    surfaces_text += f'{surface_id} '

            text = f'{key_word} {cell_name} {cell_fill} {surfaces_text}\n'
            self.cells_data.append(text)

    def update_pin_data(self, pins_data: list):
        if len(self.pins_data) > 0:
            self.pins_data = []
        for pin_data in pins_data:
            key_word = self.serpent_dict.get(pin_data.get_type())
            pin_universe = str(pin_data.get_universe())
            regions_text = ''
            for region in pin_data.get_regions():
                region_name = region[0].get_name()
                region_radius = str(region[1])
                regions_text += f'{region_name} {region_radius}\n'

            text = f'{key_word} {pin_universe}\n{regions_text}'
            self.pins_data.append(text)

    def write_to_file(self):
        with open('Projects/project.inp', 'w') as file:
            for cshape_object_data in self.data:
                file.writelines(cshape_object_data)

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item
