from PySide6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QTextEdit

from project_data.view import View


class CodeEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout = QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.code_line_edit: QTextEdit = QTextEdit(self)
        self.vertical_layout.addWidget(self.code_line_edit)

