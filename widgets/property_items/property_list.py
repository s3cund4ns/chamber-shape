from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QTableWidget, QListWidget, QMenu, \
    QListWidgetItem

from widgets.property_items.property_item import PropertyItem


class PropertyList(PropertyItem):
    def __init__(self):
        super().__init__()
        self.vertical_layout = QVBoxLayout(self)
        self.label_name = QLabel(self)
        self.horizontal_layout = QHBoxLayout(self)
        self.list_box = QListWidget(self)
        self.horizontal_layout.addWidget(self.list_box)
        self.vertical_layout.addWidget(self.label_name)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.list_box.itemChanged.connect(self.change_item)
        self.list_box.setContextMenuPolicy(Qt.CustomContextMenu)
        self.list_box.customContextMenuRequested.connect(self.show_context_menu)

    def set_data(self, data: list):
        name, *values = data
        self.label_name.setText(name)
        for value in values:
            index = self.list_box.count()
            item = QListWidgetItem(self.list_to_str(value, ' '))
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.list_box.insertItem(index, item)

    def show_context_menu(self, pos):
        context_menu = QMenu(self.list_box)
        add = context_menu.addAction('Add')
        delete = context_menu.addAction('Delete')
        add.triggered.connect(self.add_item)
        delete.triggered.connect(self.delete_item)
        context_menu.exec_(self.list_box.mapToGlobal(pos))

    def add_item(self):
        index = self.list_box.count()
        name = 'NewNuclide'
        value = 0.0
        item = QListWidgetItem(self.list_to_str([name, value], ' '))
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.list_box.insertItem(index, item)
        sender = self.sender().text()
        self.properties_view.apply_values_changes((sender, [index, name, value]))

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
