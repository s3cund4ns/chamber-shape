import enum
import struct

from PySide6.Qt3DCore import Qt3DCore
from PySide6.Qt3DExtras import Qt3DExtras
from PySide6.Qt3DRender import Qt3DRender
from PySide6.QtCore import QBuffer, QByteArray
from PySide6.QtGui import QVector3D, QRgba64


class LineDirection(enum.Enum):
    vertical = 0
    horizontal = 1


class LineEntity(Qt3DCore.QEntity):
    def __init__(self, line_direction: int, parent=None):
        super().__init__(parent)
        self.line_direction = line_direction
        self.mesh: Qt3DRender.QGeometryRenderer = Qt3DRender.QGeometryRenderer(self)
        self.mesh.setPrimitiveType(Qt3DRender.QGeometryRenderer.PrimitiveType.Lines)
        self.vertices: list[QVector3D] = []
        self.vertex_buffer: QBuffer = QBuffer()
        self.vertex_data: QByteArray = QByteArray()
        self.material = Qt3DExtras.QPhongMaterial(self)
        self.material.setAmbient(QRgba64.fromRgba(255, 255, 255, 255))
        self.transform: Qt3DCore.QTransform = Qt3DCore.QTransform(self)
        self.transform.setRotationX(90.0)
        self.transform.setTranslation(QVector3D(0.0, 0.0, 0.0))

    def add_vertices(self, vertical_lines_count: int, horizontal_lines_count: int, pitch: float):
        if self.line_direction == LineDirection.vertical.value:
            for line_index in range(vertical_lines_count):
                self.vertices.append(QVector3D(0.0, vertical_lines_count * pitch, 0.0))
                self.vertices.append(QVector3D(horizontal_lines_count * pitch, vertical_lines_count * pitch, 0.0))
        elif self.line_direction == LineDirection.horizontal.value:
            for line_index in range(horizontal_lines_count):
                self.vertices.append(QVector3D(0.0, horizontal_lines_count * pitch, 0.0))
                self.vertices.append(QVector3D(vertical_lines_count * pitch, horizontal_lines_count * pitch, 0.0))

    def set_geometry(self):
        for vertex in self.vertices:
            self.vertex_data.append(struct.pack('3f', vertex.x(), vertex.y(), vertex.z()))
            self.vertex_buffer.setData(self.vertex_data)
            self.mesh.setGeometry(self.vertex_buffer)

    def add_components(self):
        self.addComponent(self.mesh)
        self.addComponent(self.material)
        self.addComponent(self.transform)
