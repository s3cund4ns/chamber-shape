from surfaces.surface import SurfacesTypes, Surface


class Cone(Surface):
    def __init__(self, pos_x, pos_y, pos_z, rot_x, rot_y, rot_z, radius, height):
        super().__init__(pos_x, pos_y, pos_z, rot_x, rot_y, rot_z)
        self.type = SurfacesTypes.Cone
        self.parameters = {'radius': radius, 'height': height}

    def set_properties(self, position: list, rotation: list, parameters: list):
        pos_x, pos_y, pos_z = position
        rot_x, rot_y, rot_z = rotation
        radius, height = parameters
        self.position: dict = {'x': pos_x, 'y': pos_y, 'z': pos_z}
        self.rotation: dict = {'x': rot_x, 'y': rot_y, 'z': rot_z}
        self.parameters = {'radius': radius, 'height': height}

