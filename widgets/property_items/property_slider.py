from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QSlider, QDoubleSpinBox

from widgets.property_items.property_item import PropertyItem


class PropertySlider(PropertyItem):
    def __init__(self):
        super().__init__()
        self.vertical_layout = QVBoxLayout()
        self.horizontal_layout = QHBoxLayout()
        self.label_name = QLabel(self)
        self.horizontal_layout.addWidget(self.label_name)
        self.slider_value = QSlider(Qt.Horizontal, self)
        self.horizontal_layout.addWidget(self.slider_value)
        self.double_spin_box_value = QDoubleSpinBox(self)
        self.double_spin_box_value.setReadOnly(True)
        self.horizontal_layout.addWidget(self.double_spin_box_value)
        self.vertical_layout.addLayout(self.horizontal_layout)

    def set_data(self, data):
        name, values_range, value = data
        min_value, max_value = values_range
        self.label_name.setText(name)
        self.slider_value.setRange(min_value, max_value)
        self.slider_value.setValue(value)
