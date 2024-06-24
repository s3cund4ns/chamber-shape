import xml.etree.ElementTree as ET

from preprocessor.input_data_generator import InputDataGenerator


class InputDataGeneratorForOpenMC(InputDataGenerator):
    def __init__(self):
        super().__init__()
        self.tokens: dict = {
            'Surface': 'surf',
            'XPlane': 'x-plane',
            'YPlane': 'y-plane',
            'ZPlane': 'z-plane',
            'XCylinder': 'x-cylinder',
            'YCylinder': 'y-cylinder',
            'ZCylinder': 'z-cylinder',
            'Sphere': 'sphere',
            'Cone': 'cone',
            'XTorus': 'torx',
            'YTorus': 'tory',
            'ZTorus': 'torz',
            'TriangularPrism': 'tric',
            'RectangularPrism': 'rect',
            'XHexagonalPrism': 'hexxc',
            'YHexagonalPrism': 'hexyc',
            'OctagonalPrism': 'octa',
            'DodecagonalPrism': 'dode',
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
            'Lattice': 'lat',
            'SquareLattice': '1',
            'Neutron population': 'set pop',
            'Boundary conditions': 'set bc',
            'Energy grid': 'ene',
            'Arbitrary Defined': '1',
            'Equal Energy Width Bins': '2',
            'Equal Lethargy Width Bins': '3',
            'Black': '1',
            'Reflective': '2',
            'Periodic': '3',
            'MaterialDetector': 'dm',
            'LatticeDetector': 'dl'
        }

        self.root = ET.Element('opemnc')
        self.materials = ET.SubElement(self.root, 'materials')
        self.geometry = ET.SubElement(self.root, 'geometry')
        self.settings = ET.SubElement(self.root, 'settings')
        self.text = ET.tostring(self.root, encoding='utf-8', xml_declaration=True).decode('utf-8')

    def generate_basic_data(self, basic_data):
        return [self.text]

    def generate_materials_data(self, materials: list):
        pass

    def generate_surfaces_data(self, surfaces: list):
        for surface_data in surfaces:
            surface_info = []
            for key in surface_data:
                value = surface_data[key]
                if key == 'Color':
                    continue
                if key == 'Size':
                    continue
                if key == 'Length':
                    continue
                if type(value) is list:
                    token = self.list_to_str(value, ' ')
                    surface_info.append(token)
                    continue
                if value not in self.tokens:
                    surface_info.append(value)
                    continue
                token = self.tokens.get(value)
                surface_info.append(token)

            print(surface_info)
            surface_id = str(surfaces.index(surface_data)+1)
            coeffs_text = f'{surface_info[2]} {surface_info[3]}'
            ET.SubElement(self.geometry, 'surface', id=surface_id, type=surface_info[0], coeffs=coeffs_text)
        self.text = ET.tostring(self.root, encoding='utf-8', xml_declaration=True).decode('utf-8')
        print(self.text)
        return [self.text]

    def generate_cells_data(self, cells: list, all_surfaces: list):
        return []

    def generate_pins_data(self, pins: list, all_materials: list):
        return []

    def generate_lattices_data(self, lattices):
        return []

    def generate_calculation_parameters_data(self, calculation_parameters: list):
        return []

    def generate_detectors_data(self, detectors: list, energy_grid, all_elements: list):
        return []

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item