from dataclasses import dataclass

from project_data.view_model import ViewModel


@dataclass
class Operations:
    Add = 'Add'
    Select = 'Select'
    Change = 'Change'
    Delete = 'Delete'


class ViewModelSurfacesList(ViewModel):
    def __init__(self):
        super().__init__()

    def add_item_to_models(self, *args):
        index, item_type = args
        for model in self.models:
            model.add_item(index, item_type)

    def add_item_to_views(self, *args):
        index, item_text, item = args
        for view in self.views:
            view.add_item(index, item_text, item)
        self.project_data.set_not_saved_state()

    def select_item_in_models(self, *args):
        index, = args
        for model in self.models:
            model.select_item(index)

    def select_item_in_views(self, *args):
        index, item = args
        for view in self.views:
            view.select_item(index, item)

    def change_item_in_models(self, *args):
        value, = args
        for model in self.models:
            model.change_data(value)

    def change_item_in_views(self, *args):
        index, value, item_text = args
        print(index, value)
        for view in self.views:
            view.change_item(index, value, item_text)
        self.project_data.set_not_saved_state()

    def delete_item_in_models(self):
        for model in self.models:
            model.delete_item()

    def delete_item_in_views(self, index):
        for view in self.views:
            view.delete_item(index)
        self.project_data.set_not_saved_state()

    def clear_views(self):
        for view in self.views:
            view.clear()

