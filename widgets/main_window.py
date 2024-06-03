import json

from PySide6.QtGui import QFont, QFontDatabase, QIcon
from PySide6.QtWidgets import QMainWindow, QWidget, QFileDialog, QPushButton, QMessageBox

from project_data.project_data import ProjectData
from project_data.project_state import ProjectState
from renderer.viewport import Viewport
from widgets.application_settings import ApplicationSettings
from widgets.input_data_editor import InputDataEditor
from ui_files.ui_main import Ui_MainWindow
from widgets.localization import Localization
from widgets.new_project_widget import NewProjectWidget
from widgets.new_project_window import NewProjectWindow
from widgets.settings_window import SettingsWindow
from widgets.start_widget import StartWidget
from widgets.start_window import StartWindow
from widgets.theme_settings import ThemeSettings


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.application_settings: ApplicationSettings = ApplicationSettings()
        self.theme_settings: ThemeSettings = ThemeSettings()

        with open('app_configs/MainConfig.json', 'r') as app_config:
            self.application_settings = ApplicationSettings(**json.load(app_config))

        with open(f'themes/{self.application_settings.theme_config}', 'r') as theme_config:
            self.theme_settings = ThemeSettings(**json.load(theme_config))

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Chamber Shape')
        self.setWindowIcon(QIcon('favicon.ico'))

        with open(f'styles/{self.theme_settings.qss_file}', 'r') as file:
            self.setStyleSheet(file.read())

        QFontDatabase.addApplicationFont('D:/Projects/chamber-shape/resources/fonts/Inter-Medium.ttf')
        font = QFont("Inter-Medium.ttf", 14)

        self.file_menu = self.ui.menubar.addMenu('Файл')
        new_project_action = self.file_menu.addAction('Новый Проект')
        new_project_action.triggered.connect(self.open_new_project_window)
        open_action = self.file_menu.addAction('Открыть')
        open_action.triggered.connect(self.open_project)
        save_action = self.file_menu.addAction('Сохранить')
        save_action.triggered.connect(self.save_project)
        save_as_action = self.file_menu.addAction('Сохранить Как')
        save_as_action.triggered.connect(self.save_project_to_new_directory)
        settings_action = self.file_menu.addAction('Параметры')
        settings_action.triggered.connect(self.open_settings_window)

        self.edit_menu = self.ui.menubar.addMenu('Редактировать')
        self.edit_menu.addAction('Вырезать')
        self.edit_menu.addAction('Копировать')
        self.edit_menu.addAction('Вставить')

        self.file_menu = self.ui.menubar.addMenu('Проект')
        run_simulation = self.file_menu.addAction('Запустить Расчет')
        run_simulation.triggered.connect(self.run_simulation)
        open_code = self.file_menu.addAction('Открыть Входные Данные')
        open_code.triggered.connect(self.open_code_editor)

        self.file_menu = self.ui.menubar.addMenu('Расчет')
        neutron_population = self.file_menu.addAction('Размножение Нейтронов')
        neutron_population.triggered.connect(self.open_calculation_parameters)
        boundary_conditions = self.file_menu.addAction('Граничные Условия')
        boundary_conditions.triggered.connect(self.open_calculation_parameters)
        energy_grid = self.file_menu.addAction('Энергетическая Сетка')
        energy_grid.triggered.connect(self.open_calculation_parameters)
        output = self.file_menu.addAction('Результаты')
        output.triggered.connect(self.open_calculation_output)

        self.file_menu = self.ui.menubar.addMenu('Помощь')
        manual = self.file_menu.addAction('Руководство')
        about = self.file_menu.addAction('О программе')

        self.start_window = StartWindow()
        self.start_window.set_main_window(self)
        self.start_widget = StartWidget()
        self.new_project_widget = NewProjectWidget()
        self.new_project_window = NewProjectWidget()
        self.settings_window = SettingsWindow()
        self.input_data_editor = InputDataEditor()

        self.viewport = Viewport()
        self.ui.view_container = QWidget.createWindowContainer(self.viewport.scene)
        self.ui.viewport_layout.addWidget(self.ui.view_container)
        self.viewport.scene.show()
        self.viewport.set_background_color(self.theme_settings.viewport_color)

        self.project_data = ProjectData()
        self.project_data.connect_models()
        self.project_data.connect_views()
        self.project_data.connect_view_models()
        self.project_data.set_main_window(self)

        self.ui.universes_layout.addWidget(self.project_data.views_data.universes_list_view.universes_list_widget)
        self.ui.materials_layout.addWidget(self.project_data.views_data.materials_list_view.materials_list_widget)
        self.ui.surfaces_layout.addWidget(self.project_data.views_data.surfaces_list_view.surfaces_list_widget)
        self.ui.cells_layout.addWidget(self.project_data.views_data.cells_list_view.cells_list_widget)
        self.ui.pins_layout.addWidget(self.project_data.views_data.pins_list_view.pins_list_widget)
        self.ui.lattices_layout.addWidget(self.project_data.views_data.lattices_list_view.lattices_list_widget)
        self.ui.detectors_layout.addWidget(self.project_data.views_data.detectors_list_view.detectors_list_widget)

        self.project_data.views_data.material_properties_view.attach_to_layout(self.ui.properties_layout)
        self.project_data.views_data.surface_properties_view.attach_to_layout(self.ui.properties_layout)
        self.project_data.views_data.cell_properties_view.attach_to_layout(self.ui.properties_layout)
        self.project_data.views_data.pin_properties_view.attach_to_layout(self.ui.properties_layout)
        self.project_data.views_data.lattice_properties_view.attach_to_layout(self.ui.properties_layout)
        self.project_data.views_data.detector_properties_view.attach_to_layout(self.ui.properties_layout)
        self.project_data.views_data.universe_properties_view.attach_to_layout(self.ui.properties_layout)
        self.project_data.views_data.calculation_parameters_properties_view.attach_to_layout(self.ui.properties_layout)
        self.project_data.views_data.output_data_properties_view.attach_to_layout(self.ui.properties_layout)

        self.project_data.views_data.surfaces_renderer_view.set_scene(self.viewport.root_entity)
        self.project_data.views_data.pin_renderer_view.set_scene(self.viewport.root_entity)

        self.project_data.views_data.input_data_view.attach_to_editor(self.input_data_editor)

        self.project_data.views_data.plot_view.set_tab_widget(self.ui.tab_main)
        self.project_data.views_data.plot_view.set_dark_style(self.theme_settings.dark_plot_style)

        if self.project_data.state == ProjectState.NOT_EXISTING.value:
            self.open_start_window()

    def open_start_window(self):
        self.start_window.show()
        self.start_window.vertical_layout.addWidget(self.start_widget)
        self.start_window.vertical_layout.addWidget(self.new_project_widget)
        self.new_project_widget.hide()
        with open(f'styles/{self.theme_settings.qss_file}', 'r') as file:
            self.start_window.setStyleSheet(file.read())
        self.start_widget.button_create_project.clicked.connect(self.show_new_project_widget)
        self.start_widget.button_open_project.clicked.connect(self.open_project)

    def create_new_project(self):
        project_settings = self.new_project_widget.get_data()
        self.project_data.set_new(project_settings)
        self.setWindowTitle(f'Chamber Shape - {self.project_data.settings.project_name}')
        self.start_window.hide()

    def create_new_project_from_window(self):
        project_settings = self.new_project_window.get_data()
        self.new_project_window.close()
        self.project_data.set_new(project_settings)
        self.setWindowTitle(f'Chamber Shape - {self.project_data.settings.project_name}')

    def show_new_project_widget(self):
        self.start_widget.hide()
        self.new_project_widget.show()
        self.new_project_widget.button_create_project.clicked.connect(self.create_new_project)
        self.new_project_widget.button_cancel.clicked.connect(self.back_to_start_widget)

    def back_to_start_widget(self):
        self.new_project_widget.hide()
        self.start_widget.show()
        self.start_widget.button_create_project.clicked.connect(self.show_new_project_widget)
        self.start_widget.button_open_project.clicked.connect(self.open_project)

    def open_new_project_window(self):
        self.new_project_window.show()
        with open(f'styles/{self.theme_settings.qss_file}', 'r') as file:
            self.new_project_window.setStyleSheet(file.read())
        self.new_project_widget.button_create_project.clicked.connect(self.create_new_project)
        self.new_project_widget.button_cancel.clicked.connect(self.new_project_window.close)

    def save_project(self):
        self.project_data.save()
        self.setWindowTitle(f'Chamber Shape - {self.project_data.settings.project_name}')

    def save_project_to_new_directory(self):
        response = QFileDialog.getExistingDirectory(
            parent=self,
            caption='Сохранить Проект в Новую Директорию'
        )

        self.project_data.save_to_new_directory(response)
        self.setWindowTitle(f'Chamber Shape - {self.project_data.settings.project_name}')

    def open_project(self):
        response = QFileDialog.getExistingDirectory(
            parent=self,
            caption='Открыть Проект'
        )

        self.project_data.load(response)
        self.setWindowTitle(f'Chamber Shape - {self.project_data.settings.project_name}')
        self.start_window.hide()

    def open_settings_window(self):
        self.settings_window.show()
        with open(f'styles/{self.theme_settings.qss_file}', 'r') as file:
            self.settings_window.setStyleSheet(file.read())
        self.settings_window.apply_button.clicked.connect(self.set_theme)

    def open_code_editor(self):
        self.ui.tab_main.addTab(self.input_data_editor, 'Входные Данные')

    def open_calculation_parameters(self):
        sender = self.sender().text()
        self.project_data.open_calculation_parameters(sender)

    def open_calculation_output(self):
        self.project_data.open_calculation_output()

    def run_simulation(self):
        self.project_data.run_simulation()

    def set_theme(self):
        theme_names_map: dict = {
            'Светлая': 'Light.json',
            'Темная': 'Dark.json'
        }
        app_theme = self.settings_window.get_data()
        app_theme_config = theme_names_map[app_theme]
        self.application_settings.theme_config = app_theme_config

        with open(f'themes/{self.application_settings.theme_config}', 'r') as theme_config:
            self.theme_settings = ThemeSettings(**json.load(theme_config))

        with open(f'styles/{self.theme_settings.qss_file}', 'r') as file:
            self.setStyleSheet(file.read())

        self.viewport.set_background_color(self.theme_settings.viewport_color)

        self.project_data.views_data.plot_view.set_dark_style(self.theme_settings.dark_plot_style)

    def set_not_saved_title(self):
        self.setWindowTitle(f'Chamber Shape - {self.project_data.settings.project_name}*')

    def save_app_configs(self):
        with open('app_configs/MainConfig.json', 'w') as app_config:
            json.dump(self.application_settings.__dict__, app_config, indent=4)

        with open(f'themes/{self.application_settings.theme_config}', 'w') as theme_config:
            json.dump(self.theme_settings.__dict__, theme_config, indent=4)

    def closeEvent(self, event):
        if self.project_data.state != ProjectState.NOT_SAVED.value:
            self.save_app_configs()
            event.accept()
            return

        reply = QMessageBox.question(self, 'Выйти из Chamber Shape', 'Вы хотите сохранить изменения?',
                                     QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Save)

        if reply == QMessageBox.Save:
            self.save_project()
            self.save_app_configs()
            event.accept()
        elif reply == QMessageBox.Discard:
            self.save_app_configs()
            event.accept()
        else:
            event.ignore()
