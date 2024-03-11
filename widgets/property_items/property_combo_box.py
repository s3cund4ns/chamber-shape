from dataclasses import asdict

from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QComboBox

from widgets.property_items.property_item import PropertyItem


class PropertyComboBox(PropertyItem):
    def __init__(self):
        super().__init__()
        self.vertical_layout = QVBoxLayout(self)
        self.horizontal_layout = QHBoxLayout(self)
        self.label_name = QLabel(self)
        self.horizontal_layout.addWidget(self.label_name)
        self.combo_box_value = QComboBox(self)
        self.horizontal_layout.addWidget(self.combo_box_value)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.combo_box_value.currentTextChanged.connect(self.get_values_changes)

    def set_data(self, data):
        name, values, current_value = data
        self.label_name.setText(name)
        for key in values:
            value = values[key]
            self.combo_box_value.insertItem(self.combo_box_value.count(), value)

        self.combo_box_value.setCurrentText(current_value)

    def set_default_values(self, *args):
        pass

    def get_values_changes(self):
        sender = self.sender().currentText()
        self.properties_view.apply_values_changes((self.label_name.text(), sender))
