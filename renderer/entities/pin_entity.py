from PySide6.Qt3DCore import Qt3DCore
from PySide6.Qt3DExtras import Qt3DExtras
from PySide6.Qt3DRender import Qt3DRender
from PySide6.QtGui import QRgba64, QTransform, QVector3D


class PinEntity(Qt3DCore.QEntity):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.meshes: list[Qt3DRender.QMesh] = []
        self.material = Qt3DExtras.QDiffuseSpecularMaterial(self)
        self.material.setAmbient(QRgba64.fromRgba(139, 0, 255, 255))

        self.transform = Qt3DCore.QTransform(self)
        self.transform.setRotationX(90.0)
        self.transform.setTranslation(QVector3D(0.0, 0.0, 0.0))

    def add_mesh(self, color: QRgba64, radius: float):
        mesh: Qt3DExtras.QCylinderMesh = Qt3DExtras.QCylinderMesh(self)
        mesh.setRadius()

    def set_data(self, properties):
        pass
