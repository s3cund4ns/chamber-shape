from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QDoubleSpinBox, QAbstractSpinBox

from widgets.property_items.property_item import PropertyItem


class PropertyFloat(PropertyItem):
    def __init__(self):
        super().__init__()
        self.vertical_layout = QVBoxLayout(self)
        self.horizontal_layout = QHBoxLayout(self)
        self.label_name = QLabel(self)
        self.horizontal_layout.addWidget(self.label_name)
        self.double_spin_box_value = QDoubleSpinBox(self)
        self.double_spin_box_value.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.horizontal_layout.addWidget(self.double_spin_box_value)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.double_spin_box_value.valueChanged.connect(self.get_values_changes)

    def set_data(self, data):
        name, value, values_range = data
        min_value, max_value = values_range
        self.label_name.setText(name)
        self.double_spin_box_value.setMinimum(min_value)
        self.double_spin_box_value.setMaximum(max_value)
        self.double_spin_box_value.setValue(value)

    def set_default_values(self, *args):
        pass

    def get_values_changes(self):
        sender = self.sender()
        self.properties_view.apply_values_changes((self.label_name.text(), sender.value()))
