from abc import abstractmethod

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidget, QMenu


class View:
    def __init__(self):
        self.view_model = None

    def set_view_model(self, view_model):
        self.view_model = view_model

    # def notify_view_model(self, operation, parameter):
    #     self.view_models.notify_model(operation, parameter)

    @abstractmethod
    def add_item(self, *args):
        pass

    @abstractmethod
    def select_item(self, *args):
        pass

    @abstractmethod
    def change_item(self, *args):
        pass

    @abstractmethod
    def delete_item(self, index):
        pass
