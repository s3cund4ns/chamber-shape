from dataclasses import dataclass

from cshape_objects.cshape_object import CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.detectors.detector import DetectorsTypes, Detector


@dataclass
class Properties(CShapeObjectProperties):
    Object = 'Object'
    Name = 'Name'
    Material = 'Material'


class Material(Detector):
    def __init__(self):
        super().__init__()
        self.detector_type = DetectorsTypes.Material
        self.properties = Properties()
        self.material: str = 'name of material'

    def set_material(self, material: str):
        self.material = material

    def get_material(self) -> str:
        return self.material

    def get_data(self):
        return {
            self.properties.Name: (CShapeTypes.String, self.name),
            Properties.Material: (CShapeTypes.String, self.material)
        }

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case self.properties.Name:
                name = value
                self.name = name
            case Properties.Material:
                self.material = value



