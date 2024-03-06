from random import randint

from surfaces.surface import SurfacesTypes, Surface
from surfaces.plane import Plane
from surfaces.cylinder import Cylinder
from surfaces.sphere import Sphere
from surfaces.cone import Cone
from surfaces.x_hexagonal_prism import XHexagonalPrism
from surfaces.y_hexagonal_prism import YHexagonalPrism


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

