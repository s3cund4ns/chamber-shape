from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit

from widgets.property_items.property_item import PropertyItem


class PropertyInfo(PropertyItem):
    def __init__(self):
        super(PropertyInfo, self).__init__()
        self.vertical_layout = QVBoxLayout(self)
        self.horizontal_layout = QHBoxLayout(self)
        self.label_name = QLabel(self)
        self.horizontal_layout.addWidget(self.label_name)
        self.vertical_layout.addLayout(self.horizontal_layout)

    def set_data(self, data):
        name, values = data
        self.label_name.setText(name)
        for value in values:
            self.line_edit_info = QLineEdit(self)
            self.line_edit_info.setReadOnly(True)
            self.line_edit_info.setText(str(value))
            self.horizontal_layout.addWidget(self.line_edit_info)