import sys

from PySide6.QtWidgets import QApplication
from widgets.main_window import MainWindow


class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()
        self.main_window.show()

    def run(self):
        self.app.exec()
