from dataclasses import dataclass

from cshape_objects.cshape_object import CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.detectors.detector import DetectorsTypes, Detector


@dataclass
class Properties(CShapeObjectProperties):
    Object = 'Object'
    Name = 'Name'
    Lattice = 'Lattice'


class LatticeDetector(Detector):
    def __init__(self):
        super().__init__()
        self.detector_type = DetectorsTypes.LatticeDetector
        self.properties = Properties()
        self.lattice: str = 'name of lattice'

    def set_lattice(self, lattice: str):
        self.lattice = lattice

    def get_lattice(self) -> str:
        return self.lattice

    def get_data(self):
        return {
            self.properties.Name: (CShapeTypes.String, self.name),
            Properties.Lattice: (CShapeTypes.String, self.lattice)
        }

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case self.properties.Name:
                name = value
                self.name = name
            case Properties.Lattice:
                self.lattice = value


