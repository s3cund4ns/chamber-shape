from random import randint

from cshape_objects.surfaces.surface import SurfacesTypes
from cshape_objects.surfaces.z_plane import Plane
from cshape_objects.surfaces.x_cylinder import Cylinder
from cshape_objects.surfaces.sphere import Sphere
from cshape_objects.surfaces.cone import Cone
from cshape_objects.surfaces.x_hexagonal_prism import XHexagonalPrism
from cshape_objects.surfaces.y_hexagonal_prism import YHexagonalPrism


def create_surface(surface_type):
    match surface_type:
        case SurfacesTypes.Plane:
            return Plane([0.0, 0.0, 0.0], [randint(100, 255), randint(100, 255), randint(100, 255), 255])
        case SurfacesTypes.Cylinder:
            return Cylinder([0.0, 0.0, 0.0], [randint(100, 255), randint(100, 255), randint(100, 255), 255], 5.0)
        case SurfacesTypes.Sphere:
            return Sphere([0.0, 0.0, 0.0], [randint(100, 255), randint(100, 255), randint(100, 255), 255], 5.0)
        case SurfacesTypes.Cone:
            return Cone([0.0, 0.0, 0.0], [randint(100, 255), randint(100, 255), randint(100, 255), 255], 5.0, 50.0)
        case SurfacesTypes.XHexagonalPrism:
            return XHexagonalPrism([0.0, 0.0, 0.0], [randint(100, 255), randint(100, 255), randint(100, 255), 255], 5.0)
        case SurfacesTypes.YHexagonalPrism:
            return YHexagonalPrism([0.0, 0.0, 0.0], [randint(100, 255), randint(100, 255), randint(100, 255), 255], 5.0)

