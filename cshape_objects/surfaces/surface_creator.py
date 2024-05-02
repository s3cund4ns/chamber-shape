from cshape_objects.surfaces.cone import Cone
from cshape_objects.surfaces.cylinder import Cylinder
from cshape_objects.surfaces.x_plane import XPlane
from cshape_objects.surfaces.y_plane import YPlane
from cshape_objects.surfaces.z_plane import ZPlane
from cshape_objects.surfaces.sphere import Sphere
from cshape_objects.surfaces.surface import SurfacesTypes
from cshape_objects.surfaces.x_hexagonal_prism import XHexagonalPrism
from cshape_objects.surfaces.y_hexagonal_prism import YHexagonalPrism

surfaces_types = {
    SurfacesTypes.XPlane: XPlane,
    SurfacesTypes.YPlane: YPlane,
    SurfacesTypes.ZPlane: ZPlane,
    SurfacesTypes.Cone: Cone,
    SurfacesTypes.Sphere: Sphere,
    SurfacesTypes.Cylinder: Cylinder,
    SurfacesTypes.XHexagonalPrism: XHexagonalPrism,
    SurfacesTypes.YHexagonalPrism: YHexagonalPrism
}


def create_surface(surface_type):
    return surfaces_types[surface_type]()
