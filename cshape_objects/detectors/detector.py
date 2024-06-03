from dataclasses import dataclass
from abc import abstractmethod

from cshape_objects.calculation_parameters.energy_grid import EnergyGrid
from cshape_objects.cshape_object import CShapeObject, CShapeObjectTypes
from typing import Sequence


@dataclass
class CShapeObjects:
    Detector = 'Detector'


@dataclass
class DetectorsTypes:
    NoneType = None
    MaterialDetector = 'MaterialDetector'
    LatticeDetector = 'LatticeDetector'
    MeshDetector = 'MeshDetector'

    Default = MeshDetector

    def get(self) -> Sequence[str]:
        return [self.MaterialDetector, self.LatticeDetector, self.MeshDetector]

    def get_field_name_by_value(self, value):
        for attr_name, attr_value in self.__dict__.items():
            if attr_value == value:
                return attr_name
        return None


class Detector(CShapeObject):
    def __init__(self):
        super().__init__()
        self.type = CShapeObjectTypes.Detector
        self.detector_type: DetectorsTypes = DetectorsTypes.NoneType
        self.name: str = 'NewDetector'
        self.energy_mid_grid: tuple | None = None
        self.sp_flux: tuple | None = None
        self.sp_errors: tuple | None = None
        self.energy_grid: EnergyGrid | None = None

    def get_type(self):
        return self.detector_type

    def get_name(self):
        return self.name

    @abstractmethod
    def get_data(self):
        pass

    def is_output_data_empty(self) -> bool:
        return self.energy_mid_grid is None and self.sp_flux is None and self.sp_errors is None

    def get_output_data(self) -> tuple:
        return self.energy_mid_grid, self.sp_flux, self.sp_errors

    @abstractmethod
    def set_data(self, properties):
        pass

    def set_output_data(self, data: tuple) -> None:
        self.energy_mid_grid, self.sp_flux, self.sp_errors = data

    def dump_data(self) -> dict:
        pass
