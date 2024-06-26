from dataclasses import dataclass

import numpy as np

from cshape_objects.cshape_object import CShapeObject, CShapeObjectTypes, CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes


@dataclass
class UniverseElementsTypes:
    NoneType = None
    Cell = 'Cell'
    Lattice = 'Lattice'


@dataclass
class Properties(CShapeObjectProperties):
    Position = 'Position'
    Elements = 'Elements'

    def get(self):
        return [self.Position, self.Elements]


class Universe(CShapeObject):
    def __init__(self, index: int):
        super().__init__()
        self.type = CShapeObjectTypes.Universe
        self.properties = Properties()
        self.index: int = index
        self.position = np.array([0.0, 0.0, 0.0], dtype=np.float32)
        self.elements: list = []

    def get_type(self):
        return self.type

    def set_index(self, index: int):
        self.index = index

    def get_index(self):
        return self.index

    def add_element(self, element) -> None:
        current_element = element
        self.elements.append(current_element)

    def delete_element(self, element_id):
        self.elements.pop(element_id)

    def get_names(self):
        position_names = ['x', 'y', 'z']
        return position_names

    def get_values(self):
        return self.position, self.elements

    def get_data(self):
        elements = []
        for element in self.elements:
            elements.append([element.get_type(), element.get_name()])
        return {self.properties.Position: (CShapeTypes.Vector3DFloat, [list(np.array(self.position, dtype=float)), (-99999.9999, 99999.9999)]),
                self.properties.Elements: (CShapeTypes.List, elements)}

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case self.properties.Position:
                self.position[0:3] = value
