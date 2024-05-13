from PySide6.Qt3DExtras import Qt3DExtras
from PySide6.Qt3DRender import Qt3DRender
from PySide6.QtGui import QVector3D, QRgba64

from renderer.entities.surface_entity import SurfaceEntity
from cshape_objects.surfaces.rectangular_prism import Properties


class RectangularPrismEntity(SurfaceEntity):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mesh: Qt3DExtras.QCylinderMesh = Qt3DExtras.QCylinderMesh(self)
        self.mesh.setSlices(4)
        self.mesh.setRadius(5.0)
        self.mesh.setLength(50.0)

        self.addComponent(self.mesh)
        self.addComponent(self.material)
        self.addComponent(self.transform)

    def set_data(self, properties: dict):
        name, value = properties
        match name:
            case Properties.Position:
                x, y = value
                self.transform.setTranslation(QVector3D(x, y, 0.0))
            case Properties.HalfWidth:
                self.mesh.setRadius(value)
            case Properties.Length:
                self.mesh.setLength(value)
            case Properties.Color:
                red, green, blue = value
                self.material.setAmbient(QRgba64.fromRgba(red, green, blue, 255))

