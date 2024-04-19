from dataclasses import dataclass
from abc import ABC, abstractmethod
from cshape_objects.cshape_object import CShapeObject, CShapeObjectTypes, CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from typing import Sequence


@dataclass
class CShapeObjects:
    Detector = 'Detector'


@dataclass
class DetectorsTypes:
    NoneType = None
    Material = 'Material'
    Lattice = 'Lattice'
    Mesh = 'Mesh'

    Default = Mesh

    def get(self) -> Sequence[str]:
        return [self.Material, self.Lattice, self.Mesh]

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

    def get_type(self):
        return self.detector_type

    def get_name(self):
        return self.name

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_data(self, properties):
        pass

