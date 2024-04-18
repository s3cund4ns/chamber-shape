from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QDoubleSpinBox, QAbstractSpinBox, QSpinBox

from widgets.property_items.property_item import PropertyItem


class PropertyVector2DInt(PropertyItem):
    def __init__(self):
        super(PropertyVector2DInt, self).__init__()

        self.vertical_layout = QVBoxLayout(self)
        self.horizontal_layout = QHBoxLayout(self)
        self.label_name = QLabel(self)
        self.horizontal_layout.addWidget(self.label_name)
        self.spin_box_value_x = QSpinBox(self)
        self.spin_box_value_x.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spin_box_value_x.setObjectName('x')
        self.horizontal_layout.addWidget(self.spin_box_value_x)
        self.spin_box_value_y = QSpinBox(self)
        self.spin_box_value_y.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spin_box_value_y.setObjectName('y')
        self.horizontal_layout.addWidget(self.spin_box_value_y)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.spin_box_value_x.valueChanged.connect(self.get_values_changes)
        self.spin_box_value_y.valueChanged.connect(self.get_values_changes)

    def set_data(self, data):
        name, value_x, value_y = data
        self.label_name.setText(name)
        self.spin_box_value_x.setValue(value_x)
        self.spin_box_value_y.setValue(value_y)

    def get_values_changes(self):
        data = []
        sender = self.sender()
        match sender.objectName():
            case 'x':
                data = [sender.value(), self.spin_box_value_y.value()]
            case 'y':
                data = [self.spin_box_value_x.value(), sender.value()]

        self.properties_view.apply_values_changes((self.label_name.text(), data))
