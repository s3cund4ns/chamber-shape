from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowTitle('Settings')
        self.setWindowIcon(QIcon('favicon.ico'))
        with open('styles/dark.qss', 'r') as file:
            self.setStyleSheet(file.read())
