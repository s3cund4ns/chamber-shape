from surfaces.surface import SurfacesTypes, Surface


class Cylinder(Surface):
    def __init__(self, position: list[float, float, float], color: list[float, float, float, float], radius):
        super().__init__(position, color)
        self.type = SurfacesTypes.Cylinder
        self.parameters_names = ['radius']
        self.parameters_values = [radius]

    def set_parameters(self, parameters: list):
        self.parameters_values = parameters


