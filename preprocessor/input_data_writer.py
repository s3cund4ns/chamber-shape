from PySide6.QtCore import QObject

from cshape_objects.material import Material


class InputDataWriter(QObject):
    def __init__(self):
        super().__init__()
        self.materials_data = []
        self.pins_data = []
        self.surfaces_data = []
        self.cells_data = []
        self.serpent_dict = {
            'Surface': 'surf',
            'Plane': 'plane',
            'Sphere': 'sph',
            'Cylinder': 'cyl',
            'Cone': 'cone',
            'XHexagonalPrism': 'hexxc',
            'YHexagonalPrism': 'hexyc',
            'Material': 'mat',
            'Cell': 'cell',
            'Pin': 'pin'
        }

    def update_surface_data(self, surfaces_data: list):
        if len(self.surfaces_data) > 0:
            self.surfaces_data = []
        for surface_data in surfaces_data:
            key_word = 'surf'
            surface_type = surface_data.get_type()
            surface_type_text = self.serpent_dict.get(surface_type)
            surface_id = str(surfaces_data.index(surface_data) + 1)
            surface_position_x = str(surface_data.get_values()[0][0])
            surface_position_y = str(surface_data.get_values()[0][1])
            surface_position_z = str(surface_data.get_values()[0][2])
            surface_parameters = surface_data.get_values()[2]
            surface_parameters_text = ''
            if len(surface_parameters) > 0:
                for parameter in surface_parameters:
                    surface_parameters_text += str(parameter)

            if surface_type == 'Sphere':
                text = (f'{key_word} {surface_type_text} {surface_id} {surface_position_x} {surface_position_y} '
                        f'{surface_position_z} {surface_parameters_text}\n')
            else:
                text = (f'{key_word} {surface_type_text} {surface_id} {surface_position_x} {surface_position_y} '
                        f'{surface_parameters_text}\n')
            self.surfaces_data.append(text)
        self.surfaces_data.append('\n')

    def update_material_data(self, materials_data: list):
        if len(self.materials_data) > 0:
            self.materials_data = []
        for material_data in materials_data:
            key_word = 'mat'
            material_name = material_data.get_name()
            material_density = str(material_data.get_density())
            nuclides_text = ''
            for nuclide in material_data.get_nuclides():
                nuclides_text += f'{material_data.get_nuclides().index(nuclide)} {str(nuclide)}\n'

            text = f'{key_word} {material_name} {material_density}\n{nuclides_text}'
            self.materials_data.append(text)
            self.materials_data.append('\n')

    def update_cell_data(self, cells_data: list, surfaces_data: list):
        if len(self.cells_data) > 0:
            self.cells_data = []
        for cell_data in cells_data:
            key_word = self.serpent_dict.get(cell_data.get_type())
            cell_name = cell_data.get_name()
            cell_fill = ''
            if type(cell_data.get_fill()) is str:
                cell_fill = cell_data.get_fill()
            elif type(cell_data.get_fill()) is Material:
                cell_fill = cell_data.get_fill().get_name()
            elif type(cell_data.get_fill()) is int:
                cell_fill = str(cell_data.fill.get_fill())
            surfaces_text = ''
            for surface in cell_data.get_surfaces():
                if surface[0] in surfaces_data:
                    surface_id = surfaces_data.index(surface[0]) + 1
                    surface_id = surface_id * surface[1]
                    surfaces_text += f'{surface_id} '

            text = f'{key_word} {cell_name} {cell_fill} {surfaces_text}\n'
            self.cells_data.append(text)

    def update_pin_data(self, pins_data: list):
        if len(self.pins_data) > 0:
            self.pins_data = []
        for pin_data in pins_data:
            key_word = self.serpent_dict.get(pin_data.get_type())
            pin_universe = str(pin_data.get_universe())
            regions_text = ''
            for region in pin_data.get_regions():
                region_name = region[0].get_name()
                region_radius = str(region[1])
                regions_text += f'{region_name} {region_radius}\n'

            text = f'{key_word} {pin_universe}\n{regions_text}'
            self.pins_data.append(text)

    def write_to_file(self):
        with open('Projects/project.inp', 'w') as file:
            file.writelines(self.materials_data)
            file.writelines(self.pins_data)
            file.writelines(self.surfaces_data)
            file.writelines(self.cells_data)
