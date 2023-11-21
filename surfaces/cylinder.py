from surfaces.surface import SurfacesTypes, Surface


class Cylinder(Surface):
    def __init__(self, pos_x, pos_y, pos_z, rot_x, rot_y, rot_z, radius):
        super().__init__(pos_x, pos_y, pos_z, rot_x, rot_y, rot_z)
        self.type = SurfacesTypes.Cylinder
        self.parameters = {'radius': radius}

    def set_properties(self, position: list, rotation: list, parameters: list):
        pos_x, pos_y, pos_z = position
        rot_x, rot_y, rot_z = rotation
        radius, = parameters
        self.position: dict = {'x': pos_x, 'y': pos_y, 'z': pos_z}
        self.rotation: dict = {'x': rot_x, 'y': rot_y, 'z': rot_z}
        self.parameters = {'radius': radius}


