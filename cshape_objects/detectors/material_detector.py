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
        self.all_materials: list[Material] = []
        self.material = None

    def get_data(self):
        materials_info: list = []
        for material in self.all_materials:
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
                self.material = self.all_materials[material]

    def dump_data(self) -> dict:
        material_index: int | None = None
        if self.material is not None:
            material_index = self.all_materials.index(self.material)

        return {
            'Type': self.detector_type,
            self.properties.Name: self.name,
            self.properties.Material: material_index
        }
