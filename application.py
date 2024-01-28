import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication
from widgets.main_window import MainWindow
from widgets.styling_widget import StylingWidget


class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()
        # self.main_window = StylingWidget()
        # with open('styles/style.qss', 'r') as file:
        #     self.main_window.setStyleSheet(file.read())
        self.main_window.show()

    def run(self):
        self.app.exec()
