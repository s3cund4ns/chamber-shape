from dataclasses import dataclass

from cshape_objects.cshape_object import CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.detectors.detector import DetectorsTypes, Detector
from cshape_objects.material import Material


@dataclass
class Properties(CShapeObjectProperties):
    Object = 'Object'
    Name = 'Name'
    Material = 'Material'


class MaterialDetector(Detector):
    def __init__(self):
        super().__init__()
        self.detector_type = DetectorsTypes.MaterialDetector
        self.properties = Properties()
        self.materials_list = []
        self.material = None

    def get_data(self):
        materials_info: list = []
        for material in self.materials_list:
            material = f'{material.get_name()} {material.get_density()}'
            materials_info.append(material)
        if self.material is None:
            current_material_info = ''
        else:
            current_material_info = f'{self.material.get_name()} {self.material.get_density()}'

        return {
            self.properties.Name: (CShapeTypes.String, self.name),
            self.properties.Material: (CShapeTypes.Reference, [current_material_info, materials_info])
        }

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case self.properties.Name:
                name = value
                self.name = name
            case self.properties.Material:
                material = value
                self.material = self.materials_list[material]
