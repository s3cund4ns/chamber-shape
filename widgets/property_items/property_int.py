from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QSpinBox, QAbstractSpinBox

from widgets.property_items.property_item import PropertyItem


class PropertyInt(PropertyItem):
    def __init__(self):
        super().__init__()
        self.vertical_layout = QVBoxLayout(self)
        self.horizontal_layout = QHBoxLayout(self)
        self.label_name = QLabel(self)
        self.horizontal_layout.addWidget(self.label_name)
        self.spin_box_value = QSpinBox(self)
        self.spin_box_value.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.horizontal_layout.addWidget(self.spin_box_value)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.spin_box_value.valueChanged.connect(self.get_values_changes)

    def set_data(self, data):
        name, value = data
        self.label_name.setText(name)
        self.spin_box_value.setValue(value)

    def set_default_values(self, *args):
        pass

    def get_values_changes(self):
        sender = self.sender()
        self.properties_view.apply_values_changes((self.label_name.text(), sender.value()))
