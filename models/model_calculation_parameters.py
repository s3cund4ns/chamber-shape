from cshape_objects.calculation_parameters.calculation_parameter import CalculationParameter
from cshape_objects.calculation_parameters.calculation_parameter_creator import create_calculation_parameter
from project_data.model import Model


class ModelCalculationParameters(Model):
    def __init__(self):
        super().__init__()
        self.data: list = []
        self.selected_parameter_type: str = ''

    def find_parameter(self, parameter_type: str):
        for parameter in self.data:
            if parameter.parameter_type == parameter_type:
                return parameter
        return None

    def add_item(self, parameter_type: str):
        item = create_calculation_parameter(parameter_type)
        self.data.append(item)

    def select_item(self, parameter_type: str):
        self.selected_parameter_type = parameter_type
        selected_item: CalculationParameter = self.find_parameter(parameter_type)
        self.view_model.select_item_in_views(selected_item.get_data())

    def change_data(self, value):
        selected_item: CalculationParameter = self.find_parameter(self.selected_parameter_type)
        selected_item.set_data(value)
