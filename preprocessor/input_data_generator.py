from abc import ABC, abstractmethod


class InputDataGenerator(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def generate_basic_data(self, basic_data):
        pass

    @abstractmethod
    def generate_materials_data(self, materials: list):
        pass

    @abstractmethod
    def generate_surfaces_data(self, surfaces: list):
        pass

    @abstractmethod
    def generate_cells_data(self, cells: list, all_surfaces: list):
        pass

    @abstractmethod
    def generate_pins_data(self, pins: list, all_materials: list):
        pass

    @abstractmethod
    def generate_lattices_data(self, lattices):
        pass

    @abstractmethod
    def generate_calculation_parameters_data(self, calculation_parameters: list):
        pass

    @abstractmethod
    def generate_detectors_data(self, detectors: list, energy_grid, all_elements: list):
        pass

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item