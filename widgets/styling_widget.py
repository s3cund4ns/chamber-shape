from ui_files.ui_styling import UiForm
from PySide6.QtWidgets import QWidget


class StylingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = UiForm()
        self.ui.setupUi(self)

