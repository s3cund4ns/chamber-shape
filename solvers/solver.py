import json
from abc import ABC, abstractmethod
from dataclasses import dataclass

from nuclear_data.nuclear_data import NuclearData


@dataclass
class Solvers:
    Serpent = 'Serpent'
    OpenMC = 'OpenMC'


class Solver(ABC):
    def __init__(self):
        self.tokens: dict[str, str] = {}
        self.nuclear_data: NuclearData = NuclearData()
        self.path: str = ''
        self.calculation_data_path: str = ''

    @abstractmethod
    def load_tokens(self):
        pass

    def load_nuclear_data(self, file_path: str):
        with open(file_path, 'r') as file:
            nuclear_data: dict = json.load(file)
            self.nuclear_data = NuclearData(**nuclear_data)

    @abstractmethod
    def create_input_data_file(self, file_name: str):
        pass

    @abstractmethod
    def save_input_data_file(self, file_name: str, input_data: list):
        pass

    @abstractmethod
    def start_calculation(self, file_name: str):
        pass
