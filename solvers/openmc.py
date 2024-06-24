import xml.etree.ElementTree as ET

from solvers.solver import Solver


class OpenMC(Solver):
    def __init__(self, path: str, calculation_data_path: str):
        super().__init__()
        self.path = path
        self.calculation_data_path = calculation_data_path

    def load_tokens(self):
        pass

    def __create_object_data_file(self, object_name: str):
        root = ET.Element(object_name)
        tree = ET.ElementTree(root)
        tree.write(f'{self.calculation_data_path}/{object_name}', encoding='utf-8', xml_declaration=True)

    def create_input_data_file(self, file_name: str):
        self.__create_object_data_file('materials')
        self.__create_object_data_file('geometry')
        self.__create_object_data_file('settings')

    def save_input_data_file(self, file_name: str, input_data: list):
        pass

    def start_calculation(self, file_name: str):
        pass
