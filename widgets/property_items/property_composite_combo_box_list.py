from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget, QMenu, QPushButton, QHBoxLayout, QLineEdit, QDoubleSpinBox, \
    QAbstractSpinBox, QComboBox

from widgets.property_items.property_item import PropertyItem


class PropertyCompositeComboBoxList(PropertyItem):
    def __init__(self):
        super().__init__()
        self.all_items_in_menu: list = []
        self.composite_items: list = []
        self.vertical_layout = QVBoxLayout(self)
        self.label_name = QLabel()
        self.composite_item_list = QWidget()
        self.composite_item_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.vertical_layout.addWidget(self.label_name)
        self.vertical_layout.addWidget(self.composite_item_list)
        self.context_menu = QMenu(self.composite_item_list)

    def set_default_values(self, *args):
        pass

    def set_data(self, data: list):
        name, *values = data
        self.label_name.setText(name)
        self.all_items_in_menu = values[1]

        composite_items = values[0]

        self.button_add_composite_item = QPushButton(self)
        self.button_add_composite_item.setText('Add')
        self.button_add_composite_item.setMenu(self.context_menu)
        self.add_items_to_menu()
        self.vertical_layout.addWidget(self.button_add_composite_item)

        for composite_item in composite_items:
            composite_item_widget = QWidget(self.composite_item_list)
            composite_item_layout = QHBoxLayout(composite_item_widget)

            combo_box: QComboBox = QComboBox(composite_item_widget)
            combo_box.addItems(self.all_items_in_menu)
            combo_box.setCurrentText(composite_item[0])
            combo_box.currentIndexChanged.connect(self.change_item)
            composite_item_layout.addWidget(combo_box)

            button_delete_composite_item = QPushButton(self)
            button_delete_composite_item.setText('  -  ')
            button_delete_composite_item.clicked.connect(self.delete_item)
            composite_item_layout.addWidget(button_delete_composite_item)

            self.vertical_layout.addWidget(composite_item_widget)

            self.composite_items.append(composite_item_widget)

    def add_item(self):
        composite_item = QWidget(self.composite_item_list)
        composite_item_layout = QHBoxLayout(composite_item)
        composite_item_info: str = self.sender().text()

        combo_box: QComboBox = QComboBox(composite_item)
        combo_box.addItems(self.all_items_in_menu)
        combo_box.setCurrentText(composite_item_info)
        combo_box.currentIndexChanged.connect(self.change_item)
        composite_item_layout.addWidget(combo_box)

        button_delete_composite_item = QPushButton(self)
        button_delete_composite_item.setText('  -  ')
        button_delete_composite_item.clicked.connect(self.delete_item)
        composite_item_layout.addWidget(button_delete_composite_item)

        self.vertical_layout.addWidget(composite_item)

        self.composite_items.append(composite_item)

        index = self.context_menu.actions().index(self.sender())
        self.properties_view.apply_values_changes(('Add', index))

    def change_item(self):
        sender_index = self.composite_items.index(self.sender().parent())
        if type(self.sender()) is QComboBox:
            self.properties_view.apply_values_changes(('Change', [sender_index, self.sender().currentIndex()]))

    def delete_item(self):
        sender = self.sender().parent()
        index = self.composite_items.index(sender)
        self.properties_view.apply_values_changes(('Delete', index))
        layout = sender.layout()
        while layout.count() > 0:
            element = layout.takeAt(0)
            element.widget().deleteLater()
        self.composite_items.remove(sender)

    def add_items_to_menu(self):
        for item_in_menu in self.all_items_in_menu:
            action = self.context_menu.addAction(item_in_menu)
            action.triggered.connect(self.add_item)
