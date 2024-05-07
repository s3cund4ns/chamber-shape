from PySide6.Qt3DExtras import Qt3DExtras
from PySide6.Qt3DRender import Qt3DRender
from PySide6.QtGui import QVector3D

from renderer.entities.surface_entity import SurfaceEntity
from cshape_objects.surfaces.x_torus import Properties


class XTorusEntity(SurfaceEntity):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mesh: Qt3DExtras.QTorusMesh = Qt3DExtras.QTorusMesh(self)
        self.mesh.setMinorRadius(5.0)
        self.mesh.setRadius(5.0)

        self.transform.setRotationZ(-90.0)

        self.addComponent(self.mesh)
        self.addComponent(self.material)
        self.addComponent(self.transform)

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case Properties.Position:
                x, y, z = value
                self.transform.setTranslation(QVector3D(x, y, z))
            case Properties.MinorRadius:
                self.mesh.setMinorRadius(value)
            case Properties.MajorRadius:
                self.mesh.setRadius(value)
