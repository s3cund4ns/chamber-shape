from dataclasses import dataclass

from project_data.model import ViewModel


@dataclass
class Operations:
    Add = 'Add'
    Select = 'Select'
    Change = 'Change'
    Delete = 'Delete'


class ViewModelViewport(ViewModel):
    def __init__(self):
        super().__init__()

    def notify_model(self, operation: Operations, parameters: list):
        pass

    def notify_views(self, item_index, item, operation):
        for view in self.views:
            match operation:
                case Operations.Add:
                    view.add_item(item_index, item)
                case Operations.Select:
                    view.select_item(item_index)
                case Operations.Change:
                    view.change_item(item_index, item)
                case Operations.Delete:
                    view.delete_item(item_index)