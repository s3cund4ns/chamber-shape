from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QPushButton, QMenu, QComboBox

from widgets.property_items.property_item import PropertyItem


class PropertyArray2DInt(PropertyItem):
    def __init__(self):
        super().__init__()

        self.current_element: QPushButton | None = None

        self.all_values: list = []
        self.vertical_layout = QVBoxLayout(self)
        self.label_name = QLabel(self)
        self.vertical_layout.addWidget(self.label_name)
        self.array_grid_layout = QGridLayout(self)
        self.vertical_layout.addLayout(self.array_grid_layout)
        self.context_menu = QMenu(self)

    def set_default_values(self, *args):
        pass

    def set_data(self, data):
        name, *values = data
        array, self.all_values = values
        self.label_name.setText(name)
        self.add_items_to_menu()
        for row in range(len(array)):
            for column in range(len(array[0])):
                element = QPushButton(self)
                element.setObjectName(f'{row}_{column}')
                element.setText(str(array[row][column]))
                element.pressed.connect(self.set_current_element)
                element.setMenu(self.context_menu)
                self.array_grid_layout.addWidget(element, row, column)

    def add_items_to_menu(self):
        for item in self.all_values:
            action = self.context_menu.addAction(item)
            action.triggered.connect(self.change_item)

    def set_current_element(self):
        sender: QPushButton = self.sender()
        self.current_element = sender

    def change_item(self):
        sender = self.sender().text()
        element_index = self.current_element.objectName().split('_')
        row, column = int(element_index[0]), int(element_index[1])
        value_list = sender.split(' ')
        value = value_list[1]
        self.current_element.setText(value)
        self.properties_view.apply_values_changes((self.label_name.text(), [(row, column), value]))
