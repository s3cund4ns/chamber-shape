from abc import abstractmethod

from PySide6.Qt3DCore import Qt3DCore
from PySide6.Qt3DExtras import Qt3DExtras
from PySide6.Qt3DRender import Qt3DRender
from PySide6.QtGui import QRgba64, QTransform, QVector3D


class SurfaceEntity(Qt3DCore.QEntity):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mesh = None
        self.material = Qt3DExtras.QDiffuseSpecularMaterial(self)
        self.material.setAmbient(QRgba64.fromRgba(139, 0, 255, 255))

        self.transform = Qt3DCore.QTransform(self)
        self.transform.setRotationX(90.0)
        self.transform.setTranslation(QVector3D(0.0, 0.0, 0.0))

    @abstractmethod
    def set_data(self, properties):
        pass
