from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QDoubleSpinBox, QAbstractSpinBox, QSpinBox, QPushButton, \
    QColorDialog

from widgets.property_items.property_item import PropertyItem


class PropertyColor(PropertyItem):
    def __init__(self):
        super(PropertyColor, self).__init__()

        self.vertical_layout = QVBoxLayout(self)
        self.horizontal_layout = QHBoxLayout(self)
        self.label_name = QLabel(self)
        self.horizontal_layout.addWidget(self.label_name)
        self.spin_box_value_r = QSpinBox(self)
        self.spin_box_value_r.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spin_box_value_r.setObjectName('r')
        self.horizontal_layout.addWidget(self.spin_box_value_r)
        self.spin_box_value_g = QSpinBox(self)
        self.spin_box_value_g.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spin_box_value_g.setObjectName('g')
        self.horizontal_layout.addWidget(self.spin_box_value_g)
        self.spin_box_value_b = QSpinBox(self)
        self.spin_box_value_b.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spin_box_value_b.setObjectName('b')
        self.horizontal_layout.addWidget(self.spin_box_value_b)

        self.button_choose_color = QPushButton(self)
        self.button_choose_color.setText('   ...   ')
        self.button_choose_color.clicked.connect(self.set_color_from_dialog)
        self.vertical_layout.addLayout(self.horizontal_layout)
        self.vertical_layout.addWidget(self.button_choose_color)

        self.spin_box_value_r.valueChanged.connect(self.get_values_changes)
        self.spin_box_value_g.valueChanged.connect(self.get_values_changes)
        self.spin_box_value_b.valueChanged.connect(self.get_values_changes)

    def set_data(self, data):
        name, value_r, value_g, value_b = data
        self.label_name.setText(name)
        self.spin_box_value_r.setMinimum(0)
        self.spin_box_value_r.setMaximum(255)
        self.spin_box_value_r.setValue(value_r)

        self.spin_box_value_g.setMinimum(0)
        self.spin_box_value_g.setMaximum(255)
        self.spin_box_value_g.setValue(value_g)

        self.spin_box_value_b.setMinimum(0)
        self.spin_box_value_b.setMaximum(255)
        self.spin_box_value_b.setValue(value_b)

    def get_values_changes(self):
        data = []
        sender = self.sender()
        match sender.objectName():
            case 'r':
                data = [sender.value(), self.spin_box_value_g.value(), self.spin_box_value_b.value()]
            case 'g':
                data = [self.spin_box_value_r.value(), sender.value(), self.spin_box_value_b.value()]
            case 'b':
                data = [self.spin_box_value_r.value(), self.spin_box_value_g.value(), sender.value()]

        self.properties_view.apply_values_changes((self.label_name.text(), data))

    def set_color_from_dialog(self):
        color_dialog: QColorDialog = QColorDialog(self)
        color: QColor = color_dialog.getColor()
        self.spin_box_value_r.setValue(color.red())
        self.spin_box_value_g.setValue(color.green())
        self.spin_box_value_b.setValue(color.blue())
