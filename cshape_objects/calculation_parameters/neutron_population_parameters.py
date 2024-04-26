from dataclasses import dataclass

from cshape_objects.calculation_parameters.calculation_parameter import CalculationParameter, CalculationParametersTypes
from cshape_objects.cshape_object import CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes


@dataclass
class Properties(CShapeObjectProperties):
    Name = 'Neutron population'
    NeutronsPerGeneration = 'Neutrons per generation'
    ActiveGenerations = 'Active generations'
    InactiveGenerations = 'Inactive generations'


class NeutronPopulationParameters(CalculationParameter):
    def __init__(self):
        super().__init__()
        self.parameter_type = CalculationParametersTypes.NeutronPopulation
        self.properties = Properties()
        self.name = 'Neutron population'
        self.neutrons_per_generation: int = 0
        self.active_generations: int = 0
        self.inactive_generations: int = 0

    def get_data(self):
        return {
            self.properties.NeutronsPerGeneration: (CShapeTypes.Int, self.neutrons_per_generation),
            self.properties.ActiveGenerations: (CShapeTypes.Int, self.active_generations),
            self.properties.InactiveGenerations: (CShapeTypes.Int, self.inactive_generations)
        }

    def set_data(self, properties: tuple):
        name, value = properties
        match name:
            case self.properties.NeutronsPerGeneration:
                self.neutrons_per_generation = value
            case self.properties.ActiveGenerations:
                self.active_generations = value
            case self.properties.InactiveGenerations:
                self.inactive_generations = value
