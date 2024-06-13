from cshape_objects.material import Material
from preprocessor.input_data_generator import InputDataGenerator
from preprocessor.input_data_generator_creator import create_input_data_generator
from project_data.model import Model


class ModelInputData(Model):
    def __init__(self):
        super().__init__()
        self.generator: InputDataGenerator | None = None
        self.data = [[], [], [], [], [], [], [], []]

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

    def update_cells_data(self, cells_data: list, all_surfaces_data: list):
        translated_cells_data = self.generator.generate_cells_data(cells_data, all_surfaces_data)
        self.data[3] = translated_cells_data
        self.view_model.add_item_to_views(self.data)

    def update_pins_data(self, pins_data: list, all_pins_data: list):
        translated_pins_data = self.generator.generate_pins_data(pins_data, all_pins_data)
        self.data[4] = translated_pins_data
        self.view_model.add_item_to_views(self.data)

    def update_lattices_data(self, lattices_data: list):
        translated_lattices_data = self.generator.generate_lattices_data(lattices_data)
        self.data[5] = translated_lattices_data
        self.view_model.add_item_to_views(self.data)

    def update_calculation_parameters_data(self, calculation_parameters_data: list):
        translated_calculation_parameters_data = self.generator.generate_calculation_parameters_data(calculation_parameters_data)
        self.data[6] = translated_calculation_parameters_data
        self.view_model.add_item_to_views(self.data)

    def update_detectors_data(self, detectors_data: list, all_elements_data: list):
        translated_detectors_data = self.generator.generate_detectors_data(detectors_data, all_elements_data)
        self.data[7] = translated_detectors_data
        self.view_model.add_item_to_views(self.data)

    def write_to_file(self):
        with open('Projects/project.inp', 'w') as file:
            for cshape_object_data in self.data:
                file.writelines(cshape_object_data)

    def clear_data(self):
        for element_data in self.data:
            element_data.clear()

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item
