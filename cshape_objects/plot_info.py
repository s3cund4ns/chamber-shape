from dataclasses import dataclass

from cshape_objects.cshape_object import CShapeObject, CShapeObjectTypes, CShapeObjectProperties
from cshape_objects.cshape_types import CShapeTypes


@dataclass
class Properties(CShapeObjectProperties):
    ObjectsForDiagram = 'Objects For Diagram'
    ObjectForDiagram = 'Diagram'
    XLabel = 'X Label'
    YLabel = 'Y Label'
    XScale = 'X Scale'
    YScale = 'Y Scale'
    XRange = 'X Range'
    YRange = 'Y Range'


@dataclass
class Scale:
    linear = 'Linear'
    logarithmic = 'Logarithmic'


class PlotInfo(CShapeObject):
    def __init__(self):
        super().__init__()
        self.type = CShapeObjectTypes.PlotInfo
        self.properties = Properties()
        self.properties.name = 'Plot Info'
        self.objects_for_diagram: list[CShapeObject] = []
        self.object_for_diagram: CShapeObject | None = None
        self.x_label: str = ''
        self.y_label: str = ''
        self.x_scale: str = Scale.linear
        self.y_scale: str = Scale.linear
        self.x_range: list[float] = [0.0, 100.0]
        self.y_range: list[float] = [0.0, 100.0]

    def get_name_of_object_for_diagram(self) -> str | None:
        if self.object_for_diagram is None:
            return None
        return self.object_for_diagram.get_name()

    def get_names_of_objects_for_diagram(self) -> list[str]:
        names_of_objects_for_diagram: list[str] = []
        for object_for_diagram in self.objects_for_diagram:
            name = object_for_diagram.get_name()
            names_of_objects_for_diagram.append(name)

        return names_of_objects_for_diagram

    def set_objects_for_diagram(self, objects_for_diagram: list[CShapeObject]) -> None:
        self.objects_for_diagram = objects_for_diagram

    def get_data(self):
        return {
            self.properties.ObjectForDiagram: (CShapeTypes.Reference, [self.get_name_of_object_for_diagram(),
                                                                       self.get_names_of_objects_for_diagram()]),
            self.properties.XLabel: (CShapeTypes.String, self.x_label),
            self.properties.YLabel: (CShapeTypes.String, self.y_label),
            self.properties.XScale: (CShapeTypes.Enum, [{Scale.linear: Scale.linear,
                                                         Scale.logarithmic: Scale.logarithmic},
                                                        self.x_scale]),
            self.properties.YScale: (CShapeTypes.Enum, [{Scale.linear: Scale.linear,
                                                         Scale.logarithmic: Scale.logarithmic},
                                                        self.y_scale]),
            self.properties.XRange: (CShapeTypes.Vector2DFloat, [self.x_range, (-99999.9999, 99999.9999)]),
            self.properties.YRange: (CShapeTypes.Vector2DFloat, [self.x_range, (-99999.9999, 99999.9999)])
        }

    def set_data(self, properties: tuple):
        name, value = properties
        match name:
            case self.properties.ObjectForDiagram:
                index = value
                self.object_for_diagram = self.objects_for_diagram[index]
            case self.properties.XLabel:
                self.x_label = value
            case self.properties.YLabel:
                self.y_label = value
            case self.properties.XScale:
                self.x_scale = value
            case self.properties.YScale:
                self.y_scale = value
            case self.properties.XRange:
                self.x_range = value
            case self.properties.YRange:
                self.y_range = value
