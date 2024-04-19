from abc import abstractmethod
from dataclasses import dataclass

from project_data.model import Model
from project_data.view import View


@dataclass
class Operations:
    pass


class ViewModel:
    def __init__(self):
        self.models: list[Model] = []
        self.views: list[View] = []

    def add_model(self, model: Model):
        self.models.append(model)
        model.set_view_model(self)

    def add_view(self, view: View):
        self.views.append(view)
        view.set_view_model(self)

    @abstractmethod
    def add_item_to_models(self, *args):
        pass

    @abstractmethod
    def add_item_to_views(self, *args):
        pass

    @abstractmethod
    def select_item_in_models(self, *args):
        pass

    @abstractmethod
    def select_item_in_views(self, *args):
        pass

    @abstractmethod
    def change_item_in_models(self, *args):
        pass

    @abstractmethod
    def change_item_in_views(self, *args):
        pass

    @abstractmethod
    def delete_item_in_models(self):
        pass

    @abstractmethod
    def delete_item_in_views(self, index):
        pass

    @abstractmethod
    def clear_views(self):
        pass

    @abstractmethod
    def notify_model(self, operation, parameter):
        pass

    @abstractmethod
    def notify_views(self, item_index, item, current_object, operation: Operations):
        pass

