from PySide6.Qt3DExtras import Qt3DExtras
from PySide6.Qt3DRender import Qt3DRender
from PySide6.QtGui import QVector3D

from renderer.entities.surface_entity import SurfaceEntity
from cshape_objects.surfaces.y_cylinder import Properties


class YCylinderEntity(SurfaceEntity):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mesh: Qt3DExtras.QCylinderMesh = Qt3DExtras.QCylinderMesh(self)
        self.mesh.setRadius(5.0)
        self.mesh.setLength(50.0)

        self.transform.setRotationZ(-90.0)
        self.transform.setRotationX(-1.0)
        self.transform.setRotationZ(-1.0)
        self.transform.setRotationZ(0.0)
        self.transform.setRotationX(0.0)

        self.addComponent(self.mesh)
        self.addComponent(self.material)
        self.addComponent(self.transform)

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case Properties.Position:
                x, z = value
                self.transform.setTranslation(QVector3D(x, 0.0, z))
            case Properties.Radius:
                self.mesh.setRadius(value)
            case Properties.Length:
                self.mesh.setLength(value)
