from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QMainWindow, QDoubleSpinBox, QLabel, QListWidgetItem, QComboBox, QMenu, QTreeWidgetItem, \
    QButtonGroup, QRadioButton, QLineEdit, QListWidget, QPushButton, QCheckBox

from preprocessor.cell import Cell, CellProperties, SpecialEntires
from preprocessor.input_data_writer import InputDataWriter
from preprocessor.lattice_square import LatticeSquare
from preprocessor.material import Material
from preprocessor.pin import Pin
from preprocessor.universe import Universe, UniverseProperties
from renderer.scene import vertices, scene
from surfaces.create_surface import create_surface
from widgets.property_item_widget import PropertyItemWidget
from widgets.property_type_item_widget import PropertyTypeItemWidget
from ui_files.ui_main import Ui_MainWindow
from widgets.property_widget import PropertyWidget
from surfaces.surface import SurfacesTypes, SurfacesProperties
from surfaces.plane import Plane

import json


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.surface_classes = []
        self.property_classes = []
        self.selected_row = None

        self.universe_classes = []
        self.universe_property_classes = []

        self.cell_classes = []
        self.cell_property_classes = []

        self.pin_classes = []
        self.pin_property_classes = []

        self.material_classes = []
        self.material_property_classes = []

        self.lattice_classes = []

        self.input_data_writer = InputDataWriter()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.file_menu = self.ui.menubar.addMenu('File')
        # self.file_menu.addAction(self.ui.action_new_project)
        # self.file_menu.addAction(self.ui.action_open)
        # self.file_menu.addAction(self.ui.action_save)

        self.ui.button_add_surface.clicked.connect(self.add_item)
        self.ui.list_surfaces.itemClicked.connect(self.select_item)
        self.ui.list_surfaces.installEventFilter(self)
        self.ui.button_delete_surface.clicked.connect(self.delete_item)
        # self.ui.action_save.triggered.connect(self.save_file)

        self.ui.tree_universes.setColumnCount(2)
        self.ui.tree_universes.setHeaderLabels(['Element', 'Name'])
        self.ui.button_add_universe.clicked.connect(self.add_universe)
        self.ui.tree_universes.itemClicked.connect(self.select_universe)

        self.context_menu_universe_elements = QMenu(self)
        action_add_cell = self.context_menu_universe_elements.addAction('Cell')
        action_add_cell.triggered.connect(self.add_cell)
        action_add_pin = self.context_menu_universe_elements.addAction('Pin')
        action_add_pin.triggered.connect(self.add_pin)
        action_add_lattice = self.context_menu_universe_elements.addAction('Square Lattice')
        action_add_lattice.triggered.connect(self.add_lattice)

        self.context_menu_cell_elements = QMenu(self)

        self.ui.button_add_material.clicked.connect(self.add_material)
        self.ui.list_materials.itemClicked.connect(self.select_material)

        self.context_menu_pin_elements = QMenu(self)

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item

    @staticmethod
    def str_to_list(str_item: str, delimiter: str) -> list:
        list_item = str_item.split(delimiter)
        for i in range(0, len(list_item)):
            if i != 0:
                list_item[i] = float(list_item[i])

        return list_item

    def add_item(self):
        surface = create_surface(SurfacesTypes.Default)
        self.surface_classes.append(surface)
        count = self.ui.list_surfaces.count()
        self.insert_item_to_list_box(count, surface)
        self.ui.view.add_surface_entity(SurfacesTypes.Plane, count)
        self.input_data_writer.update_surface_data(self.surface_classes)
        self.input_data_writer.write_to_file()

    def insert_item_to_list_box(self, row, surface):
        item = [surface.get_type()]
        item = self.list_to_str(item, ' ')
        item = QListWidgetItem(item)
        self.ui.list_surfaces.insertItem(row, item)

    def delete_item(self):
        item = self.ui.list_surfaces.takeItem(self.selected_row)
        del item
        del self.surface_classes[self.selected_row]
        self.clear_properties()
        self.ui.view.delete_surface_entity(self.selected_row)

    def clear_properties(self):
        while self.ui.properties_layout.count() > 0:
            current_property = self.ui.properties_layout.takeAt(0)
            current_property.widget().deleteLater()
            if len(self.property_classes) > 0:
                del self.property_classes[0]
            elif len(self.universe_property_classes) > 0:
                del self.universe_property_classes[0]
            elif len(self.cell_property_classes) > 0:
                del self.cell_property_classes[0]
            elif len(self.material_property_classes) > 0:
                del self.material_property_classes[0]
            elif len(self.pin_property_classes) > 0:
                del self.pin_property_classes[0]

    def select_item(self, item):
        if len(self.universe_property_classes) > 0:
            self.clear_properties()
        if len(self.cell_property_classes) > 0:
            self.clear_properties()

        if len(self.property_classes) > 0:
            property_position = self.property_classes[1].get_items_values()
            property_color = self.property_classes[2].get_items_values()
            print(property_color)
            property_parameters = self.property_classes[3].get_items_values()

            self.surface_classes[self.selected_row].set_position(property_position)
            self.surface_classes[self.selected_row].set_color(property_color)
            self.surface_classes[self.selected_row].set_parameters(property_parameters)

            self.clear_properties()

            self.ui.view.set_surface_transform(self.selected_row, property_position[0], property_position[1],
                                               property_position[2])

            self.ui.view.set_surface_mesh(self.selected_row, self.surface_classes[self.selected_row].get_type(),
                                          property_parameters)

            self.ui.view.deselect_surface_entity(self.selected_row)

            self.ui.view.set_surface_color(self.selected_row, property_color[0], property_color[1],
                                           property_color[2], property_color[3])

            # if self.ui.list_surfaces.item(self.selected_row) is not None:
            #     self.ui.list_surfaces.item(self.selected_row).setText(self.list_to_str(
            #         [self.surface_classes[self.selected_row].get_type(),
            #          self.surface_classes[self.selected_row].get_values()], ' '))

        self.context_menu_cell_elements.clear()

        self.selected_row = int(self.ui.list_surfaces.selectedIndexes()[0].row())

        surface_types = SurfacesTypes.get(SurfacesTypes)
        property_type_item_widget = PropertyTypeItemWidget()
        property_type_item_widget.set_name('Type')
        property_type_item_widget.append_values(surface_types)
        property_type_item_widget.set_value(self.surface_classes[self.selected_row].get_type())
        self.property_classes.append(property_type_item_widget)
        self.ui.properties_layout.addWidget(property_type_item_widget)
        property_type_item_widget.on_value_changed(self.change_item_type)

        surface_properties = SurfacesProperties.get(SurfacesProperties)
        for surface_property in surface_properties:
            property_widget = PropertyWidget()
            property_widget.set_name(surface_property)
            index = surface_properties.index(surface_property)
            items_names = self.surface_classes[self.selected_row].get_names()[index]
            property_widget.add_items(items_names)
            items_values = self.surface_classes[self.selected_row].get_values()[index]
            property_widget.set_items_values(items_values)
            self.property_classes.append(property_widget)
            self.ui.properties_layout.addWidget(property_widget)

        for cell in self.cell_classes:
            cell_name = cell.get_name()
            action = self.context_menu_cell_elements.addAction(cell_name)
            action.triggered.connect(self.add_surface_to_cell)
        self.context_menu_cell_elements.exec_(QCursor.pos())
        self.ui.view.select_surface_entity(self.selected_row)

    def change_item_type(self):
        surface_type = self.property_classes[0].get_value()
        self.delete_item()
        surface = create_surface(surface_type)
        self.surface_classes.insert(self.selected_row, surface)
        self.insert_item_to_list_box(self.selected_row, surface)
        self.ui.view.add_surface_entity(surface_type, self.selected_row)

    def add_universe(self):
        universe = Universe('Universe', len(self.universe_classes), self.ui.tree_universes)
        self.universe_classes.append(universe)
        self.ui.view.add_universe_entity()

    def select_universe(self):
        if len(self.property_classes) > 0:
            self.clear_properties()
        if len(self.universe_property_classes) > 0:
            self.clear_properties()
        if len(self.cell_property_classes) > 0:
            self.clear_properties()
        if len(self.pin_property_classes) > 0:
            self.clear_properties()

        if self.ui.tree_universes.currentItem().text(0) == 'Universe':
            self.select_universe_item()
        elif self.ui.tree_universes.currentItem().text(0) == 'Cell':
            self.select_cell()
        elif self.ui.tree_universes.currentItem().text(0) == 'Pin':
            self.select_pin()
        elif self.ui.tree_universes.currentItem().text(0) == 'Lattice':
            self.select_lattice()

    def select_universe_item(self):
        if len(self.property_classes) > 0:
            self.clear_properties()
        if len(self.universe_property_classes) > 0:
            self.clear_properties()
        if len(self.cell_property_classes) > 0:
            self.clear_properties()

        self.selected_row = self.ui.tree_universes.indexOfTopLevelItem(self.ui.tree_universes.currentItem())
        universe_properties = UniverseProperties.get(UniverseProperties)
        universe_position = universe_properties[0]
        property_widget = PropertyWidget()
        property_widget.set_name(universe_position)
        items_names = self.universe_classes[self.selected_row].get_names()
        property_widget.add_items(items_names)
        # items_values = self.universe_classes[self.selected_row].get_values()
        # property_widget.set_items_values(items_values)
        self.ui.properties_layout.addWidget(property_widget)
        self.universe_property_classes.append(property_widget)

        universe_elements: list[Cell | Pin] = self.universe_classes[self.selected_row].get_values()[1]
        for universe_element in universe_elements:
            element_info = QLabel()
            element_info.setText(f'{universe_element.get_type()} {universe_element.get_name()}')
            self.ui.properties_layout.addWidget(element_info)
            self.universe_property_classes.append(element_info)

        self.context_menu_universe_elements.exec_(QCursor.pos())

    def select_cell(self):
        self.selected_row = self.ui.tree_universes.currentIndex().row()

        special_entires = SpecialEntires.get(SpecialEntires)
        materials = []
        for material in range(self.ui.list_materials.count()):
            materials.append(f'Material {self.ui.list_materials.item(material).text()}')
        universes = []
        for universe in range(self.ui.tree_universes.topLevelItemCount()):
            universes.append(f'Universe {universe}')

        line_edit_name = QLineEdit()
        line_edit_name.setText(self.cell_classes[self.selected_row].get_name())
        line_edit_name.textChanged.connect(self.change_cell_name)
        self.ui.properties_layout.addWidget(line_edit_name)
        self.cell_property_classes.append(line_edit_name)
        property_type_item_widget = PropertyTypeItemWidget()
        property_type_item_widget.set_name('Fill')
        property_type_item_widget.append_values(special_entires)
        property_type_item_widget.append_values(materials)
        property_type_item_widget.append_values(universes)
        fill = self.cell_classes[self.selected_row].get_fill_name()
        property_type_item_widget.set_value(str(fill))
        self.ui.properties_layout.addWidget(property_type_item_widget)
        self.cell_property_classes.append(property_type_item_widget)
        property_type_item_widget.on_value_changed(self.change_fill_cell)

        surfaces = self.cell_classes[self.selected_row].get_surfaces()
        for surface in surfaces:
            surface_info = QLabel()
            surface_info.setText(f'{surface[0].get_type()} {surface[0].get_values()[0]}')
            self.ui.properties_layout.addWidget(surface_info)
            self.cell_property_classes.append(surface_info)
            check_box_is_in = QCheckBox()
            check_box_is_in.setText('Is in')
            if surface[1] == -1:
                check_box_is_in.setChecked(True)
            else:
                check_box_is_in.setChecked(False)

            check_box_is_in.toggled.connect(self.set_surface_side_in_cell)
            self.ui.properties_layout.addWidget(check_box_is_in)
            self.cell_property_classes.append(check_box_is_in)

    def set_surface_side_in_cell(self):
        sender = self.sender().checkState()
        sender_id = self.cell_property_classes[3:].index(self.sender()) // 2
        side = None
        if sender == Qt.CheckState.Checked:
            side = -1
        elif sender == Qt.CheckState.Unchecked:
            side = 1
        self.cell_classes[self.selected_row].set_surface_side(sender_id, side)

    def select_pin(self):
        self.selected_row = self.ui.tree_universes.currentIndex().row()
        line_edit_name = QLineEdit()
        line_edit_name.setText(self.pin_classes[self.selected_row].get_name())
        line_edit_name.textChanged.connect(self.change_pin_name)
        self.pin_property_classes.append(line_edit_name)
        self.ui.properties_layout.addWidget(line_edit_name)

        list_material_regions = QListWidget()
        self.pin_property_classes.append(list_material_regions)
        for region in self.pin_classes[self.selected_row].get_regions():
            material_name = region[0].get_name()
            radius = region[1]
            item = f'{material_name} {str(radius)}'
            item = QListWidgetItem(item)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.pin_property_classes[1].insertItem(self.pin_classes[self.selected_row].get_regions().index(region),
                                                    item)
        self.ui.properties_layout.addWidget(list_material_regions)
        list_material_regions.itemChanged.connect(self.change_region_in_pin)

    def change_region_in_pin(self):
        sender: QListWidget = self.sender()
        item: QListWidgetItem = sender.currentItem()
        item_text = item.text()
        item_index = sender.currentIndex().row()
        delimiter_index = item_text.find(' ')
        changed_radius = item_text[delimiter_index + 1:]
        self.pin_classes[self.selected_row].set_region(item_index, float(changed_radius))

    def add_cell(self):
        universe_id = self.ui.tree_universes.indexOfTopLevelItem(self.ui.tree_universes.currentItem())
        print(universe_id)
        cell = Cell('New Cell', 'void', self.ui.tree_universes.currentItem())
        cell.set_universe_number(universe_id)
        self.universe_classes[universe_id].add_element(cell)
        self.cell_classes.append(cell)
        self.ui.view.add_cell_entity(universe_id)
        self.input_data_writer.update_cell_data(self.cell_classes, self.surface_classes)
        self.input_data_writer.write_to_file()

    def add_surface_to_cell(self):
        sender_action = self.sender()
        cell_id = self.context_menu_cell_elements.actions().index(sender_action)
        surface = self.surface_classes[self.selected_row]
        self.cell_classes[cell_id].add_surface(surface)
        self.ui.view.add_surface_entity_to_cell(self.selected_row, cell_id)

    def change_fill_cell(self):
        sender = self.sender()
        if sender.currentText()[0:8] == 'Material':
            material_id = sender.currentIndex() - 2
            material = self.material_classes[material_id]
            self.cell_classes[self.selected_row].set_fill(material)
        if sender.currentText()[0:8] == 'Universe':
            universe_id = sender.currentIndex() - (2 + len(self.material_classes))
            universe = self.ui.tree_universes.topLevelItem(universe_id)
            self.ui.tree_universes.currentItem().addChild(universe)
            self.cell_classes[self.selected_row].set_fill(universe_id)

        self.cell_classes[self.selected_row].set_fill(sender.currentText())

    def change_cell_name(self):
        sender = self.sender()
        self.cell_classes[self.selected_row].set_name(sender.text())
        self.ui.tree_universes.currentItem().setText(1, sender.text())

    def add_pin(self):
        universe_id = self.ui.tree_universes.indexOfTopLevelItem(self.ui.tree_universes.currentItem())
        pin = Pin('New Pin', self.ui.tree_universes.currentItem())
        pin.set_universe(universe_id)
        self.universe_classes[universe_id].add_element(pin)
        self.pin_classes.append(pin)
        self.input_data_writer.update_pin_data(self.pin_classes)
        self.input_data_writer.write_to_file()

    def change_pin_name(self):
        sender = self.sender()
        self.pin_classes[self.selected_row].set_name(sender.text())
        self.ui.tree_universes.currentItem().setText(1, sender.text())

    def add_region_to_pin(self):
        sender_action = self.sender()
        pin_id = self.context_menu_pin_elements.actions().index(sender_action)
        region = self.material_classes[self.selected_row]
        for material in self.pin_classes[pin_id].get_regions():
            if region is material[0]:
                print('Pin already contains this material!')
                return
        self.pin_classes[pin_id].add_region(region)

    def add_lattice(self):
        universe_id = self.ui.tree_universes.indexOfTopLevelItem(self.ui.tree_universes.currentItem())
        sender = self.sender().text()
        if sender == 'Square Lattice':
            lattice = LatticeSquare([0.0, 0.0, 0.0], 5, 5, 5.0, self.ui.tree_universes.currentItem())
            lattice.set_universe_number(universe_id)
            self.lattice_classes.append(lattice)

    def select_lattice(self):
        pass

    def add_material(self):
        material = Material('New material', 0.0)
        self.material_classes.append(material)
        item = f'{material.get_name()} {str(material.get_density())}'
        item = QListWidgetItem(item)
        count = self.ui.list_materials.count()
        self.ui.list_materials.insertItem(count, item)
        self.input_data_writer.update_material_data(self.material_classes)
        self.input_data_writer.write_to_file()

    def select_material(self):
        if len(self.material_property_classes) > 0:
            self.clear_properties()

        self.context_menu_pin_elements.clear()
        self.selected_row = int(self.ui.list_materials.selectedIndexes()[0].row())
        line_edit_name = QLineEdit()
        line_edit_name.setText(self.material_classes[self.selected_row].get_name())
        self.ui.properties_layout.addWidget(line_edit_name)
        self.material_property_classes.append(line_edit_name)
        line_edit_name.textChanged.connect(self.change_material_name)

        property_widget = PropertyItemWidget()
        property_widget.set_name('Density')
        property_widget.set_value(self.material_classes[self.selected_row].get_density())
        self.material_property_classes.append(property_widget)
        self.ui.properties_layout.addWidget(property_widget)
        property_widget.ui.dsb_property_item_value.valueChanged.connect(self.change_material_density)

        list_nuclides = QListWidget()
        self.material_property_classes.append(list_nuclides)
        for nuclide_id in range(self.material_classes[self.selected_row].get_nuclides_count()):
            item = f'{nuclide_id} {str(self.material_classes[self.selected_row].get_nuclide(nuclide_id))}'
            item = QListWidgetItem(item)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.material_property_classes[2].insertItem(nuclide_id, item)
        self.ui.properties_layout.addWidget(list_nuclides)
        list_nuclides.itemChanged.connect(self.change_nuclide_in_material)

        button_add_nuclide = QPushButton()
        button_add_nuclide.setText('Add nuclide')
        self.material_property_classes.append(button_add_nuclide)
        self.ui.properties_layout.addWidget(button_add_nuclide)
        button_add_nuclide.clicked.connect(self.add_nuclide_to_material)

        for pin in self.pin_classes:
            pin_name = pin.get_name()
            action = self.context_menu_pin_elements.addAction(pin_name)
            action.triggered.connect(self.add_region_to_pin)
        self.context_menu_pin_elements.exec_(QCursor.pos())

    def change_material_name(self):
        sender = self.sender()
        self.material_classes[self.selected_row].set_name(sender.text())
        self.ui.list_materials.currentItem().setText(f'{self.material_classes[self.selected_row].get_name()} '
                                                     f'{str(self.material_classes[self.selected_row].get_density())}')

    def change_material_density(self):
        sender = self.sender()
        self.material_classes[self.selected_row].set_density(sender.value())
        self.ui.list_materials.currentItem().setText(f'{self.material_classes[self.selected_row].get_name()} '
                                                     f'{str(self.material_classes[self.selected_row].get_density())}')

    def add_nuclide_to_material(self):
        self.material_classes[self.selected_row].add_nuclide(0.0)
        count = self.material_property_classes[2].count()
        item = f'{count} {str(self.material_classes[self.selected_row].get_nuclide(count))}'
        item = QListWidgetItem(item)
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.material_property_classes[2].insertItem(count, item)

    def change_nuclide_in_material(self):
        sender: QListWidget = self.sender()
        item: QListWidgetItem = sender.currentItem()
        item_text = item.text()
        item_index = sender.currentIndex().row()
        delimiter_index = item_text.find(' ')
        changed_fraction = item_text[delimiter_index + 1:]
        self.material_classes[self.selected_row].set_nuclide(item_index, float(changed_fraction))

    def save_file(self):
        surfaces = ['Surfaces']
        for surface_class in self.surface_classes:
            surfaces.append(surface_class.get_properties())
        with open('Projects/Project.json', 'w') as file:
            json.dump(surfaces, file, indent=4)
