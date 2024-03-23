import random
from abc import abstractmethod


class Model:
    def __init__(self):
        self.view_model = None

    def set_view_model(self, view_model):
        self.view_model = view_model

    # def notify_view_models(self, item_index, item, current_object, operation):
    #     self.view_model.notify_views(item_index, item, operation)

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

    @abstractmethod
    def clear_data(self):
        pass

    @abstractmethod
    def dump_data(self):
        pass

    @abstractmethod
    def load_data(self, data):
        pass

