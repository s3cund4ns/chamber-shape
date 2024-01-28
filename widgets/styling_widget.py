from ui_files.ui_styling import Ui_Form
from PySide6.QtWidgets import QWidget


class StylingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

