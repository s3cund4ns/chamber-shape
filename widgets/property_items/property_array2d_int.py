from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QPushButton, QMenu, QComboBox

from widgets.property_items.property_item import PropertyItem


class PropertyArray2DInt(PropertyItem):
    def __init__(self):
        super().__init__()

        self.all_values: list = []
        self.vertical_layout = QVBoxLayout(self)
        self.label_name = QLabel(self)
        self.vertical_layout.addWidget(self.label_name)
        self.array_grid_layout = QGridLayout(self)
        self.vertical_layout.addLayout(self.array_grid_layout)

    def set_default_values(self, *args):
        pass

    def set_data(self, data):
        name, *values = data
        array, self.all_values = values
        print(values)
        self.label_name.setText(name)
        for row in range(array.shape[0]):
            for column in range(array.shape[1]):
                element = QComboBox(self)
                element.setObjectName(f'{row}_{column}')
                element.addItems(self.all_values)
                element.setCurrentText(str(array[row, column]))
                element.currentIndexChanged.connect(self.change_item)
                self.array_grid_layout.addWidget(element, row, column)

    def change_item(self):
        sender = self.sender().currentIndex()
        self.properties_view.apply_values_changes((self.label_name.text(), [self.sender().objectName(), sender]))
