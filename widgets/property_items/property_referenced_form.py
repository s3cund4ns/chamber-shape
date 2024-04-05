from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMenu

from widgets.property_items.property_item import PropertyItem


class PropertyReferencedForm(PropertyItem):
    def __init__(self):
        super().__init__()
        self.items_in_menu: list = []
        self.vertical_layout = QVBoxLayout(self)
        self.horizontal_layout = QHBoxLayout(self)
        self.label_name = QLabel(self)
        self.horizontal_layout.addWidget(self.label_name)
        self.line_edit_value = QLineEdit(self)
        self.line_edit_value.setReadOnly(True)
        self.horizontal_layout.addWidget(self.line_edit_value)
        self.vertical_layout.addLayout(self.horizontal_layout)
        self.context_menu = QMenu(self)

        self.button_add_reference = QPushButton(self)
        self.button_add_reference.setText('...')
        self.button_add_reference.setMenu(self.context_menu)
        self.vertical_layout.addWidget(self.button_add_reference)

    def set_default_values(self, *args):
        pass

    def set_data(self, data: list):
        name, *values = data
        print(values)
        value, items_in_menu = values
        self.label_name.setText(name)
        self.items_in_menu = items_in_menu
        print(items_in_menu)
        self.add_items_to_menu()
        self.line_edit_value.setText(value)

    def set_reference(self):
        self.properties_view.apply_values_changes(('Set', self.context_menu.actions().index(self.sender())))
        self.line_edit_value.setText(self.sender().text())

    def add_items_to_menu(self):
        for item_in_menu in self.items_in_menu:
            action = self.context_menu.addAction(item_in_menu)
            action.triggered.connect(self.set_reference)
