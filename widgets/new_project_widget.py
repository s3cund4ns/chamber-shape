from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton, QComboBox, QFileDialog, \
    QSpacerItem, QSizePolicy


class NewProjectWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowTitle('Создать Новый Проект')
        self.setWindowIcon(QIcon('favicon.ico'))

        self.parameter_name_font = QFont()
        self.parameter_name_font.setPointSize(12)
        self.parameter_name_font.setBold(True)

        self.parameter_value_font = QFont()
        self.parameter_value_font.setBold(True)

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        self.header_layout = QHBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 15)
        self.image_label = QLabel(self)
        self.image = QPixmap('resources/ChamberShapeMiniLogoApp.png')
        self.image_label.setPixmap(self.image)
        self.header_layout.addWidget(self.image_label)
        self.label_header = QLabel(self)
        self.label_header.setText('Создать Новый Проект')
        self.header_label_font = QFont()
        self.header_label_font.setPointSize(18)
        self.header_label_font.setBold(True)
        self.label_header.setFont(self.header_label_font)
        self.header_layout.addWidget(self.label_header)
        self.header_spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.header_layout.addItem(self.header_spacer)
        self.verticalLayout.addLayout(self.header_layout)

        self.layout_project_name = QHBoxLayout()
        self.label_project_name = QLabel(self)
        self.label_project_name.setText('Название:')
        self.label_project_name.setFont(self.parameter_name_font)
        self.line_edit_project_name = QLineEdit(self)
        self.line_edit_project_name.setFont(self.parameter_value_font)
        self.layout_project_name.addWidget(self.label_project_name)
        self.layout_project_name.addWidget(self.line_edit_project_name)
        self.verticalLayout.addLayout(self.layout_project_name)

        self.layout_project_directory = QHBoxLayout()
        self.label_project_directory = QLabel(self)
        self.label_project_directory.setText('Путь:')
        self.label_project_directory.setFont(self.parameter_name_font)
        self.line_edit_project_directory = QLineEdit(self)
        self.line_edit_project_directory.setFont(self.parameter_value_font)
        self.button_choose_project_directory = QPushButton(self)
        self.button_choose_project_directory.setText('  ...  ')
        self.button_choose_project_directory.clicked.connect(self.open_project_directory)
        self.layout_project_directory.addWidget(self.label_project_directory)
        self.layout_project_directory.addWidget(self.line_edit_project_directory)
        self.layout_project_directory.addWidget(self.button_choose_project_directory)
        self.verticalLayout.addLayout(self.layout_project_directory)

        self.layout_precision_code = QHBoxLayout()
        self.label_precision_code = QLabel(self)
        self.label_precision_code.setText('Прецизионный Код:')
        self.label_precision_code.setFont(self.parameter_name_font)
        self.combo_box_precision_code = QComboBox(self)
        self.combo_box_precision_code.addItems(['Serpent', 'OpenMC'])
        self.combo_box_precision_code.setCurrentIndex(0)
        self.combo_box_precision_code.setFont(self.parameter_value_font)
        self.layout_precision_code.addWidget(self.label_precision_code)
        self.layout_precision_code.addWidget(self.combo_box_precision_code)
        self.verticalLayout.addLayout(self.layout_precision_code)

        self.layout_precision_code_directory = QHBoxLayout()
        self.label_precision_code_directory = QLabel(self)
        self.label_precision_code_directory.setText('Путь к Директории Кода:')
        self.label_precision_code_directory.setFont(self.parameter_name_font)
        self.line_edit_precision_code_directory = QLineEdit(self)
        self.line_edit_precision_code_directory.setFont(self.parameter_value_font)
        self.button_choose_precision_code_directory = QPushButton(self)
        self.button_choose_precision_code_directory.setText('  ...  ')
        self.button_choose_precision_code_directory.clicked.connect(self.open_precision_code_directory)
        self.layout_precision_code_directory.addWidget(self.label_precision_code_directory)
        self.layout_precision_code_directory.addWidget(self.line_edit_precision_code_directory)
        self.layout_precision_code_directory.addWidget(self.button_choose_precision_code_directory)
        self.verticalLayout.addLayout(self.layout_precision_code_directory)

        self.layout_nuclear_data_library = QHBoxLayout()
        self.label_nuclear_data_library = QLabel(self)
        self.label_nuclear_data_library.setText('Библиотека Данных:')
        self.label_nuclear_data_library.setFont(self.parameter_name_font)
        self.combo_box_nuclear_data_library = QComboBox(self)
        self.combo_box_nuclear_data_library.addItems(['JEFF'])
        self.combo_box_nuclear_data_library.setCurrentIndex(0)
        self.combo_box_nuclear_data_library.setFont(self.parameter_value_font)
        self.layout_nuclear_data_library.addWidget(self.label_nuclear_data_library)
        self.layout_nuclear_data_library.addWidget(self.combo_box_nuclear_data_library)
        self.verticalLayout.addLayout(self.layout_nuclear_data_library)

        self.layout_nuclear_data_library_directory = QHBoxLayout()
        self.label_nuclear_data_library_directory = QLabel(self)
        self.label_nuclear_data_library_directory.setText('Путь к Библиотеке Данных:')
        self.label_nuclear_data_library_directory.setFont(self.parameter_name_font)
        self.line_edit_nuclear_data_library_directory = QLineEdit(self)
        self.line_edit_nuclear_data_library_directory.setFont(self.parameter_value_font)
        self.button_choose_nuclear_data_library_directory = QPushButton(self)
        self.button_choose_nuclear_data_library_directory.setText('  ...  ')
        self.button_choose_nuclear_data_library_directory.clicked.connect(self.open_nuclear_data_library_directory)
        self.layout_nuclear_data_library_directory.addWidget(self.label_nuclear_data_library_directory)
        self.layout_nuclear_data_library_directory.addWidget(self.line_edit_nuclear_data_library_directory)
        self.layout_nuclear_data_library_directory.addWidget(self.button_choose_nuclear_data_library_directory)
        self.verticalLayout.addLayout(self.layout_nuclear_data_library_directory)

        self.layout_create_or_cancel = QHBoxLayout()
        self.button_create_project = QPushButton(self)
        self.button_create_project.setText('Создать')
        self.button_create_project.setFont(self.parameter_value_font)
        self.button_cancel = QPushButton(self)
        self.button_cancel.setText('Отмена')
        self.button_cancel.setFont(self.parameter_value_font)
        self.layout_create_or_cancel.addWidget(self.button_create_project)
        self.layout_create_or_cancel.addWidget(self.button_cancel)
        self.verticalLayout.addLayout(self.layout_create_or_cancel)

    def open_choose_directory_window(self, caption: str) -> str | None:
        response = QFileDialog.getExistingDirectory(
            parent=self,
            caption=caption
        )
        return response

    def open_project_directory(self):
        directory: str = self.open_choose_directory_window('Выбрать Директорию Проекта')
        self.line_edit_project_directory.setText(directory)

    def open_precision_code_directory(self):
        directory: str = self.open_choose_directory_window('Выбрать Директорию Прецизионного Кода')
        self.line_edit_precision_code_directory.setText(directory)

    def open_nuclear_data_library_directory(self):
        directory: str = self.open_choose_directory_window('Выбрать Директорию Библиотеки Данных')
        self.line_edit_nuclear_data_library_directory.setText(directory)

    def get_data(self):
        project_name = self.line_edit_project_name.text()
        project_directory = self.line_edit_project_directory.text()
        precision_code = self.combo_box_precision_code.currentText()
        precision_code_directory = self.line_edit_precision_code_directory.text()
        nuclear_data_library = self.combo_box_nuclear_data_library.currentText()
        nuclear_data_library_directory = self.line_edit_nuclear_data_library_directory.text()

        return {
            'project_name': project_name,
            'project_directory': project_directory,
            'solver': precision_code,
            'solver_directory': precision_code_directory,
            'calculation_data_directory': '',
            'nuclear_data_library': nuclear_data_library,
            'nuclear_data_library_directory': nuclear_data_library_directory
        }


