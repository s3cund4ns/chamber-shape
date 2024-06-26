from dataclasses import dataclass

from project_data.view_model import ViewModel


@dataclass
class Operations:
    Add = 'Add'
    Select = 'Select'
    Delete = 'Delete'


class ViewModelCellsList(ViewModel):
    def __init__(self):
        super().__init__()

    def add_item_to_models(self, *args):
        index, = args
        for model in self.models:
            model.add_item(index, None)

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
        value, = args
        for view in self.views:
            view.change_item(value)
        self.project_data.set_not_saved_state()

    def delete_item_in_models(self):
        for model in self.models:
            model.delete_item()

    def delete_item_in_views(self, index):
        for view in self.views:
            view.delete_item(index)
        self.project_data.set_not_saved_state()

    def insert_fill_property(self, fill_property):
        for view in self.views:
            view.insert_property(fill_property)

    def clear_views(self):
        for view in self.views:
            view.clear()
