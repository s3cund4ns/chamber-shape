from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QComboBox

from widgets.property_items.property_item import PropertyItem


class PropertyVector3DComboBox(PropertyItem):
    def __init__(self):
        super().__init__()

        self.vertical_layout = QVBoxLayout(self)
        self.horizontal_layout = QHBoxLayout(self)
        self.label_name = QLabel(self)
        self.horizontal_layout.addWidget(self.label_name)
        self.label_name_x = QLabel(self)
        self.horizontal_layout.addWidget(self.label_name_x)
        self.combo_box_value_x = QComboBox(self)
        self.combo_box_value_x.setObjectName('x')
        self.horizontal_layout.addWidget(self.combo_box_value_x)
        self.label_name_y = QLabel(self)
        self.horizontal_layout.addWidget(self.label_name_y)
        self.combo_box_value_y = QComboBox(self)
        self.combo_box_value_y.setObjectName('y')
        self.horizontal_layout.addWidget(self.combo_box_value_y)
        self.label_name_z = QLabel(self)
        self.horizontal_layout.addWidget(self.label_name_z)
        self.combo_box_value_z = QComboBox(self)
        self.combo_box_value_z.setObjectName('z')
        self.horizontal_layout.addWidget(self.combo_box_value_z)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.combo_box_value_x.currentTextChanged.connect(self.get_values_changes)
        self.combo_box_value_y.currentTextChanged.connect(self.get_values_changes)
        self.combo_box_value_z.currentTextChanged.connect(self.get_values_changes)

    def set_data(self, data):
        (name, name_x, current_value_x, all_values_x,
         name_y, current_value_y, all_values_y,
         name_z, current_value_z, all_values_z) = data
        self.label_name.setText(name)

        self.label_name_x.setText(name_x)
        self.combo_box_value_x.setCurrentText(current_value_x)
        self.combo_box_value_x.insertItems(self.combo_box_value_x.count(), all_values_x)

        self.label_name_y.setText(name_y)
        self.combo_box_value_y.setCurrentText(current_value_y)
        self.combo_box_value_y.insertItems(self.combo_box_value_y.count(), all_values_y)

        self.label_name_z.setText(name_z)
        self.combo_box_value_z.setCurrentText(current_value_z)
        self.combo_box_value_z.insertItems(self.combo_box_value_z.count(), all_values_z)

    def get_values_changes(self):
        data = []
        sender = self.sender()
        match sender.objectName():
            case 'x':
                data = [sender.currentText(), self.combo_box_value_y.currentText(), self.combo_box_value_z.currentText()]
            case 'y':
                data = [self.combo_box_value_x.currentText(), sender.currentText(), self.combo_box_value_z.currentText()]
            case 'z':
                data = [self.combo_box_value_x.currentText(), self.combo_box_value_y.currentText(), sender.currentText()]

        self.properties_view.apply_values_changes((self.label_name.text(), data))

