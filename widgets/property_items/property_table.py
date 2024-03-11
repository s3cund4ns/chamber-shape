from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QTableWidget, QListWidget, QMenu, \
    QListWidgetItem

from widgets.property_items.property_item import PropertyItem


class PropertyTable(PropertyItem):
    def __init__(self):
        super().__init__()
        self.vertical_layout = QVBoxLayout(self)
        self.label_name = QLabel(self)
        self.horizontal_layout = QHBoxLayout(self)
        self.table = QTableWidget(self)
        self.horizontal_layout.addWidget(self.table)
        self.vertical_layout.addWidget(self.label_name)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.table.itemChanged.connect(self.change_item)
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.show_context_menu)

    def set_data(self, data: list):
        name, *values = data
        self.label_name.setText(name)
        self.table.setRowCount(len(values))
        for value in values:
            *value_components, = value
            for i in range(value_components):
                value_component = value_components[i]
                self.table.setItem(values.index(value), i, value_component)

    def set_default_values(self, *args):
        values, = args
        self.table.setColumnCount(len(values))
        self.table.setHorizontalHeaderLabels(values)

    def show_context_menu(self, pos):
        context_menu = QMenu(self.table)
        add = context_menu.addAction('Add')
        delete = context_menu.addAction('Delete')
        add.triggered.connect(self.add_item)
        delete.triggered.connect(self.delete_item)
        context_menu.exec_(self.table.mapToGlobal(pos))

    def add_item(self):
        item = QListWidgetItem(self.list_to_str([name, value], ' '))
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.list_box.insertItem(index, item)
        # sender = self.sender().text()
        # self.properties_view.apply_values_changes((sender, [index, name, value]))

    def change_item(self):
        sender_index: int = self.sender().currentRow()
        sender_text: str = self.sender().currentItem().text()
        changed_item = sender_text.split()
        name, value = changed_item
        value = float(value)
        self.properties_view.apply_values_changes((self.label_name.text(), [sender_index, name, value]))

    def delete_item(self):
        index = self.list_box.currentRow()
        self.list_box.takeItem(index)
        sender = self.sender().text()
        self.properties_view.apply_values_changes((sender, index))

    @staticmethod
    def list_to_str(list_item: list, delimiter: str) -> str:
        str_item = delimiter.join(map(str, list_item))
        return str_item
