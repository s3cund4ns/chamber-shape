from PySide6.QtWidgets import QMainWindow, QDoubleSpinBox, QLabel, QListWidgetItem, QComboBox

from surfaces.create_surface import create_surface
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

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.file_menu = self.ui.menubar.addMenu('File')
        # self.file_menu.addAction(self.ui.action_new_project)
        # self.file_menu.addAction(self.ui.action_open)
        # self.file_menu.addAction(self.ui.action_save)

        self.ui.button_add_surface.clicked.connect(self.add_item)
        self.ui.list_surfaces.itemClicked.connect(self.select_item)
        self.ui.button_delete_surface.clicked.connect(self.delete_item)
        # self.ui.action_save.triggered.connect(self.save_file)

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

    def insert_item_to_list_box(self, row, surface):
        item = [surface.get_type(), surface.get_values()]
        item = self.list_to_str(item, ' ')
        item = QListWidgetItem(item)
        self.ui.list_surfaces.insertItem(row, item)

    def delete_item(self):
        item = self.ui.list_surfaces.takeItem(self.selected_row)
        del item
        del self.surface_classes[self.selected_row]
        self.clear_properties()

    def clear_properties(self):
        while self.ui.properties_layout.count() > 0:
            current_property = self.ui.properties_layout.takeAt(0)
            current_property.widget().deleteLater()
            del self.property_classes[0]

    def select_item(self, item):
        if len(self.property_classes) > 0:
            property_position = self.property_classes[1].get_items_values()
            property_rotation = self.property_classes[2].get_items_values()
            property_parameters = self.property_classes[3].get_items_values()
            self.surface_classes[self.selected_row].set_properties(property_position, property_rotation,
                                                                   property_parameters)

            self.clear_properties()

            if self.ui.list_surfaces.item(self.selected_row) is not None:
                self.ui.list_surfaces.item(self.selected_row).setText(self.list_to_str(
                    [self.surface_classes[self.selected_row].get_type(),
                     self.surface_classes[self.selected_row].get_values()], ' '))

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

    def change_item_type(self):
        surface_type = self.property_classes[0].get_value()
        self.delete_item()
        surface = create_surface(surface_type)
        self.surface_classes.insert(self.selected_row, surface)
        self.insert_item_to_list_box(self.selected_row, surface)

    def save_file(self):
        surfaces = ['Surfaces']
        for surface_class in self.surface_classes:
            surfaces.append(surface_class.get_properties())
        with open('Projects/Project.json', 'w') as file:
            json.dump(surfaces, file, indent=4)

