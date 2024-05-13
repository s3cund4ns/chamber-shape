from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowTitle('Starter Shape')
        self.setWindowIcon(QIcon('favicon.ico'))
        with open('styles/dark.qss', 'r') as file:
            self.setStyleSheet(file.read())

        self.vertical_layout = QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)

        self.label_header = QLabel(self)
        self.label_header.setText('Start or continue the chamber shaping')
        self.label_header.setFont(QFont('MS Shell Dig 2', 16))
        self.vertical_layout.addWidget(self.label_header)

        self.button_create_project = QPushButton(self)
        self.button_create_project.setText('Create Project')
        self.vertical_layout.addWidget(self.button_create_project)

        self.button_open_project = QPushButton(self)
        self.button_open_project.setText('Open Project')
        self.vertical_layout.addWidget(self.button_open_project)
