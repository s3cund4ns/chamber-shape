from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit

from widgets.property_items.property_item import PropertyItem


class PropertyString(PropertyItem):
    def __init__(self):
        super().__init__()
        self.vertical_layout = QVBoxLayout(self)
        self.horizontal_layout = QHBoxLayout(self)
        self.label_name = QLabel(self)
        self.horizontal_layout.addWidget(self.label_name)
        self.line_edit_value = QLineEdit(self)
        self.horizontal_layout.addWidget(self.line_edit_value)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.line_edit_value.textChanged.connect(self.get_values_changes)

    def set_data(self, data: list):
        name, value = data
        self.label_name.setText(name)
        self.line_edit_value.setText(value)

    def get_values_changes(self):
        sender = self.sender()
        self.properties_view.apply_values_changes((self.label_name.text(), sender.text()))
