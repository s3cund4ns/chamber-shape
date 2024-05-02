from PySide6.Qt3DExtras import Qt3DExtras

from renderer.entities.cylinder_entity import CylinderEntity
from renderer.entities.x_plane_entity import XPlaneEntity
from renderer.entities.y_plane_entity import YPlaneEntity
from renderer.entities.z_plane_entity import ZPlaneEntity
from renderer.entities.sphere_entity import SphereEntity
from cshape_objects.surfaces.surface import SurfacesTypes

meshes = {
    SurfacesTypes.XPlane: XPlaneEntity,
    SurfacesTypes.YPlane: YPlaneEntity,
    SurfacesTypes.ZPlane: ZPlaneEntity,
    SurfacesTypes.Cylinder: CylinderEntity,
    SurfacesTypes.Sphere: SphereEntity,
    SurfacesTypes.Cone: Qt3DExtras.QConeMesh,
    SurfacesTypes.XHexagonalPrism: Qt3DExtras.QCylinderMesh,
    SurfacesTypes.YHexagonalPrism: Qt3DExtras.QCylinderMesh
}


def create_mesh(mesh_type, entity):
    return meshes[mesh_type](entity)
