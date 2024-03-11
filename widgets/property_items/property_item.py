from abc import abstractmethod
from dataclasses import dataclass

from PySide6.QtWidgets import QWidget


class PropertyItem(QWidget):
    def __init__(self):
        super().__init__()
        self.properties_view = None

    def set_properties_view(self, properties_view):
        self.properties_view = properties_view

    @abstractmethod
    def set_data(self, data: list):
        pass

    @abstractmethod
    def set_default_values(self, *args):
        pass
