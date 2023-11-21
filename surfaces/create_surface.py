from surfaces.surface import SurfacesTypes, Surface
from surfaces.plane import Plane
from surfaces.cylinder import Cylinder
from surfaces.sphere import Sphere
from surfaces.cone import Cone


def create_surface(surface_type: SurfacesTypes):
    match surface_type:
        case SurfacesTypes.Plane:
            return Plane(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        case SurfacesTypes.Cylinder:
            return Cylinder(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        case SurfacesTypes.Sphere:
            return Sphere(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        case SurfacesTypes.Cone:
            return Cone(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

