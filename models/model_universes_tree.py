from cshape_objects.lattices.finite_lattices_2d.lattice_square import LatticeSquare
from cshape_objects.lattices.lattice import Lattice
from cshape_objects.lattices.lattice_creator import create_lattice
from data_structs.tree import Tree
from models.cell_data_dumper import CellDataDumper
from models.lattice_data_dumper import LatticeDataDumper
from models.pin_data_dumper import PinDataDumper
from models.universe_data_dumper import UniverseDataDumper
from solvers.solver_dict import serpent_dict
from project_data.model import Model
from cshape_objects.cell import Cell
from cshape_objects.pin import Pin
from cshape_objects.universe import Universe


class ModelUniversesTree(Model):
    def __init__(self):
        super(ModelUniversesTree, self).__init__()
        self.data: Tree = Tree()
        self.key_of_selected_item: str = ''
        self.selected_item_index = -1
        self.elements_amount = 0

        self.materials_model = None
        self.surfaces_model = None
        self.input_data_model = None

        self.universe_data_dumper: UniverseDataDumper = UniverseDataDumper()
        self.cell_data_dumper: CellDataDumper = CellDataDumper()
        self.pin_data_dumper: PinDataDumper = PinDataDumper()
        self.lattice_data_dumper: LatticeDataDumper = LatticeDataDumper()

    def add_item(self, item_type):
        print(item_type)
        universe_element, element_type = item_type
        print(universe_element)
        match universe_element:
            case 'Universe':
                self.add_universe()
            case 'Cell':
                self.add_cell()
            case 'Pin':
                self.add_pin()
            case 'Lattice':
                self.add_lattice(element_type)

    def add_universe(self):
        item: Universe = Universe(self.elements_amount)
        self.present_item = item
        self.data.insert_node('root', str(item), item)
        item_text = ('Universe', str(self.elements_amount))
        self.elements_amount += 1
        self.view_model.add_item_to_views('root', item_text, str(item))

    def find_elements_of_type(self, element_type):
        elements = []
        for item_key in self.data.get():
            item_value = self.data.get_node_value(item_key)
            if type(item_value) is element_type:
                elements.append(item_value)

        return elements

    def insert_universe_element_to_data(self, item: Cell | Pin | Lattice):
        self.data.insert_node(self.key_of_selected_item, str(item), item)
        self.data.get_node_value(self.key_of_selected_item).add_element(item)
        item_text = (item.get_type(), item.get_name())
        self.view_model.add_item_to_views(self.key_of_selected_item, item_text, str(item))

    def add_cell(self):
        if type(self.data.get_node_value(self.key_of_selected_item)) != Universe:
            return

        item: Cell = Cell()
        self.insert_universe_element_to_data(item)
        self.input_data_model.update_cells_data(self.dump_data())

    def add_pin(self):
        if type(self.data.get_node_value(self.key_of_selected_item)) != Universe:
            return

        item: Pin = Pin()
        self.insert_universe_element_to_data(item)
        self.input_data_model.update_pins_data(self.dump_data())

    def add_lattice(self, lattice):
        if type(self.data.get_node_value(self.key_of_selected_item)) != Universe:
            return

        item: Lattice = create_lattice(lattice)
        self.insert_universe_element_to_data(item)
        self.input_data_model.update_lattices_data(self.dump_data())

    def select_item(self, key):
        self.key_of_selected_item = key
        selected_item = self.data.get_node_value(self.key_of_selected_item)
        if type(selected_item) is Cell:
            selected_item.all_elements = self.surfaces_model.data
            selected_item.all_materials = self.materials_model.data
            selected_item.all_universes = self.find_elements_of_type(Universe)
        if type(selected_item) is Pin:
            selected_item.all_materials = self.materials_model.data
        if type(selected_item) is LatticeSquare:
            selected_item.all_universes = self.find_elements_of_type(Universe)
        self.view_model.select_item_in_views(self.data.get_node(key)[0])

    def delete_item(self):
        self.data.delete_node(self.key_of_selected_item)
        self.view_model.delete_item_in_views(self.key_of_selected_item)
        self.key_of_selected_item = ''

    def change_data(self, value):
        item = self.data.get_node_value(self.key_of_selected_item)
        item.set_data(value)
        name, item_value = value
        if name == 'Name':
            self.view_model.change_item_in_views(item_value)
        if type(item) is Cell:
            self.input_data_model.update_cells_data(self.dump_data())
        if type(item) is Pin:
            self.input_data_model.update_pins_data(self.dump_data())
        if type(item) is LatticeSquare:
            self.input_data_model.update_lattices_data(self.dump_data())

    def clear_data(self):
        self.data.clear()
        self.elements_amount = 0
        self.view_model.clear_views()

    def dump_data(self):
        universes_data = []

        for item in self.data.get_values_from_nodes():
            if type(item) is Universe:
                universes_data.append(self.universe_data_dumper.dump(item))
            if type(item) is Cell:
                universes_data.append(self.cell_data_dumper.dump(item))
            if type(item) is Pin:
                universes_data.append(self.pin_data_dumper.dump(item))
            if type(item) is LatticeSquare:
                universes_data.append(self.lattice_data_dumper.dump(item))

        return universes_data

    def load_data(self):
        pass

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item
