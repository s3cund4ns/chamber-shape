from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QDoubleSpinBox, QAbstractSpinBox

from widgets.property_items.property_item import PropertyItem


class PropertyVector3DFloat(PropertyItem):
    def __init__(self):
        super(PropertyVector3DFloat, self).__init__()

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
        self.double_spin_box_value_z = QDoubleSpinBox(self)
        self.double_spin_box_value_z.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.double_spin_box_value_z.setObjectName('z')
        self.horizontal_layout.addWidget(self.double_spin_box_value_z)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.double_spin_box_value_x.valueChanged.connect(self.get_values_changes)
        self.double_spin_box_value_y.valueChanged.connect(self.get_values_changes)
        self.double_spin_box_value_z.valueChanged.connect(self.get_values_changes)

    def set_data(self, data):
        name, value_x, value_y, value_z = data
        self.label_name.setText(name)
        self.double_spin_box_value_x.setValue(value_x)
        self.double_spin_box_value_y.setValue(value_y)
        self.double_spin_box_value_z.setValue(value_z)

    def get_values_changes(self):
        data = []
        sender = self.sender()
        match sender.objectName():
            case 'x':
                data = [sender.value(), self.double_spin_box_value_y.value(), self.double_spin_box_value_z.value()]
            case 'y':
                data = [self.double_spin_box_value_x.value(), sender.value(), self.double_spin_box_value_z.value()]
            case 'z':
                data = [self.double_spin_box_value_x.value(), self.double_spin_box_value_y.value(), sender.value()]

        self.properties_view.apply_values_changes((self.label_name.text(), data))
