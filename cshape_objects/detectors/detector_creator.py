from cshape_objects.detectors.lattice_detector import LatticeDetector
from cshape_objects.detectors.material_detector import MaterialDetector
from cshape_objects.detectors.mesh_detector import MeshDetector

from cshape_objects.detectors.detector import DetectorsTypes


detectors_types = {
    DetectorsTypes.MaterialDetector: MaterialDetector,
    DetectorsTypes.LatticeDetector: LatticeDetector,
    DetectorsTypes.MeshDetector: MeshDetector
}


def create_detector(detector_type):
    return detectors_types[detector_type]()
