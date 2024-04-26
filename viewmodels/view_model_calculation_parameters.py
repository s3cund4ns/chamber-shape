from project_data.view_model import ViewModel


class ViewModelCalculationParameters(ViewModel):
    def __init__(self):
        super().__init__()

    def add_item_to_models(self, *args):
        pass

    def add_item_to_views(self, *args):
        pass

    def select_item_in_models(self, parameter_type: str):
        for model in self.models:
            if model.find_parameter(parameter_type) is None:
                print(parameter_type)
                model.add_item(parameter_type)
            model.select_item(parameter_type)

    def select_item_in_views(self, item_data):
        for view in self.views:
            view.select_item(item_data)

    def change_item_in_models(self, *args):
        value, = args
        for model in self.models:
            model.change_data(value)

    def change_item_in_views(self, *args):
        pass

    def delete_item_in_models(self):
        pass

    def delete_item_in_views(self, index):
        pass

    def clear_views(self):
        pass

    def notify_model(self, operation, parameter):
        pass
