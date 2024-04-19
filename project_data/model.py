import random
from abc import abstractmethod


class Model:
    def __init__(self):
        self.view_model = None

    def set_view_model(self, view_model):
        self.view_model = view_model

    @abstractmethod
    def add_item(self, *args):
        pass

    @abstractmethod
    def select_item(self, *args):
        pass

    @abstractmethod
    def delete_item(self):
        pass

    @abstractmethod
    def change_data(self, value):
        pass

