from dataclasses import dataclass

from cshape_objects.cshape_object import CShapeObjectTypes, CShapeObject, CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes


@dataclass
class Properties(CShapeObjectProperties):
    ImpKeff = 'ImpKeff'
    AbsKinf = 'AbsKinf'


class CalculationOutput(CShapeObject):
    def __init__(self):
        super().__init__()
        self.type = CShapeObjectTypes.CalculationOutput
        self.properties = Properties()
        self.name = 'Calculation output'
        self.imp_keff: tuple | None = None
        self.abs_kinf: tuple | None = None

    def is_clean(self) -> bool:
        return self.imp_keff is None and self.abs_kinf is None

    def clear(self):
        self.imp_keff = None
        self.abs_kinf = None

    def get_data(self):
        return {
            self.properties.ImpKeff: (CShapeTypes.Info, self.imp_keff),
            self.properties.AbsKinf: (CShapeTypes.Info, self.abs_kinf)
        }

    def set_data(self, properties: tuple):
        name, values = properties
        value, variation = values
        error = value * variation
        match name:
            case self.properties.ImpKeff:
                self.imp_keff = (value, error)
            case self.properties.AbsKinf:
                self.abs_kinf = (value, error)
