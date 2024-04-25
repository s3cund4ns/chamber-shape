from dataclasses import dataclass

from cshape_objects.cshape_object import CShapeObject, CShapeObjectTypes


@dataclass
class CalculationParametersTypes:
    NoneType = None
    NeutronPopulation = 'Neutron population'


class CalculationParameter(CShapeObject):
    def __init__(self):
        super().__init__()
        self.type = CShapeObjectTypes.CalculationParameter
        self.parameter_type: CalculationParametersTypes = CalculationParametersTypes.NoneType

    def get_data(self):
        pass

    def set_data(self, data):
        pass