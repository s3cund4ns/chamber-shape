from cshape_objects.material import Material
from preprocessor.input_data_generator import InputDataGenerator
from preprocessor.input_data_generator_creator import create_input_data_generator
from project_data.model import Model


class ModelInputData(Model):
    def __init__(self):
        super().__init__()
        self.generator = None
        self.data = [[], [], [], [], [], []]

    def create_input_data_generator(self, generator):
        self.generator: InputDataGenerator = create_input_data_generator(generator)

    def add_item(self, *args):
        cshape_object_data, index = args
        self.data[index].clear()
        self.data[index] = cshape_object_data
        self.view_model.add_item_to_views(self.data)

    def update_basic_data(self, basic_data):
        translated_basic_data = self.generator.generate_basic_data(basic_data)
        self.data[0] = translated_basic_data
        self.view_model.add_item_to_views(self.data)

    def update_materials_data(self, material_data):
        translated_material_data = self.generator.generate_materials_data(material_data)
        self.data[1] = translated_material_data
        self.view_model.add_item_to_views(self.data)

    def update_surfaces_data(self, surfaces_data):
        translated_surfaces_data = self.generator.generate_surfaces_data(surfaces_data)
        self.data[2] = translated_surfaces_data
        self.view_model.add_item_to_views(self.data)

    def update_cells_data(self, data: list):
        cells_data = []
        for item in data:
            if item['Type'] == 'Cell':
                cells_data.append(item)
        translated_cells_data = self.generator.generate_cells_data(cells_data)
        self.data[3] = translated_cells_data
        self.view_model.add_item_to_views(self.data)

    def update_pins_data(self, data: list):
        pins_data = []
        for item in data:
            if item['Type'] == 'Pin':
                pins_data.append(item)
        translated_pins_data = self.generator.generate_pins_data(pins_data)
        self.data[4] = translated_pins_data
        self.view_model.add_item_to_views(self.data)

    def update_lattices_data(self, data: list):
        lattices_data = []
        for item in data:
            if item['Type'] == 'Lattice':
                lattices_data.append(item)
        translated_lattices_data = self.generator.generate_lattices_data(lattices_data)
        self.data[5] = translated_lattices_data
        self.view_model.add_item_to_views(self.data)

    def write_to_file(self):
        with open('Projects/project.inp', 'w') as file:
            for cshape_object_data in self.data:
                file.writelines(cshape_object_data)

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item
