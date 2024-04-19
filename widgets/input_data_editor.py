from PySide6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QTextEdit

from project_data.view import View


class InputDataEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout = QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.text_edit: QTextEdit = QTextEdit(self)
        self.vertical_layout.addWidget(self.text_edit)

    def set_text(self, text: str):
        self.text_edit.setText(text)

    def get_text(self):
        return self.text_edit.document().toRawText()

