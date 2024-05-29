from project_data.view_model import ViewModel


class ViewModelCalculationParameters(ViewModel):
    def __init__(self):
        super().__init__()
        self.parameter_type_map: dict = {
            'Размножение Нейтронов': 'Neutron population',
            'Граничные Условия': 'Boundary conditions',
            'Энергетическая Сетка': 'Energy grid'
        }

    def add_item_to_models(self, *args):
        pass

    def add_item_to_views(self, *args):
        pass

    def select_item_in_models(self, parameter_type: str):
        mapped_parameter_type = self.parameter_type_map[parameter_type]
        for model in self.models:
            model.select_item(mapped_parameter_type)

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
