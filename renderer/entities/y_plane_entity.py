from PySide6.Qt3DExtras import Qt3DExtras
from PySide6.QtGui import QVector3D, QRgba64

from renderer.entities.surface_entity import SurfaceEntity
from cshape_objects.surfaces.y_plane import Properties


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
            case Properties.Distance:
                self.transform.setTranslation(QVector3D(0.0, value, 0.0))
            case Properties.Size:
                width, height = value
                self.mesh.setWidth(width)
                self.mesh.setHeight(height)
            case Properties.Color:
                red, green, blue = value
                self.material.setAmbient(QRgba64.fromRgba(red, green, blue, 255))


