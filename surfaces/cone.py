from surfaces.surface import SurfacesTypes, Surface


class Cone(Surface):
    def __init__(self, position: list[float, float, float], color: list[float, float, float, float], radius, height):
        super().__init__(position, color)
        self.type = SurfacesTypes.Cone
        self.parameters_names = ['radius', 'height']
        self.parameters_values = [radius, height]

    def set_parameters(self, parameters: list):
        self.parameters_values = parameters

