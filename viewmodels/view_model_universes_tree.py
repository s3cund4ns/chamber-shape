from dataclasses import dataclass

from project_data.view_model import ViewModel


@dataclass
class Operations:
    Add = 'Add'
    Select = 'Select'
    Delete = 'Delete'


class ViewModelUniversesTree(ViewModel):
    def __init__(self):
        self.data: dict = {}
        self.current_key: str = ''
        super().__init__()

    def set_node_value(self, value: any):
        self.data[self.current_key] = value

    def add_item_to_models(self, *args):
        item_type = args
        for model in self.models:
            model.add_item(item_type)

    def add_item_to_views(self, *args):
        index, item_text, key, item = args
        self.current_key = key
        for view in self.views:
            view.add_item(index, item_text, item)

    def select_item_in_models(self, *args):
        item, = args
        for key, value in self.data.items():
            if value == item:
                self.current_key = key
        for model in self.models:
            model.select_item(self.current_key)

    def select_item_in_views(self, *args):
        item = args
        for view in self.views:
            view.select_item(0, item)

    def change_item_in_models(self, *args):
        value, = args
        for model in self.models:
            model.change_data(value)

    def change_item_in_views(self, *args):
        value, = args
        for view in self.views:
            view.change_item(value)

    def delete_item_in_models(self):
        for model in self.models:
            model.delete_item()

    def delete_item_in_views(self, key):
        self.data.delete_node(key)
        for view in self.views:
            view.delete_item(key)

    def clear_views(self):
        for view in self.views:
            view.clear()

    # def notify_model(self, operation: Operations, parameters: list):
    #     match operation:
    #         case Operations.Add:
    #             self.model.add_item()
    #         case Operations.Select:
    #             item_index = parameters[0]
    #             self.model.select_item(item_index)
    #         case Operations.Delete:
    #             self.model.delete_item(parameters[0])
    #
    # def notify_views(self, item_index, item, current_object, operation: Operations):
    #     for view in self.views:
    #         match operation:
    #             case Operations.Add:
    #                 view.add_item(str(item_index))
    #             case Operations.Select:
    #                 view.select_item(item_index)
    #             case Operations.Delete:
    #                 view.delete_item(item_index)

