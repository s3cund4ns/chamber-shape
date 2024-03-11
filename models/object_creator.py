from cshape_objects.surfaces.cone import Cone
from cshape_objects.surfaces.cylinder import Cylinder
from cshape_objects.surfaces.plane import Plane
from cshape_objects.surfaces.sphere import Sphere
from cshape_objects.surfaces.surface import SurfacesTypes
from cshape_objects.surfaces.x_hexagonal_prism import XHexagonalPrism
from cshape_objects.surfaces.y_hexagonal_prism import YHexagonalPrism

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
