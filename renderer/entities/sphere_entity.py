from PySide6.Qt3DExtras import Qt3DExtras
from PySide6.QtGui import QVector3D

from renderer.entities.surface_entity import SurfaceEntity
from surfaces.sphere import Properties


class SphereEntity(SurfaceEntity):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mesh: Qt3DExtras.QSphereMesh = Qt3DExtras.QSphereMesh(self)
        self.mesh.setRadius(5.0)

        self.addComponent(self.mesh)
        self.addComponent(self.material)
        self.addComponent(self.transform)

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case Properties.Position:
                x, y, z = value
                self.transform.setTranslation(QVector3D(x, y, z))
            case Properties.Radius:
                self.mesh.setRadius(value)
