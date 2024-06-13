from dataclasses import dataclass

from cshape_objects.calculation_parameters.calculation_parameter import CalculationParameter, CalculationParametersTypes
from cshape_objects.cshape_object import CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes


@dataclass
class Properties(CShapeObjectProperties):
    Name = 'Parameter'
    GridName = 'Name'
    Type = 'Type'
    EnergyBins = 'Energy Bins'
    MinEnergy = 'Min Energy (MeV)'
    MaxEnergy = 'Max Energy (MeV)'
    BinsNumber = 'Bins Number'
    Add = 'Add'


@dataclass
class EnergyGridType:
    arbitrary_defined = 'Arbitrary Defined'
    equal_energy_width_bins = 'Equal Energy Width Bins'
    equal_lethargy_width_bins = 'Equal Lethargy Width Bins'


class EnergyGrid(CalculationParameter):
    def __init__(self):
        super().__init__()
        self.parameter_type: CalculationParametersTypes = CalculationParametersTypes.EnergyGrid
        self.properties = Properties()
        self.name: str = 'Energy grid'
        self.grid_name: str = 'EnergyGrid'
        self.grid_type: str = EnergyGridType.equal_energy_width_bins
        self.energy_bins: list[float] = []
        self.min_energy: float = 0.0
        self.max_energy: float = 0.0
        self.bins_number: int = 0

    def get_name(self):
        return self.grid_name

    def get_data(self):
        if self.grid_type == EnergyGridType.arbitrary_defined:
            return {
                self.properties.GridName: (CShapeTypes.String, self.grid_name),
                self.properties.Type: (CShapeTypes.Enum, [{EnergyGridType.arbitrary_defined: 'Arbitary Defined',
                                                           EnergyGridType.equal_energy_width_bins: 'Equal Energy Width Bins',
                                                           EnergyGridType.equal_lethargy_width_bins: 'Equal Lethargy Width Bins'},
                                                          self.grid_type]),
                self.properties.EnergyBins: (CShapeTypes.List, self.energy_bins)
            }
        else:
            return {
                self.properties.GridName: (CShapeTypes.String, self.grid_name),
                self.properties.Type: (CShapeTypes.Enum, [{EnergyGridType.arbitrary_defined: 'Arbitary Defined',
                                                        EnergyGridType.equal_energy_width_bins: 'Equal Energy Width Bins',
                                                        EnergyGridType.equal_lethargy_width_bins: 'Equal Lethargy Width Bins'},
                                                          self.grid_type]),
                self.properties.BinsNumber: (CShapeTypes.Int, [self.bins_number, (0, 99999999)]),
                self.properties.MinEnergy: (CShapeTypes.Float, [self.min_energy, (0.00001, 99999.9999)]),
                self.properties.MaxEnergy: (CShapeTypes.Float, [self.max_energy, (0.00001, 99999.9999)])
            }

    def set_data(self, properties: tuple):
        name, value = properties
        match name:
            case self.properties.GridName:
                self.grid_name = value
            case self.properties.Type:
                self.grid_type = value
            case self.properties.EnergyBins:
                index, energy, unit = value
                self.energy_bins.append(energy)
            case self.properties.MinEnergy:
                self.min_energy = value / 100000000
            case self.properties.MaxEnergy:
                self.max_energy = value
            case self.properties.BinsNumber:
                self.bins_number = value

    def dump_data(self) -> dict:
        if self.grid_type == EnergyGridType.arbitrary_defined:
            return {
                self.properties.Name: self.name,
                self.properties.GridName: self.grid_name,
                self.properties.Type: self.grid_type,
                self.properties.EnergyBins: self.energy_bins
            }
        else:
            return {
                self.properties.Name: self.name,
                self.properties.GridName: self.grid_name,
                self.properties.Type: self.grid_type,
                self.properties.BinsNumber: self.bins_number,
                self.properties.MinEnergy: self.min_energy,
                self.properties.MaxEnergy: self.max_energy
            }
