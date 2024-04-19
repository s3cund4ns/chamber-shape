import os

from preprocessor.input_data_generator import InputDataGenerator


class InputDataGeneratorForSerpent(InputDataGenerator):
    def __init__(self):
        super().__init__()
        self.tokens: dict = {
            'Surface': 'surf',
            'Plane': 'plane',
            'Sphere': 'sph',
            'Cylinder': 'cyl',
            'Cone': 'cone',
            'XHexagonalPrism': 'hexxc',
            'YHexagonalPrism': 'hexyc',
            'Material': 'mat',
            'Atomic': '',
            'Massive': '-',
            'Void': 'void',
            'Outside': 'outside',
            'Universe': 'fill',
            'Nuclides': '',
            'Cell': 'cell',
            'In': '-',
            'Out': '',
            'Pin': 'pin',
            'Lattice': 'lat'
        }

    def generate_basic_data(self, basic_data):
        input_data = []
        title: str = basic_data[0]
        nuclear_data: dict = basic_data[1]
        nuclear_data_path: str = basic_data[2]
        text = ''
        text += f'set title "{title}"\n'
        for key in nuclear_data.keys():
            text += f'set {key} "{nuclear_data_path}/{nuclear_data[key]}"\n'
        input_data.append(text)

        return input_data

    def generate_materials_data(self, materials: dict):
        input_data = []
        for material_data in materials:
            material_info = []
            nuclides_info = []
            for key in material_data:
                value = material_data[key]
                if key == 'Nuclides':
                    nuclides_info = value
                    continue
                if value not in self.tokens:
                    material_info.append(value)
                    continue
                token = self.tokens.get(value)
                material_info.append(token)

            key_word, name, density, mode = material_info
            material_text = f'{key_word} {name} {mode}{density}\n'

            nuclides_text = ''
            for nuclide_info in nuclides_info:
                nuclide_text = self.list_to_str(nuclide_info, ' ')
                nuclides_text += f'{nuclide_text}\n'

            text = f'{material_text} {nuclides_text}'
            input_data.append(text)
            input_data.append('\n')

        return input_data

    def generate_surfaces_data(self, surfaces: dict):
        input_data = []
        for surface_data in surfaces:
            surface_info = []
            for key in surface_data:
                value = surface_data[key]
                if type(value) is list:
                    token = self.list_to_str(value, ' ')
                    surface_info.append(token)
                    continue
                if value not in self.tokens:
                    surface_info.append(value)
                    continue
                token = self.tokens.get(value)
                surface_info.append(token)

            surface_info[0], surface_info[1] = surface_info[1], surface_info[0]

            surface_text = f"{self.tokens.get('Surface')} "
            for token in surface_info:
                surface_text += f'{token} '

            input_data.append(surface_text)
            input_data.append('\n')

        return input_data

    def generate_cells_data(self, cells: list):
        input_data = []
        for cell_data in cells:
            cell_info = []
            surfaces_info = []
            for key in cell_data:
                value = cell_data[key]
                if key == 'Surfaces':
                    surfaces_info = value
                    continue
                if value not in self.tokens:
                    cell_info.append(value)
                    continue
                token = self.tokens.get(value)
                cell_info.append(token)

            key_word, name, fill, entire = cell_info
            if fill == 'Universe':
                fill = self.tokens.get(fill)
            if fill == self.tokens.get('Material'):
                fill = ''
            if fill == 'Void' or fill == 'Outside':
                fill = self.tokens.get(fill)
                entire = ''
            if entire is None:
                entire = ''

            universe_text = f'{key_word} {name} {fill} {entire}'

            surfaces_text = ''
            for surface_info in surfaces_info:
                surface_index, surface_side = surface_info
                surface_side = self.tokens.get(surface_side)
                surface_text = f'{surface_side}{surface_index}'
                surfaces_text += f'{surface_text} '

            text = f'{universe_text} {surfaces_text}'

            input_data.append(text)
            input_data.append('\n')

        return input_data

    def generate_pins_data(self, pins):
        input_data = []
        for pin_data in pins:
            pin_info = []
            regions_info = []
            for key in pin_data:
                value = pin_data[key]
                if key == 'Regions':
                    regions_info = value
                    continue
                if value not in self.tokens:
                    pin_info.append(value)
                    continue
                token = self.tokens.get(value)
                pin_info.append(token)

            key_word, name = pin_info
            pin_text = f'{key_word} {name}'

            regions_text = ''
            for region_info in regions_info:
                region_name, region_radius = region_info
                region_text = f'{region_name} {region_radius}\n'
                regions_text += region_text

            text = f'{pin_text}\n{regions_text}'
            input_data.append(text)
            input_data.append('\n')

        return input_data

    def generate_lattices_data(self, lattices):
        input_data = []
        for lattice_data in lattices:
            lattice_info = []
            universes_text = ''
            for key in lattice_data:
                value = lattice_data[key]
                if key == 'Universe Matrix':
                    for row in range(lattice_data['Size'][0]):
                        for column in range(lattice_data['Size'][1]):
                            universes_text += f' {value[row][column]}'
                        universes_text += '\n'
                    continue
                if type(value) is list:
                    token = self.list_to_str(value, ' ')
                    lattice_info.append(token)
                    continue
                if value not in self.tokens:
                    lattice_info.append(value)
                    continue
                token = self.tokens.get(value)
                lattice_info.append(token)

            key_word, name, position, size, pitch = lattice_info[:5]
            text = f'{key_word} {position} {size} {pitch}\n{universes_text}'
            input_data.append(text)
            input_data.append('\n')

        return input_data
