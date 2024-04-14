from cshape_objects.detectors.lattice import Lattice
from cshape_objects.detectors.material import Material
from cshape_objects.detectors.mesh import Mesh

from cshape_objects.detectors.detector import DetectorsTypes


detectors_types = {
    DetectorsTypes.Material: Material,
    DetectorsTypes.Lattice: Lattice,
    DetectorsTypes.Mesh: Mesh
}


def create_detector(detector_type):
    return detectors_types[detector_type]()
