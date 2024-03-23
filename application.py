import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from widgets.main_window import MainWindow
from widgets.plot_widget import PlotWidget
from widgets.styling_widget import StylingWidget


class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()
        self.main_window.setWindowTitle('Chamber Shape')
        # self.plot_widget = PlotWidget()
        # self.main_window = StylingWidget()
        with open('styles/dark.qss', 'r') as file:
            self.main_window.setStyleSheet(file.read())
            # self.plot_widget.setStyleSheet(file.read())
        self.main_window.show()
        # self.plot_widget.show()

    def run(self):
        self.app.exec()
