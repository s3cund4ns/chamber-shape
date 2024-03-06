from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit

from widgets.property_items.property_item import PropertyItem


class PropertyLabel(PropertyItem):
    def __init__(self):
        super().__init__()
        self.vertical_layout = QVBoxLayout(self)
        self.horizontal_layout = QHBoxLayout(self)
        self.label_name = QLabel(self)
        self.horizontal_layout.addWidget(self.label_name)
        self.label_value = QLabel(self)
        self.horizontal_layout.addWidget(self.label_value)
        self.vertical_layout.addLayout(self.horizontal_layout)

    def set_data(self, data):
        self.label_name.setText('Object: ')
        self.label_value.setText(data)
