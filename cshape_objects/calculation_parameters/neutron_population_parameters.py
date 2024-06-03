from dataclasses import dataclass

from cshape_objects.calculation_parameters.calculation_parameter import CalculationParameter, CalculationParametersTypes
from cshape_objects.cshape_object import CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes


@dataclass
class Properties(CShapeObjectProperties):
    Name = 'Parameter'
    NeutronsPerCycle = 'Neutrons per cycle'
    ActiveCycles = 'Active cycles'
    InactiveCycles = 'Inactive cycles'


class NeutronPopulationParameters(CalculationParameter):
    def __init__(self):
        super().__init__()
        self.parameter_type = CalculationParametersTypes.NeutronPopulation
        self.properties = Properties()
        self.name = 'Neutron population'
        self.neutrons_per_cycle: int = 0
        self.active_cycles: int = 0
        self.inactive_cycles: int = 0

    def get_data(self):
        return {
            self.properties.NeutronsPerCycle: (CShapeTypes.Int, [self.neutrons_per_cycle, (0, 99999999)]),
            self.properties.ActiveCycles: (CShapeTypes.Int, [self.active_cycles, (0, 99999999)]),
            self.properties.InactiveCycles: (CShapeTypes.Int, [self.inactive_cycles, (0, 99999999)])
        }

    def set_data(self, properties: tuple):
        name, value = properties
        match name:
            case self.properties.NeutronsPerCycle:
                self.neutrons_per_cycle = value
            case self.properties.ActiveCycles:
                self.active_cycles = value
            case self.properties.InactiveCycles:
                self.inactive_cycles = value

    def dump_data(self) -> dict:
        return {
            self.properties.Name: self.name,
            self.properties.NeutronsPerCycle: self.neutrons_per_cycle,
            self.properties.ActiveCycles: self.active_cycles,
            self.properties.InactiveCycles: self.inactive_cycles
        }
