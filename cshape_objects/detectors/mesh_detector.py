from dataclasses import dataclass

from cshape_objects.cshape_object import CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes
from cshape_objects.detectors.detector import DetectorsTypes, Detector

import numpy as np


@dataclass
class Properties(CShapeObjectProperties):
    Object = 'Object'
    Name = 'Name'
    Mode = 'Mode'
    Coordinate1 = 'Coordinate1'
    Coordinate2 = 'Coordinate2'
    Coordinate3 = 'Coordinate3'


@dataclass
class Mode:
    Cylindrical = 'Cylindrical'
    Spherical = 'Spherical'


class MeshDetector(Detector):
    def __init__(self):
        super().__init__()
        self.detector_type = DetectorsTypes.MeshDetector
        self.properties = Properties()
        self.modes: dict = {'Cylindrical': 'Cylindrical', 'Spherical': 'Spherical'}
        self.mode = self.modes['Cylindrical']
        self.coordinate1 = np.array([0.0, 0.0, 1.0], dtype=np.float32)
        self.coordinate2 = np.array([0.0, 0.0, 1.0], dtype=np.float32)
        self.coordinate3 = np.array([0.0, 0.0, 1.0], dtype=np.float32)

    def get_data(self):
        return {
            self.properties.Name: (CShapeTypes.String, self.name),
            self.properties.Mode: (CShapeTypes.Enum, [self.modes, self.mode]),
            self.properties.Coordinate1: (CShapeTypes.Vector3DFloat, [list(self.coordinate1), (-99999.9999, 99999.9999)]),
            self.properties.Coordinate2: (CShapeTypes.Vector3DFloat, [list(self.coordinate2), (-99999.9999, 99999.9999)]),
            self.properties.Coordinate3: (CShapeTypes.Vector3DFloat, [list(self.coordinate3), (-99999.9999, 99999.9999)])
        }

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case self.properties.Name:
                name = value
                self.name = name
            case self.properties.Mode:
                mode = value
                self.mode = self.modes[mode]
            case self.properties.Coordinate1:
                coordinate1 = value
                self.coordinate1[0:3] = coordinate1
            case self.properties.Coordinate2:
                coordinate2 = value
                self.coordinate2[0:3] = coordinate2
            case self.properties.Coordinate3:
                coordinate3 = value
                self.coordinate3[0:3] = coordinate3
