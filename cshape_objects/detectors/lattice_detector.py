from dataclasses import dataclass

from cshape_objects.cshape_object import CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.detectors.detector import DetectorsTypes, Detector
from cshape_objects.lattices.lattice import Lattice


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
        self.all_lattices: list[Lattice] = []
        self.lattice = None

    def get_data(self):
        lattices_info: list = []
        print(self.all_lattices)
        for lattice in self.all_lattices:
            lattice = f'{lattice.get_name()}'
            lattices_info.append(lattice)
        if self.lattice is None:
            current_lattice_info = ''
        else:
            current_lattice_info = f'{self.lattice.get_name()}'

        return {
            self.properties.Name: (CShapeTypes.String, self.name),
            self.properties.Lattice: (CShapeTypes.Reference, [current_lattice_info, lattices_info])
        }

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case self.properties.Name:
                name = value
                self.name = name
            case Properties.Lattice:
                lattice = value
                self.lattice = self.all_lattices[lattice]


