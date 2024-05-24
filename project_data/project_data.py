import json
import os

from project_data.models_data import ModelsData
from project_data.project_settings import ProjectSettings
from project_data.project_state import ProjectState
from project_data.view_models_data import ViewModelsData
from project_data.views_data import ViewsData
from solvers.solver import Solver
from solvers.solver_creator import create_solver

PROJECTS_DIRECTORY = 'Projects/'


class ProjectData:
    def __init__(self):
        self.state: int = ProjectState.NOT_EXISTING.value
        self.settings: ProjectSettings = ProjectSettings()
        self.solver = None
        self.models_data: ModelsData = ModelsData()
        self.view_models_data: ViewModelsData = ViewModelsData()
        self.views_data: ViewsData = ViewsData()
        self.projects_directory: str = PROJECTS_DIRECTORY
        self.project_name: str = ''

    def connect_models(self):
        self.view_models_data.universes_view_model.add_model(self.models_data.universes_model)
        self.view_models_data.materials_view_model.add_model(self.models_data.materials_model)
        self.view_models_data.surfaces_view_model.add_model(self.models_data.surfaces_model)
        self.view_models_data.cells_view_model.add_model(self.models_data.cells_model)
        self.view_models_data.pins_view_model.add_model(self.models_data.pins_model)
        self.view_models_data.lattices_view_model.add_model(self.models_data.lattices_model)
        self.view_models_data.detectors_view_model.add_model(self.models_data.detectors_model)
        self.view_models_data.calculation_parameters_view_model.add_model(self.models_data.calculation_parameters_model)
        self.view_models_data.input_data_view_model.add_model(self.models_data.input_data_model)
        self.view_models_data.output_data_view_model.add_model(self.models_data.output_data_model)

    def connect_views(self):
        self.view_models_data.universes_view_model.add_view(self.views_data.universes_list_view)
        self.view_models_data.materials_view_model.add_view(self.views_data.materials_list_view)
        self.view_models_data.surfaces_view_model.add_view(self.views_data.surfaces_list_view)
        self.view_models_data.cells_view_model.add_view(self.views_data.cells_list_view)
        self.view_models_data.pins_view_model.add_view(self.views_data.pins_list_view)
        self.view_models_data.lattices_view_model.add_view(self.views_data.lattices_list_view)
        self.view_models_data.detectors_view_model.add_view(self.views_data.detectors_list_view)
        self.view_models_data.materials_view_model.add_view(self.views_data.material_properties_view)
        self.view_models_data.surfaces_view_model.add_view(self.views_data.surface_properties_view)
        self.view_models_data.cells_view_model.add_view(self.views_data.cell_properties_view)
        self.view_models_data.pins_view_model.add_view(self.views_data.pin_properties_view)
        self.view_models_data.lattices_view_model.add_view(self.views_data.lattice_properties_view)
        self.view_models_data.detectors_view_model.add_view(self.views_data.detector_properties_view)
        self.view_models_data.universes_view_model.add_view(self.views_data.universe_properties_view)
        self.view_models_data.calculation_parameters_view_model.add_view(
            self.views_data.calculation_parameters_properties_view
        )
        self.view_models_data.output_data_view_model.add_view(self.views_data.output_data_properties_view)
        self.view_models_data.output_data_view_model.add_view(self.views_data.plot_view)
        self.view_models_data.surfaces_view_model.add_view(self.views_data.surfaces_renderer_view)
        self.view_models_data.pins_view_model.add_view(self.views_data.pin_renderer_view)
        self.view_models_data.lattices_view_model.add_view(self.views_data.lattice_renderer_view)
        self.view_models_data.input_data_view_model.add_view(self.views_data.input_data_view)

    def create_project_directory(self):
        name = self.settings.project_name
        directory = self.settings.project_directory
        full_directory = f'{directory}/{name}'
        os.mkdir(full_directory)
        self.settings.project_directory = full_directory

    def create_calculation_data_directory(self):
        solver_name = self.settings.solver
        self.settings.calculation_data_directory = f'{self.settings.project_directory}/{solver_name}'
        os.mkdir(self.settings.calculation_data_directory)

    def initialize_solver(self):
        self.solver: Solver = create_solver(self.settings.solver, self.settings.solver_directory,
                                            self.settings.calculation_data_directory)
        self.solver.load_tokens()
        self.solver.load_nuclear_data(f'D:/Projects/chamber-shape/nuclear_data/'
                                      f'{self.settings.nuclear_data_library}.json')
        self.solver.create_input_data_file(self.settings.project_name)

    def set_basic_input_data(self):
        self.models_data.input_data_model.update_basic_data((self.settings.project_name,
                                                 self.solver.nuclear_data.__dict__,
                                                 self.replace_disk_letter_with_mnt(
                                                     self.settings.nuclear_data_library_directory)))

    def save_settings(self):
        with open(f'{self.settings.project_directory}/SettingsConfig.json', 'w') as settings_file:
            json.dump(self.settings.__dict__, settings_file, indent=4)

    def save_objects(self):
        universes_data = self.models_data.universes_model.dump_data()
        materials_data = self.models_data.materials_model.dump_data()
        surfaces_data = self.models_data.surfaces_model.dump_data()
        cells_data = self.models_data.cells_model.dump_data()
        pins_data = self.models_data.pins_model.dump_data()
        lattices_data = self.models_data.lattices_model.dump_data()
        calculation_parameters_data = self.models_data.calculation_parameters_model.dump_data()
        detectors_data = self.models_data.detectors_model.dump_data()
        data = {
            'Universes': universes_data,
            'Materials': materials_data,
            'Surfaces': surfaces_data,
            'Cells': cells_data,
            'Pins': pins_data,
            'Lattices': lattices_data,
            'Calculation parameters': calculation_parameters_data,
            'Detectors': detectors_data
                }

        with open(f'{self.settings.project_directory}/ObjectsConfig.json', 'w') as objects_file:
            json.dump(data, objects_file, indent=4)

    def save_input_data(self):
        self.solver.save_input_data_file(self.settings.project_name, self.models_data.input_data_model.data)

    def set_new(self, settings: dict):
        self.settings = ProjectSettings(**settings)
        self.create_project_directory()
        self.create_calculation_data_directory()
        self.initialize_solver()
        self.clear_data_in_models()
        self.models_data.input_data_model.create_input_data_generator(self.settings.solver)
        self.models_data.output_data_model.create_output_data_writer(self.settings.solver,
                                                                     self.settings.calculation_data_directory)
        self.set_basic_input_data()
        self.save_settings()
        self.save_objects()
        self.state = ProjectState.EXISTING.value

    def save(self):
        self.save_settings()
        self.save_objects()
        self.save_input_data()

    def save_to_new_directory(self, path: str):
        temp_directory = self.settings.project_directory
        self.settings.project_directory = path
        self.create_project_directory()
        self.create_calculation_data_directory()
        self.initialize_solver()
        self.save()
        self.settings.project_directory = temp_directory

    def load_settings(self, path: str):
        with open(f'{path}/SettingsConfig.json', 'r') as settings_file:
            self.settings = ProjectSettings(**json.load(settings_file))

    def load_objects(self, path: str):
        with open(f'{path}/ObjectsConfig.json', 'r') as objects_file:
            data = json.load(objects_file)
            self.models_data.universes_model.load_data(data['Universes'])
            self.models_data.materials_model.load_data(data['Materials'])
            self.models_data.surfaces_model.load_data(data['Surfaces'])
            self.models_data.cells_model.load_data(data['Cells'])
            self.models_data.pins_model.load_data(data['Pins'])
            self.models_data.lattices_model.load_data(data['Lattices'])
            self.models_data.calculation_parameters_model.load_data(data['Calculation parameters'])
            self.models_data.detectors_model.load_data(data['Detectors'])

    def load(self, path: str):
        self.load_settings(path)
        self.initialize_solver()
        self.clear_data_in_models()
        self.models_data.input_data_model.create_input_data_generator(self.settings.solver)
        self.models_data.output_data_model.create_output_data_writer(self.settings.solver,
                                                                     self.settings.calculation_data_directory)
        self.set_basic_input_data()
        self.load_objects(path)
        self.state = ProjectState.EXISTING.value

    def clear_data_in_models(self):
        self.models_data.universes_model.clear_data()
        self.models_data.materials_model.clear_data()
        self.models_data.surfaces_model.clear_data()

    def write_input_data(self):
        self.models_data.input_data_model.add_item(
            self.models_data.materials_model.get_input_data(),
            self.models_data.surfaces_model.get_input_data()
        )
        self.models_data.input_data_model.write_to_file()

    def open_calculation_parameters(self, parameter_type: str):
        self.view_models_data.calculation_parameters_view_model.select_item_in_models(parameter_type)

    def open_calculation_output(self):
        self.view_models_data.output_data_view_model.select_calculation_output_in_model()

    def run_simulation(self):
        self.save_input_data()
        self.solver.start_calculation(self.settings.project_name)

    def open_plot(self):
        self.view_models_data.output_data_view_model.get_plot_info_from_model()

    @staticmethod
    def replace_disk_letter_with_mnt(file_path):
        drive_letter, rest_of_path = os.path.splitdrive(file_path)
        mnt_path = "/mnt/" + drive_letter[0].lower() + rest_of_path
        return mnt_path
