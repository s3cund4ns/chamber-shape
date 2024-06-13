from project_data.view_model import ViewModel


class ViewModelInputData(ViewModel):
    def __init__(self):
        super().__init__()

    def add_item_to_views(self, input_data: list):
        for view in self.views:
            view.add_item(input_data)

    def clear_views(self):
        for view in self.views:
            view.clear()