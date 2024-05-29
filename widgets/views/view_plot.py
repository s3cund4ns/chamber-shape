from PySide6.QtWidgets import QTabWidget
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from project_data.view import View


class ViewPlot(View):
    def __init__(self):
        super().__init__()
        self.tab_widget: QTabWidget | None = None

    def set_tab_widget(self, tab_widget: QTabWidget):
        self.tab_widget = tab_widget

    def add_item(self, *args):
        pass

    def select_item(self, *args):
        pass

    def change_item(self, *plot_property):
        name, energy_mid_grid, sp_flux, sp_errors = plot_property
        # plt.style.use('dark_background')
        fig = Figure(figsize=(5, 4), dpi=100)
        axes = fig.add_subplot(111)
        canvas = FigureCanvasQTAgg(fig)
        axes.errorbar(energy_mid_grid, sp_flux, sp_errors * 3 * sp_flux, marker=',')
        axes.grid(visible=True, which='major', axis='both', color='0.3', linestyle='-', linewidth=0.5)
        axes.grid(visible=True, which='minor', axis='both', color='0.7', linestyle='-', linewidth=0.5)
        axes.set(xlabel='Энергия, МэВ', ylabel='ФV, отн. ед.', xscale='log', yscale='log',
                 xlim=(1e-8, 20), ylim=(2e-3, 2e1))
        axes.set_xticks((1e-7, 1e-5, 1e-3, 1e-1, 10), minor=True)
        axes.legend(loc='best')
        self.tab_widget.addTab(canvas, name)
