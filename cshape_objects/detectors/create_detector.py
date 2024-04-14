from cshape_objects.detectors.lattice import Lattice
from cshape_objects.detectors.material import Material
from cshape_objects.detectors.mesh import Mesh
from cshape_objects.detectors.detector import DetectorsTypes
from random import randint

def create_detector(detector_type):
    match detector_type:
        case DetectorsTypes.Mesh:
            return Mesh([0.0, 0.0, 0.0], [randint(100, 255), randint(100, 255), randint(100, 255), 255])
        case DetectorsTypes.Lattice:
            return Lattice([0.0, 0.0, 0.0], [randint(100, 255), randint(100, 255), randint(100, 255), 255], 5.0)
        case DetectorsTypes.Material:
            return Material([0.0, 0.0, 0.0], [randint(100, 255), randint(100, 255), randint(100, 255), 255], 5.0)
