from dataclasses import dataclass
from enum import Enum

from cshape_objects.calculation_parameters.boundary_condition_setting import AllDirectionsSetting, \
    AllDirectionsWithAlbedoSetting, SeparateDirectionsSetting, SeparateDirectionsWithAlbedoSetting, \
    BoundaryConditionSetting, ConditionTypes
from cshape_objects.calculation_parameters.calculation_parameter import CalculationParameter, CalculationParametersTypes
from cshape_objects.cshape_object import CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes


@dataclass
class Properties(CShapeObjectProperties):
    Name = 'Boundary conditions'
    Setting = 'Setting'
    ConditionType = 'Condition type'
    Albedo = 'Albedo'


@dataclass
class Setting:
    AllDirections = 'AllDirections'
    AllDirectionsWithAlbedo = 'AllDirectionsWithAlbedo'
    SeparateDirections = 'SeparateDirections'
    SeparateDirectionsWithAlbedo = 'SeparateDirectionsWithAlbedo'


class BoundaryConditions(CalculationParameter):
    def __init__(self):
        super().__init__()
        self.parameter_type = CalculationParametersTypes.BoundaryConditions
        self.properties = Properties()
        self.name = 'Boundary conditions'
        self.settings: dict = {
            Setting.AllDirections: 'AllDirections',
            Setting.AllDirectionsWithAlbedo: 'AllDirectionsWithAlbedo',
            Setting.SeparateDirections: 'SeparateDirections',
            Setting.SeparateDirectionsWithAlbedo: 'SeparateDirectionsWithAlbedo'
        }
        self.setting: str = self.settings[Setting.AllDirections]
        self.setting_behaviour_map: dict = {
            Setting.AllDirections: AllDirectionsSetting,
            Setting.AllDirectionsWithAlbedo: AllDirectionsWithAlbedoSetting,
            Setting.SeparateDirections: SeparateDirectionsSetting,
            Setting.SeparateDirectionsWithAlbedo: SeparateDirectionsWithAlbedoSetting
        }
        self.setting_behaviour: BoundaryConditionSetting = self.__create_setting_behaviour()
        self.condition_type: str | list[str] = self.setting_behaviour.set_condition_type(ConditionTypes.black.value)
        self.albedo: float | None = self.setting_behaviour.set_albedo(0.0)

    def __create_setting_behaviour(self):
        return self.setting_behaviour_map[self.setting]()

    def get_data(self):
        return {
            self.properties.Setting: (CShapeTypes.Enum, [self.settings, self.setting]),
            self.properties.ConditionType: self.setting_behaviour.get_condition_type(self.condition_type),
            self.properties.Albedo: self.setting_behaviour.get_albedo(self.albedo)
        }

    def set_data(self, properties: tuple):
        name, value = properties
        match name:
            case self.properties.Setting:
                self.setting = self.settings[value]
                self.setting_behaviour: BoundaryConditionSetting = self.__create_setting_behaviour()
                self.condition_type = self.setting_behaviour.set_condition_type(self.condition_type)
                self.albedo = self.setting_behaviour.set_albedo(self.albedo)
            case self.properties.ConditionType:
                self.condition_type = self.setting_behaviour.set_condition_type(value)
