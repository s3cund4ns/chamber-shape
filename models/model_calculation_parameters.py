from cshape_objects.calculation_parameters.boundary_conditions import BoundaryConditions
from cshape_objects.calculation_parameters.calculation_parameter import CalculationParameter
from cshape_objects.calculation_parameters.calculation_parameter_creator import create_calculation_parameter
from cshape_objects.calculation_parameters.neutron_population_parameters import NeutronPopulationParameters
from models.model_input_data import ModelInputData
from project_data.model import Model


class ModelCalculationParameters(Model):
    def __init__(self):
        super().__init__()
        self.data: list = []
        self.add_item(None)
        self.selected_parameter_type: str = ''

        self.input_data_model: ModelInputData | None = None

    def find_parameter(self, parameter_type: str):
        for parameter in self.data:
            if parameter.parameter_type == parameter_type:
                return parameter
        return None

    def add_item(self, *args):
        neutron_population: NeutronPopulationParameters = NeutronPopulationParameters()
        # boundary_conditions: BoundaryConditions = BoundaryConditions()
        self.data.append(neutron_population)
        # self.data.append(boundary_conditions)

    def select_item(self, parameter_type: str):
        self.selected_parameter_type = parameter_type
        selected_item: CalculationParameter = self.find_parameter(parameter_type)
        self.view_model.select_item_in_views(selected_item.get_data())

    def change_data(self, value):
        selected_item: CalculationParameter = self.find_parameter(self.selected_parameter_type)
        selected_item.set_data(value)
        self.input_data_model.update_calculation_parameters_data(self.dump_data())

    def dump_data(self):
        data = []
        for parameter in self.data:
            data.append(parameter.dump_data())
        return data

    def load_data(self, calculation_parameters_data: list):
        for parameter in calculation_parameters_data:
            parameter_type = parameter['Parameter']
            self.add_item(parameter_type)
            self.select_item(parameter_type)
            parameter_tuple = tuple(parameter.items())
            for property in parameter_tuple[1:]:
                self.change_data(property)
