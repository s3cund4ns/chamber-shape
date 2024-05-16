from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import serpentTools
import os


class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        x = [1, 2, 3, 4, 5, 6]
        y = [10, 20, 30, 40, 50, 60]

        plot = plt.plot(x, y)

        canvas = FigureCanvasQTAgg(plot)
        layout.addWidget(canvas)
