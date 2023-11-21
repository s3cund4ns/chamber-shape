from typing import Sequence

from PySide6.QtWidgets import QWidget, QLabel
from ui_files.ui_property import UiForm

from widgets.property_item_widget import PropertyItemWidget
from widgets.property_type_item_widget import PropertyTypeItemWidget


class PropertyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = UiForm()
        self.ui.setupUi(self)

        self.item_classes: list = []

    def set_name(self, title: str):
        self.ui.gb_property.setTitle(title)

    def add_type_item(self, values: Sequence):
        property_type_item = PropertyTypeItemWidget()
        property_type_item.append_values(values)
        self.item_classes.append(property_type_item)
        self.ui.property_items_layout.addWidget(property_type_item)

    def add_items(self, names: list):
        for name in names:
            property_item = PropertyItemWidget()
            property_item.set_name(name)
            self.item_classes.append(property_item)
            self.ui.property_items_layout.addWidget(property_item)

    def set_items_values(self, values: list):
        for item in self.item_classes:
            item_index = self.item_classes.index(item)
            item.set_value(values[item_index])

    def get_items_values(self) -> list:
        values = []
        for item in self.item_classes:
            values.append(item.get_value())
        return values


