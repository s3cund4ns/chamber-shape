from PySide6.Qt3DExtras import Qt3DExtras

from renderer.entities.cylinder_entity import CylinderEntity
from renderer.entities.plane_entity import PlaneEntity
from renderer.entities.sphere_entity import SphereEntity
from cshape_objects.surfaces.surface import SurfacesTypes

meshes = {
    SurfacesTypes.Plane: PlaneEntity,
    SurfacesTypes.Cylinder: CylinderEntity,
    SurfacesTypes.Sphere: SphereEntity,
    SurfacesTypes.Cone: Qt3DExtras.QConeMesh,
    SurfacesTypes.XHexagonalPrism: Qt3DExtras.QCylinderMesh,
    SurfacesTypes.YHexagonalPrism: Qt3DExtras.QCylinderMesh
}


def create_mesh(mesh_type, entity):
    return meshes[mesh_type](entity)
