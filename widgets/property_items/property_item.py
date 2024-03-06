from abc import abstractmethod
from dataclasses import dataclass

from PySide6.QtWidgets import QWidget


@dataclass
class PropertyItemTypes:
    Int = "<class 'int'>"
    Float = "<class 'float'>"
    String = "<class 'str'>"
    Vector2DInt = "<class 'list'> 2 int"
    Vector2DFloat = "<class 'list'> 2 float"
    Vector2DString = "<class 'list'> 2 str"
    Vector3DInt = "<class 'list'> 3 int"
    Vector3DFloat = "<class 'list'> 3 <class 'numpy.float32'>"
    Vector3DString = "<class 'list'> 3 str"
    ComboBox = "<class 'list'> 2 <class 'dict'>"
    ListBox = "<class 'list'> <class 'list'>"


class PropertyItem(QWidget):
    def __init__(self):
        super().__init__()
        self.properties_view = None

    def set_properties_view(self, properties_view):
        self.properties_view = properties_view

    @abstractmethod
    def set_data(self, data: list):
        pass
