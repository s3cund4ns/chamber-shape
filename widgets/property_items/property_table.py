from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QTableWidget, QListWidget, QMenu, \
    QListWidgetItem, QTableWidgetItem, QComboBox

from widgets.property_items.property_item import PropertyItem


class PropertyTable(PropertyItem):
    def __init__(self):
        super().__init__()
        self.vertical_layout = QVBoxLayout(self)
        self.label_name = QLabel(self)
        self.horizontal_layout = QHBoxLayout(self)
        self.table = QTableWidget(self)
        # self.table.setDragEnabled(True)
        self.table.setAcceptDrops(True)
        self.horizontal_layout.addWidget(self.table)
        self.vertical_layout.addWidget(self.label_name)
        self.vertical_layout.addLayout(self.horizontal_layout)

        # self.table.itemChanged.connect(self.change_item)
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.show_context_menu)

        self.all_items_for_menu: list = []

        # self.table..connect(self.add_item)

    def set_data(self, data: list):
        name, *values = data
        self.label_name.setText(name)
        self.all_items_for_menu = values[1]
        self.table.setRowCount(len(values[0]))
        print(values[0])
        for row_index, value_row in enumerate(values[0]):
            for col_index, value_component in enumerate(value_row):
                print(row_index, col_index, value_row, value_component)
                item = QTableWidgetItem(value_component)
                self.table.setItem(row_index, col_index, QTableWidgetItem(value_component))

    def set_default_values(self, *args):
        values, = args
        self.table.setColumnCount(len(values))
        self.table.setHorizontalHeaderLabels(values)

    def show_context_menu(self, pos):
        context_menu = QMenu(self.table)
        add = context_menu.addMenu('Add')
        add.setObjectName('Add')
        for add_menu_item in self.all_items_for_menu:
            add.addAction(add_menu_item)

        delete = context_menu.addAction("Delete")
        delete.triggered.connect(self.delete_item)
        selected_action = context_menu.exec_(self.table.mapToGlobal(pos))
        if selected_action and (selected_action.text() != 'Delete'):
            selected_item_name = selected_action.parent().objectName()
            select_action_index = add.actions().index(selected_action)
            select_action_name = selected_action.text()
            self.add_item(select_action_name, select_action_index)

    def add_item(self, item_info_text: str, item_index: int):
        item_info_list: list = self.str_to_list(item_info_text, ' ')
        self.table.insertRow(self.table.rowCount())
        for info_element in item_info_list:
            info_element_index: int = item_info_list.index(info_element)
            table_item: QTableWidgetItem = QTableWidgetItem(info_element)
            self.table.setItem(self.table.rowCount()-1, info_element_index, table_item)

        combo_box = QComboBox(self.table)
        combo_box.addItem('In')
        combo_box.addItem('Out')
        self.table.setCellWidget(self.table.rowCount()-1, self.table.columnCount()-1, combo_box)

        self.all_items_for_menu.remove(item_info_text)

        self.properties_view.apply_values_changes(('Add', [item_index, combo_box.currentText()]))

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

    @staticmethod
    def str_to_list(str_item: str, delimiter: str) -> list:
        list_item = str_item.split(delimiter)
        return list_item
