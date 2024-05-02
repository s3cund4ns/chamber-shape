from cshape_objects.surfaces.cone import Cone
from cshape_objects.surfaces.dodecagonal_prism import DodecagonalPrism
from cshape_objects.surfaces.octagonal_prism import OctagonalPrism
from cshape_objects.surfaces.rectangular_prism import RectangularPrism
from cshape_objects.surfaces.triangular_prism import TriangularPrism
from cshape_objects.surfaces.x_cylinder import XCylinder
from cshape_objects.surfaces.x_plane import XPlane
from cshape_objects.surfaces.x_torus import XTorus
from cshape_objects.surfaces.y_cylinder import YCylinder
from cshape_objects.surfaces.y_plane import YPlane
from cshape_objects.surfaces.y_torus import YTorus
from cshape_objects.surfaces.z_cylinder import ZCylinder
from cshape_objects.surfaces.z_plane import ZPlane
from cshape_objects.surfaces.sphere import Sphere
from cshape_objects.surfaces.surface import SurfacesTypes
from cshape_objects.surfaces.x_hexagonal_prism import XHexagonalPrism
from cshape_objects.surfaces.y_hexagonal_prism import YHexagonalPrism
from cshape_objects.surfaces.z_torus import ZTorus

surfaces_types = {
    SurfacesTypes.XPlane: XPlane,
    SurfacesTypes.YPlane: YPlane,
    SurfacesTypes.ZPlane: ZPlane,
    SurfacesTypes.XCylinder: XCylinder,
    SurfacesTypes.YCylinder: YCylinder,
    SurfacesTypes.ZCylinder: ZCylinder,
    SurfacesTypes.Cone: Cone,
    SurfacesTypes.Sphere: Sphere,
    SurfacesTypes.XTorus: XTorus,
    SurfacesTypes.YTorus: YTorus,
    SurfacesTypes.ZTorus: ZTorus,
    SurfacesTypes.TriangularPrism: TriangularPrism,
    SurfacesTypes.RectangularPrism: RectangularPrism,
    SurfacesTypes.YHexagonalPrism: YHexagonalPrism,
    SurfacesTypes.OctagonalPrism: OctagonalPrism,
    SurfacesTypes.DodecagonalPrism: DodecagonalPrism
}


def create_surface(surface_type):
    return surfaces_types[surface_type]()
