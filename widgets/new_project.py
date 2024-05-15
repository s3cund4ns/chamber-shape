from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton, QComboBox, QFileDialog


class NewProject(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowTitle('Create new project')
        self.setWindowIcon(QIcon('favicon.ico'))
        with open('styles/light.qss', 'r') as file:
            self.setStyleSheet(file.read())

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.label_header = QLabel(self)
        self.label_header.setText('Create new project')
        self.label_header.setFont(QFont('MS Shell Dig 2', 16))
        self.verticalLayout.addWidget(self.label_header)

        self.layout_project_name = QHBoxLayout()
        self.label_project_name = QLabel(self)
        self.label_project_name.setText('Name:')
        self.line_edit_project_name = QLineEdit(self)
        self.layout_project_name.addWidget(self.label_project_name)
        self.layout_project_name.addWidget(self.line_edit_project_name)
        self.verticalLayout.addLayout(self.layout_project_name)

        self.layout_project_directory = QHBoxLayout()
        self.label_project_directory = QLabel(self)
        self.label_project_directory.setText('Directory:')
        self.line_edit_project_directory = QLineEdit(self)
        self.button_choose_project_directory = QPushButton(self)
        self.button_choose_project_directory.setText('...')
        self.button_choose_project_directory.clicked.connect(self.open_project_directory)
        self.layout_project_directory.addWidget(self.label_project_directory)
        self.layout_project_directory.addWidget(self.line_edit_project_directory)
        self.layout_project_directory.addWidget(self.button_choose_project_directory)
        self.verticalLayout.addLayout(self.layout_project_directory)

        self.layout_precision_code = QHBoxLayout()
        self.label_precision_code = QLabel(self)
        self.label_precision_code.setText('Precision code:')
        self.combo_box_precision_code = QComboBox(self)
        self.combo_box_precision_code.addItems(['Serpent', 'OpenMC'])
        self.combo_box_precision_code.setCurrentIndex(0)
        self.layout_precision_code.addWidget(self.label_precision_code)
        self.layout_precision_code.addWidget(self.combo_box_precision_code)
        self.verticalLayout.addLayout(self.layout_precision_code)

        self.layout_precision_code_directory = QHBoxLayout()
        self.label_precision_code_directory = QLabel(self)
        self.label_precision_code_directory.setText('Precision code directory:')
        self.line_edit_precision_code_directory = QLineEdit(self)
        self.button_choose_precision_code_directory = QPushButton(self)
        self.button_choose_precision_code_directory.setText('...')
        self.button_choose_precision_code_directory.clicked.connect(self.open_precision_code_directory)
        self.layout_precision_code_directory.addWidget(self.label_precision_code_directory)
        self.layout_precision_code_directory.addWidget(self.line_edit_precision_code_directory)
        self.layout_precision_code_directory.addWidget(self.button_choose_precision_code_directory)
        self.verticalLayout.addLayout(self.layout_precision_code_directory)

        self.layout_nuclear_data_library = QHBoxLayout()
        self.label_nuclear_data_library = QLabel(self)
        self.label_nuclear_data_library.setText('Nuclear data library:')
        self.combo_box_nuclear_data_library = QComboBox(self)
        self.combo_box_nuclear_data_library.addItems(['JEFF'])
        self.combo_box_nuclear_data_library.setCurrentIndex(0)
        self.layout_nuclear_data_library.addWidget(self.label_nuclear_data_library)
        self.layout_nuclear_data_library.addWidget(self.combo_box_nuclear_data_library)
        self.verticalLayout.addLayout(self.layout_nuclear_data_library)

        self.layout_nuclear_data_library_directory = QHBoxLayout()
        self.label_nuclear_data_library_directory = QLabel(self)
        self.label_nuclear_data_library_directory.setText('Nuclear data directory:')
        self.line_edit_nuclear_data_library_directory = QLineEdit(self)
        self.button_choose_nuclear_data_library_directory = QPushButton(self)
        self.button_choose_nuclear_data_library_directory.setText('...')
        self.button_choose_nuclear_data_library_directory.clicked.connect(self.open_nuclear_data_library_directory)
        self.layout_nuclear_data_library_directory.addWidget(self.label_nuclear_data_library_directory)
        self.layout_nuclear_data_library_directory.addWidget(self.line_edit_nuclear_data_library_directory)
        self.layout_nuclear_data_library_directory.addWidget(self.button_choose_nuclear_data_library_directory)
        self.verticalLayout.addLayout(self.layout_nuclear_data_library_directory)

        self.layout_create_or_cancel = QHBoxLayout()
        self.button_create_project = QPushButton(self)
        self.button_create_project.setText('Create')
        self.button_cancel = QPushButton(self)
        self.button_cancel.setText('Cancel')
        self.button_cancel.clicked.connect(self.close)
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
        directory: str = self.open_choose_directory_window('Choose a project directory')
        self.line_edit_project_directory.setText(directory)

    def open_precision_code_directory(self):
        directory: str = self.open_choose_directory_window('Choose a precision code directory')
        self.line_edit_precision_code_directory.setText(directory)

    def open_nuclear_data_library_directory(self):
        directory: str = self.open_choose_directory_window('Choose a nuclear data library directory')
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


