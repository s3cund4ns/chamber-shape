from typing import Sequence

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
from ui_files.ui_property_type_item import UiForm


class PropertyTypeItemWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = UiForm()
        self.ui.setupUi(self)

    def set_name(self, name: str):
        self.ui.label_property_item_name.setText(name)

    def append_values(self, values: Sequence[str]):
        self.ui.cb_property_item_value.addItems(values)

    def set_value(self, value: str):
        self.ui.cb_property_item_value.setCurrentText(value)

    def get_value(self):
        return self.ui.cb_property_item_value.currentText()

    def on_value_changed(self, slot):
        self.ui.cb_property_item_value.currentTextChanged.connect(slot)






