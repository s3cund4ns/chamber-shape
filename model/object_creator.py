from dataclasses import fields

from surfaces.cone import Cone
from surfaces.cylinder import Cylinder
from surfaces.plane import Plane
from surfaces.sphere import Sphere
from surfaces.surface import SurfacesTypes
from surfaces.x_hexagonal_prism import XHexagonalPrism
from surfaces.y_hexagonal_prism import YHexagonalPrism

surfaces_types = {
    SurfacesTypes.Plane: Plane,
    SurfacesTypes.Cone: Cone,
    SurfacesTypes.Sphere: Sphere,
    SurfacesTypes.Cylinder: Cylinder,
    SurfacesTypes.XHexagonalPrism: XHexagonalPrism,
    SurfacesTypes.YHexagonalPrism: YHexagonalPrism
}


def create_object(surface_type):
    return surfaces_types[surface_type]()
