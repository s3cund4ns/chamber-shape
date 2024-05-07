from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QDoubleSpinBox, QAbstractSpinBox

from widgets.property_items.property_item import PropertyItem


class PropertyVector2DFloat(PropertyItem):
    def __init__(self):
        super(PropertyVector2DFloat, self).__init__()

        self.vertical_layout = QVBoxLayout(self)
        self.horizontal_layout = QHBoxLayout(self)
        self.label_name = QLabel(self)
        self.horizontal_layout.addWidget(self.label_name)
        self.double_spin_box_value_x = QDoubleSpinBox(self)
        self.double_spin_box_value_x.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.double_spin_box_value_x.setObjectName('x')
        self.horizontal_layout.addWidget(self.double_spin_box_value_x)
        self.double_spin_box_value_y = QDoubleSpinBox(self)
        self.double_spin_box_value_y.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.double_spin_box_value_y.setObjectName('y')
        self.horizontal_layout.addWidget(self.double_spin_box_value_y)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.double_spin_box_value_x.valueChanged.connect(self.get_values_changes)
        self.double_spin_box_value_y.valueChanged.connect(self.get_values_changes)

    def set_data(self, data):
        print(data)
        name, values, values_range = data
        value_x, value_y = values
        min_value, max_value = values_range
        self.label_name.setText(name)
        self.double_spin_box_value_x.setMinimum(min_value)
        self.double_spin_box_value_x.setMaximum(max_value)
        self.double_spin_box_value_y.setMinimum(min_value)
        self.double_spin_box_value_y.setMaximum(max_value)
        self.double_spin_box_value_x.setValue(value_x)
        self.double_spin_box_value_y.setValue(value_y)

    def get_values_changes(self):
        data = []
        sender = self.sender()
        match sender.objectName():
            case 'x':
                data = [sender.value(), self.double_spin_box_value_y.value()]
            case 'y':
                data = [self.double_spin_box_value_x.value(), sender.value()]

        self.properties_view.apply_values_changes((self.label_name.text(), data))
