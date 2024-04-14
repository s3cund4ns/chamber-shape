import os

from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QMainWindow, QWidget, QFileDialog

from project_data.project_data import ProjectData
from renderer.view_renderer import ViewRenderer
from renderer.viewport import Viewport
from widgets.input_data_editor import InputDataEditor
from ui_files.ui_main import Ui_MainWindow
from widgets.view_input_data import ViewInputData

from widgets.view_materials_list import ViewMaterialsList
from widgets.view_properties import ViewSurfaceProperties, ViewMaterialProperties, ViewUniverseProperties
from widgets.view_surfaces_list import ViewSurfacesList
from widgets.view_universes_tree import ViewUniversesTree


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Chamber Shape')

        with open('styles/dark.qss', 'r') as file:
            self.setStyleSheet(file.read())

        QFontDatabase.addApplicationFont('../resources/fonts/Inter-Medium.ttf')
        font = QFont("Inter-Medium.ttf", 14)

        # self.plot_widget = PlotWidget()

        self.file_menu = self.ui.menubar.addMenu('File')
        new_project_action = self.file_menu.addAction('New project')
        new_project_action.triggered.connect(self.new_project)
        open_action = self.file_menu.addAction('Open')
        open_action.triggered.connect(self.load_file)
        save_action = self.file_menu.addAction('Save')
        save_action.triggered.connect(self.save)
        save_as_action = self.file_menu.addAction('Save as')
        save_as_action.triggered.connect(self.save_as)

        self.file_menu = self.ui.menubar.addMenu('Edit')
        self.file_menu.addAction('Cut')
        self.file_menu.addAction('Copy')
        self.file_menu.addAction('Paste')

        self.file_menu = self.ui.menubar.addMenu('Project')
        run_simulation = self.file_menu.addAction('Run simulation')
        run_simulation.triggered.connect(self.run_simulation)
        open_code = self.file_menu.addAction('Open code')
        open_code.triggered.connect(self.open_code_editor)
        open_plot = self.file_menu.addAction('Open plot')
        open_plot.triggered.connect(self.open_plot)

        self.input_data_editor = InputDataEditor()

        self.viewport = Viewport()
        self.ui.view_container = QWidget.createWindowContainer(self.viewport.scene)
        self.ui.viewport_layout.addWidget(self.ui.view_container)

        self.view_universes_tree = ViewUniversesTree()
        self.ui.universes_layout.addWidget(self.view_universes_tree.universes_tree_widget)

        self.view_materials_list = ViewMaterialsList()
        self.ui.materials_layout.addWidget(self.view_materials_list.materials_list_widget)

        self.view_surfaces_list = ViewSurfacesList()
        self.ui.surfaces_layout.addWidget(self.view_surfaces_list.surfaces_list_widget)

        self.view_material_properties = ViewMaterialProperties(self.ui.properties_layout)
        self.view_surface_properties = ViewSurfaceProperties(self.ui.properties_layout)
        self.view_universe_properties = ViewUniverseProperties(self.ui.properties_layout)

        self.view_surfaces_renderer = ViewRenderer()
        self.view_surfaces_renderer.set_scene(self.viewport.root_entity)

        self.view_input_data = ViewInputData(self.input_data_editor)

        self.project_data = ProjectData()
        self.project_data.load_views(self.view_universes_tree, self.view_materials_list, self.view_surfaces_list,
                                     self.view_material_properties, self.view_surface_properties,
                                     self.view_universe_properties,
                                     self.view_surfaces_renderer, self.view_input_data)

    def new_project(self):
        self.project_data.set_new()

    def save(self):
        self.project_data.save_data()

    def save_as(self):
        file_filter = 'JSON file (*.json)'
        response = QFileDialog.getSaveFileName(
            parent=self,
            caption='Select a data file',
            filter=file_filter
        )

        saved_file_directory = response[0]
        self.project_data.save_data_as_file(saved_file_directory)

    def load_file(self):
        file_filter = 'JSON file (*.json)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Open a project file',
            filter=file_filter
        )

        loaded_file_directory = response[0]
        self.project_data.load_data(loaded_file_directory)

    def open_code_editor(self):
        # self.project_data.write_input_data()
        self.ui.tab_main.addTab(self.input_data_editor, 'Input data')

    def open_plot(self):
        self.plot_widget.show()

    def run_simulation(self):
        os.system("echo Hello, world!")
        # os.system("gnome-terminal -e 'bash -c \"echo Hello, world!; exec bash\"'")
