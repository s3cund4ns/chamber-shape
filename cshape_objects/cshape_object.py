from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class CShapeObjectTypes:
    Material = 'Material'
    Surface = 'Surface'
    Universe = 'Universe'
    Cell = 'Cell'
    Pin = 'Pin'
    Lattice = 'Lattice'
    Detector = 'Detector'
    CalculationParameter = 'CalculationParameter'
    CalculationOutput = 'CalculationOutput'
    PlotInfo = 'PlotInfo'


@dataclass
class CShapeObjectProperties(ABC):
    pass


class CShapeObject(ABC):
    def __init__(self):
        super().__init__()
        self.type: str
        self.properties: CShapeObjectProperties

    def get_type(self):
        pass

    def get_name(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_data(self, properties):
        pass
