from PySide6.QtWidgets import QWidget
from ui_files.ui_property_item import UiForm


class PropertyItemWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = UiForm()
        self.ui.setupUi(self)

    def set_name(self, name: str):
        self.ui.label_property_item_name.setText(name)

    def set_value(self, value: float):
        self.ui.dsb_property_item_value.setValue(value)

    def get_value(self) -> float:
        value = self.ui.dsb_property_item_value.value()
        return value


