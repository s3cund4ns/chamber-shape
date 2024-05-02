from PySide6.Qt3DExtras import Qt3DExtras
from PySide6.QtGui import QVector3D

from renderer.entities.surface_entity import SurfaceEntity
from cshape_objects.surfaces.z_plane import Properties


class YPlaneEntity(SurfaceEntity):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mesh: Qt3DExtras.QPlaneMesh = Qt3DExtras.QPlaneMesh(self)
        self.mesh.setWidth(100.0)
        self.mesh.setHeight(100.0)

        self.transform.setRotationZ(-90.0)
        self.transform.setRotationX(-1.0)
        self.transform.setRotationZ(-1.0)
        self.transform.setRotationZ(0.0)
        self.transform.setRotationX(0.0)
        self.transform.setRotationZ(0.0)

        self.addComponent(self.mesh)
        self.addComponent(self.material)
        self.addComponent(self.transform)

    def set_data(self, properties):
        name, value = properties
        match name:
            case Properties.Position:
                x, y, z = value
                self.transform.setTranslation(QVector3D(x, y, z))
            case Properties.RotationX:
                self.transform.setRotationX(value)
            case Properties.RotationY:
                self.transform.setRotationY(value)
            case Properties.RotationZ:
                self.transform.setRotationZ(value)


