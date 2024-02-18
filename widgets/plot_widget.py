from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import serpentTools


class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        x = [1, 2, 3, 4, 5, 6]
        y = [10, 20, 30, 40, 50, 60]

        fig = Figure()
        ax = fig.add_subplot()
        ax.plot(x, y, label='')

        canvas = FigureCanvasQTAgg(fig)
        layout.addWidget(canvas)
