from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, \
    QListWidget


class StartWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.vertical_layout = QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)

        self.title_font = QFont()
        self.title_font.setPointSize(16)

        self.button_font = QFont()
        self.button_font.setBold(True)

        self.header_layout = QHBoxLayout(self)
        self.header_layout.setContentsMargins(5, 5, 5, 15)
        self.image_label = QLabel(self)
        self.image = QPixmap('D:/Projects/chamber-shape/resources/ChamberShapeMiniLogoApp.png')
        self.image_label.setPixmap(self.image)
        self.header_layout.addWidget(self.image_label)
        self.label_header = QLabel(self)
        self.label_header.setText('Starter Shape')
        self.header_label_font = QFont()
        self.header_label_font.setPointSize(18)
        self.header_label_font.setBold(True)
        self.label_header.setFont(self.header_label_font)
        self.header_layout.addWidget(self.label_header)
        self.header_spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.header_layout.addItem(self.header_spacer)
        self.vertical_layout.addLayout(self.header_layout)

        self.horizontal_layout = QHBoxLayout(self)

        self.buttons_layout = QVBoxLayout(self)
        self.buttons_layout.setContentsMargins(10, 70, 10, 0)
        self.button_create_project = QPushButton(self)
        self.button_create_project.setText('Создать Проект')
        self.button_create_project.setFont(self.button_font)
        self.buttons_layout.addWidget(self.button_create_project)

        self.button_open_project = QPushButton(self)
        self.button_open_project.setText('Открыть проект')
        self.button_open_project.setFont(self.button_font)
        self.buttons_layout.addWidget(self.button_open_project)

        self.button_open_manual = QPushButton(self)
        self.button_open_manual.setText('Руководство пользователя')
        self.button_open_manual.setFont(self.button_font)
        self.buttons_layout.addWidget(self.button_open_manual)

        self.buttons_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.buttons_layout.addItem(self.buttons_spacer)

        self.horizontal_layout.addLayout(self.buttons_layout)

        self.recent_projects_layout = QVBoxLayout(self)
        self.recent_projects_layout.setContentsMargins(5, 5, 5, 5)
        self.recent_projects_title_label = QLabel(self)
        self.recent_projects_title_label.setText('Недавние Проекты')
        self.recent_projects_title_label.setFont(self.title_font)
        self.recent_projects_layout.addWidget(self.recent_projects_title_label)

        self.recent_projects_list = QListWidget(self)
        self.recent_projects_layout.addWidget(self.recent_projects_list)

        self.horizontal_layout.addLayout(self.recent_projects_layout)

        self.vertical_layout.addLayout(self.horizontal_layout)
