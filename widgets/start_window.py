from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.main_window = None
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowTitle('Добро Пожаловать')
        self.setWindowIcon(QIcon('favicon.ico'))

        self.vertical_layout = QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)

    def set_main_window(self, main_window):
        self.main_window = main_window

    def closeEvent(self, event):
        self.main_window.close()
