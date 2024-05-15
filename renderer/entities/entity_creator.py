from renderer.entities.cone_entity import ConeEntity
from renderer.entities.dodecagonal_prism_entity import DodecagonalPrismEntity
from renderer.entities.octagonal_prism_entity import OctagonalPrismEntity
from renderer.entities.rectangular_prism_entity import RectangularPrismEntity
from renderer.entities.triangular_prism_entity import TriangularPrismEntity
from renderer.entities.x_cylinder_entity import XCylinderEntity
from renderer.entities.x_torus_entity import XTorusEntity
from renderer.entities.y_cylinder_entity import YCylinderEntity
from renderer.entities.y_hexagon_prism_entity import YHexagonPrismEntity
from renderer.entities.x_plane_entity import XPlaneEntity
from renderer.entities.y_plane_entity import YPlaneEntity
from renderer.entities.y_torus_entity import YTorusEntity
from renderer.entities.z_cylinder_entity import ZCylinderEntity
from renderer.entities.z_plane_entity import ZPlaneEntity
from renderer.entities.sphere_entity import SphereEntity
from cshape_objects.surfaces.surface import SurfacesTypes
from renderer.entities.z_torus_entity import ZTorusEntity

entities = {
    SurfacesTypes.XPlane: XPlaneEntity,
    SurfacesTypes.YPlane: YPlaneEntity,
    SurfacesTypes.ZPlane: ZPlaneEntity,
    SurfacesTypes.XCylinder: XCylinderEntity,
    SurfacesTypes.YCylinder: YCylinderEntity,
    SurfacesTypes.ZCylinder: ZCylinderEntity,
    SurfacesTypes.Sphere: SphereEntity,
    SurfacesTypes.Cone: ConeEntity,
    SurfacesTypes.XTorus: XTorusEntity,
    SurfacesTypes.YTorus: YTorusEntity,
    SurfacesTypes.ZTorus: ZTorusEntity,
    SurfacesTypes.TriangularPrism: TriangularPrismEntity,
    SurfacesTypes.RectangularPrism: RectangularPrismEntity,
    SurfacesTypes.YHexagonalPrism: YHexagonPrismEntity,
    SurfacesTypes.OctagonalPrism: OctagonalPrismEntity,
    SurfacesTypes.DodecagonalPrism: DodecagonalPrismEntity
}


def create_entity(mesh_type, entity):
    return entities[mesh_type](entity)
