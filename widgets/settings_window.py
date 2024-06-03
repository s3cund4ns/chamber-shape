from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QFont
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QComboBox, \
    QPushButton


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowTitle('Параметры')
        self.setWindowIcon(QIcon('favicon.ico'))

        self.settings_group_title_font = QFont()
        self.settings_group_title_font.setPointSize(16)

        self.parameter_name_font = QFont()
        self.parameter_name_font.setPointSize(12)
        self.parameter_name_font.setBold(True)

        self.parameter_value_font = QFont()
        self.parameter_value_font.setBold(True)

        self.vertical_layout = QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(5, 5, 5, 5)

        self.header_layout = QHBoxLayout(self)
        self.header_layout.setContentsMargins(0, 0, 0, 15)
        self.image_label = QLabel(self)
        self.image = QPixmap('D:/Projects/chamber-shape/resources/ChamberShapeMiniLogoApp.png')
        self.image_label.setPixmap(self.image)
        self.header_layout.addWidget(self.image_label)
        self.header_label = QLabel(self)
        self.header_label.setText('Параметры')
        self.header_label_font = QFont()
        self.header_label_font.setPointSize(18)
        self.header_label_font.setBold(True)
        self.header_label.setFont(self.header_label_font)
        self.header_layout.addWidget(self.header_label)
        self.header_spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.header_layout.addItem(self.header_spacer)
        self.vertical_layout.addLayout(self.header_layout)

        self.appearance_label = QLabel(self)
        self.appearance_label.setText('Внешний вид')
        self.appearance_label.setFont(self.settings_group_title_font)
        self.vertical_layout.addWidget(self.appearance_label)

        self.theme_layout = QHBoxLayout(self)
        self.theme_layout.setContentsMargins(0, 0, 5, 5)
        self.theme_label = QLabel(self)
        self.theme_label.setText('Тема Приложения:')
        self.theme_label.setFont(self.parameter_name_font)
        self.theme_layout.addWidget(self.theme_label)
        self.theme_combo_box = QComboBox(self)
        self.theme_combo_box.addItems(['Светлая', 'Темная'])
        self.theme_combo_box.setCurrentIndex(0)
        self.theme_combo_box.setFont(self.parameter_value_font)
        self.theme_layout.addWidget(self.theme_combo_box)
        self.vertical_layout.addLayout(self.theme_layout)

        self.language_layout = QHBoxLayout(self)
        self.language_layout.setContentsMargins(0, 0, 5, 5)
        self.language_label = QLabel(self)
        self.language_label.setText('Язык:')
        self.language_label.setFont(self.parameter_name_font)
        self.language_layout.addWidget(self.language_label)
        self.language_combo_box = QComboBox(self)
        self.language_combo_box.addItems(['Русский', 'English'])
        self.language_combo_box.setCurrentIndex(0)
        self.language_combo_box.setFont(self.parameter_value_font)
        self.language_layout.addWidget(self.language_combo_box)
        self.vertical_layout.addLayout(self.language_layout)

        # self.project_label = QLabel(self)
        # self.project_label.setText('Проект')
        # self.project_label.setFont(self.settings_group_title_font)
        # self.vertical_layout.addWidget(self.project_label)

        self.buttons_layout = QHBoxLayout(self)
        self.buttons_layout.setContentsMargins(10, 10, 10, 10)
        self.apply_button = QPushButton(self)
        self.apply_button.setText('Применить')
        self.apply_button.setFont(self.parameter_value_font)
        self.buttons_layout.addWidget(self.apply_button)
        self.cancel_button = QPushButton(self)
        self.cancel_button.setText('Отмена')
        self.cancel_button.setFont(self.parameter_value_font)
        self.buttons_layout.addWidget(self.cancel_button)
        self.vertical_layout.addLayout(self.buttons_layout)

    def get_data(self):
        app_theme = self.theme_combo_box.currentText()
        return app_theme
