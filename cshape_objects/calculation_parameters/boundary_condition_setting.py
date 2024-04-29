from abc import ABC, abstractmethod
from enum import Enum

from cshape_objects.cshape_types import CShapeTypes


class ConditionTypes(Enum):
    black = 'Black'
    reflective = 'Reflective'
    periodic = 'Periodic'


class BoundaryConditionSetting(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def set_condition_type(self, condition_type: str | list[str]) -> str | list[str]:
        return condition_type

    @abstractmethod
    def set_albedo(self, albedo: float) -> float | None:
        pass

    @abstractmethod
    def get_condition_type(self, condition_type: str | list[str]) -> tuple:
        pass

    @abstractmethod
    def get_albedo(self, albedo: float) -> tuple:
        pass


class AllDirectionsSetting(BoundaryConditionSetting):
    def __init__(self):
        super().__init__()

    def set_condition_type(self, condition_type: str | list[str]) -> str:
        if type(condition_type) is list:
            return condition_type[0]
        return condition_type

    def set_albedo(self, albedo: float) -> None:
        return None

    def get_condition_type(self, condition_type: str) -> tuple:
        all_condition_types: dict = {
            'black': ConditionTypes.black.value,
            'reflective': ConditionTypes.reflective.value,
            'periodic': ConditionTypes.periodic.value
        }
        return CShapeTypes.Enum, [all_condition_types, condition_type]

    def get_albedo(self, albedo: float) -> tuple:
        return CShapeTypes.Range, None


class AllDirectionsWithAlbedoSetting(BoundaryConditionSetting):
    def __init__(self):
        super().__init__()

    def set_condition_type(self, condition_type: str) -> str:
        return condition_type

    def set_albedo(self, albedo: float) -> float:
        if albedo is None:
            return 0.0
        return albedo

    def get_condition_type(self, condition_type: str) -> tuple:
        all_condition_types: dict = {
            'black': ConditionTypes.black.value,
            'reflective': ConditionTypes.reflective.value,
            'periodic': ConditionTypes.periodic.value
        }
        return CShapeTypes.Enum, [all_condition_types, condition_type]

    def get_albedo(self, albedo: float) -> tuple:
        return CShapeTypes.Float, [albedo, (0.0, 1.0)]


class SeparateDirectionsSetting(BoundaryConditionSetting):
    def __init__(self):
        super().__init__()

    def set_condition_type(self, condition_type: str | list[str]) -> list[str]:
        if type(condition_type) is not list:
            return [condition_type, condition_type, condition_type]
        return condition_type

    def set_albedo(self, albedo: float) -> tuple:
        return CShapeTypes.Range, None

    def get_condition_type(self, condition_type: list[str]) -> tuple:
        print(condition_type)
        condition_type_x, condition_type_y, condition_type_z = condition_type
        all_condition_types = (ConditionTypes.black.value, ConditionTypes.reflective.value, ConditionTypes.periodic.value)
        return CShapeTypes.Vector3DComboBox, ['X', condition_type_x, all_condition_types,
                                              'Y', condition_type_y, all_condition_types,
                                              'Z', condition_type_z, all_condition_types]

    def get_albedo(self, albedo: float) -> tuple:
        return CShapeTypes.Range, None


class SeparateDirectionsWithAlbedoSetting(BoundaryConditionSetting):
    def __init__(self):
        super().__init__()

    def set_condition_type(self, condition_type: list[str]) -> list[str]:
        return condition_type

    def set_albedo(self, albedo: float) -> float:
        return albedo

    def get_condition_type(self, condition_type: list[str]) -> tuple:
        condition_type_x, condition_type_y, condition_type_z = condition_type
        all_condition_types = (
            ConditionTypes.black.value, ConditionTypes.reflective.value, ConditionTypes.periodic.value)
        return CShapeTypes.Vector3DComboBox, ['X', condition_type_x, all_condition_types,
                                              'Y', condition_type_y, all_condition_types,
                                              'Z', condition_type_z, all_condition_types]

    def get_albedo(self, albedo: float) -> tuple:
        return CShapeTypes.Float, [albedo, (0.0, 1.0)]
