from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowTitle('Добро Пожаловать')
        self.setWindowIcon(QIcon('favicon.ico'))
        with open('styles/light.qss', 'r') as file:
            self.setStyleSheet(file.read())

        self.vertical_layout = QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)

        self.label_header = QLabel(self)
        self.label_header.setText('Начать или Продолжить Моделирование')
        self.label_header.setFont(QFont('MS Shell Dig 2', 16))
        self.vertical_layout.addWidget(self.label_header)

        self.image_label = QLabel(self)
        self.image = QPixmap('D:/Projects/chamber-shape/resources/ChamberShapeGreatestWithoutBack.png')
        self.image_label.setPixmap(self.image)
        self.vertical_layout.addWidget(self.image_label)


        self.button_create_project = QPushButton(self)
        self.button_create_project.setText('Создать Проект')
        self.vertical_layout.addWidget(self.button_create_project)

        self.button_open_project = QPushButton(self)
        self.button_open_project.setText('Открыть проект')
        self.vertical_layout.addWidget(self.button_open_project)
