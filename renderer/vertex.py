from dataclasses import dataclass

from PySide6.QtGui import QVector3D


@dataclass
class Vertex:
    position: QVector3D
    normal: QVector3D
