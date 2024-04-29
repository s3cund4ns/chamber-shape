from PySide6.QtGui import QFont, QFontDatabase, QIcon
from PySide6.QtWidgets import QMainWindow, QWidget, QFileDialog

from project_data.project_data import ProjectData
from project_data.project_state import ProjectState
from renderer.view_renderer import ViewRenderer
from renderer.viewport import Viewport
from widgets.input_data_editor import InputDataEditor
from ui_files.ui_main import Ui_MainWindow
from widgets.new_project import NewProject
from widgets.settings_window import SettingsWindow
from widgets.start_window import StartWindow
from widgets.view_detectors_list import ViewDetectorsList
from widgets.view_input_data import ViewInputData

from widgets.view_materials_list import ViewMaterialsList
from widgets.view_properties import ViewSurfaceProperties, ViewMaterialProperties, ViewUniverseProperties, \
    ViewDetectorProperties, ViewCalculationParametersProperties
from widgets.view_surfaces_list import ViewSurfacesList
from widgets.view_universes_tree import ViewUniversesTree


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Chamber Shape')
        self.setWindowIcon(QIcon('favicon.ico'))

        with open('styles/light.qss', 'r') as file:
            self.setStyleSheet(file.read())

        QFontDatabase.addApplicationFont('../resources/fonts/Inter-Medium.ttf')
        font = QFont("Inter-Medium.ttf", 14)

        # self.plot_widget = PlotWidget()

        self.file_menu = self.ui.menubar.addMenu('File')
        new_project_action = self.file_menu.addAction('New project')
        new_project_action.triggered.connect(self.open_new_project_window)
        open_action = self.file_menu.addAction('Open')
        open_action.triggered.connect(self.open_project)
        save_action = self.file_menu.addAction('Save')
        save_action.triggered.connect(self.save_project)
        save_as_action = self.file_menu.addAction('Save as')
        save_as_action.triggered.connect(self.save_project_to_new_directory)
        settings_action = self.file_menu.addAction('Settings')
        settings_action.triggered.connect(self.open_settings_window)

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

        self.file_menu = self.ui.menubar.addMenu('Calculation')
        neutron_population = self.file_menu.addAction('Neutron population')
        neutron_population.triggered.connect(self.open_calculation_parameters)
        boundary_conditions = self.file_menu.addAction('Boundary conditions')
        boundary_conditions.triggered.connect(self.open_calculation_parameters)

        self.start_window = StartWindow()
        self.new_project_window = NewProject()
        self.settings_window = SettingsWindow()

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

        self.view_detectors_list = ViewDetectorsList()
        self.ui.detectors_layout.addWidget(self.view_detectors_list.detectors_list_widget)

        self.view_material_properties = ViewMaterialProperties(self.ui.properties_layout)
        self.view_surface_properties = ViewSurfaceProperties(self.ui.properties_layout)
        self.view_detector_properties = ViewDetectorProperties(self.ui.properties_layout)
        self.view_universe_properties = ViewUniverseProperties(self.ui.properties_layout)
        self.view_calculation_parameters_properties = ViewCalculationParametersProperties(self.ui.properties_layout)

        self.view_surfaces_renderer = ViewRenderer()
        self.view_surfaces_renderer.set_scene(self.viewport.root_entity)

        self.view_input_data = ViewInputData(self.input_data_editor)

        self.project_data = ProjectData()
        self.project_data.load_views(self.view_universes_tree, self.view_materials_list, self.view_surfaces_list,
                                     self.view_detectors_list,
                                     self.view_material_properties, self.view_surface_properties, self.view_detector_properties,
                                     self.view_universe_properties, self.view_calculation_parameters_properties,
                                     self.view_surfaces_renderer, self.view_input_data)

        if self.project_data.state == ProjectState.NOT_EXISTING.value:
            self.open_start_window()

    def open_start_window(self):
        self.start_window.show()
        self.start_window.button_create_project.clicked.connect(self.open_new_project_window)
        self.start_window.button_open_project.clicked.connect(self.open_project)

    def create_new_project(self):
        project_settings = self.new_project_window.get_data()
        self.new_project_window.close()
        self.project_data.set_new(project_settings)
        self.setWindowTitle(f'Chamber Shape - {self.project_data.settings.project_name}')

    def open_new_project_window(self):
        self.new_project_window.show()
        self.new_project_window.button_create_project.clicked.connect(self.create_new_project)

    def save_project(self):
        self.project_data.save()

    def save_project_to_new_directory(self):
        response = QFileDialog.getExistingDirectory(
            parent=self,
            caption='Save project to a new directory'
        )

        self.project_data.save_to_new_directory(response)

    def open_project(self):
        response = QFileDialog.getExistingDirectory(
            parent=self,
            caption='Open a project'
        )

        self.project_data.load(response)
        self.setWindowTitle(f'Chamber Shape - {self.project_data.settings.project_name}')

    def open_settings_window(self):
        self.settings_window.show()

    def open_code_editor(self):
        # self.project_data.write_input_data()
        self.ui.tab_main.addTab(self.input_data_editor, 'Input data')

    def open_plot(self):
        self.plot_widget.show()

    def open_calculation_parameters(self):
        sender = self.sender().text()
        self.project_data.open_calculation_parameters(sender)

    def run_simulation(self):
        self.project_data.run_simulation()
