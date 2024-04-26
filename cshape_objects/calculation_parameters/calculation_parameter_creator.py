from cshape_objects.calculation_parameters.calculation_parameter import CalculationParametersTypes
from cshape_objects.calculation_parameters.neutron_population_parameters import NeutronPopulationParameters

calculation_parameter_types: dict = {
    CalculationParametersTypes.NeutronPopulation: NeutronPopulationParameters
}


def create_calculation_parameter(calculation_parameter_type):
    return calculation_parameter_types[calculation_parameter_type]()
