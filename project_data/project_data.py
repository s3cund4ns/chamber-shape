import json
import os

from models.model_calculation_parameters import ModelCalculationParameters
from models.model_detectors_list import ModelDetectorsList
from models.model_materials_list import ModelMaterialsList
from models.model_surfaces_list import ModelSurfacesList
from models.model_universes_tree import ModelUniversesTree
from models.model_input_data import ModelInputData
from project_data.project_settings import ProjectSettings
from project_data.project_state import ProjectState
from solvers.solver import Solver
from solvers.solver_creator import create_solver
from solvers.solver_loader import load_serpent
from project_data.view import View
from viewmodels.view_model_calculation_parameters import ViewModelCalculationParameters
from viewmodels.view_model_detectors_list import ViewModelDetectorsList
from viewmodels.view_model_input_data import ViewModelInputData
from viewmodels.view_model_materials_list import ViewModelMaterialsList
from viewmodels.view_model_surfaces_list import ViewModelSurfacesList
from viewmodels.view_model_universes_tree import ViewModelUniversesTree

PROJECTS_DIRECTORY = 'Projects/'


class ProjectData:
    def __init__(self):
        self.state: int = ProjectState.NOT_EXISTING.value
        self.settings: ProjectSettings = ProjectSettings()
        self.solver = None
        self.projects_directory: str = PROJECTS_DIRECTORY
        self.project_name: str = ''

        self.universes_model: ModelUniversesTree = ModelUniversesTree()
        self.materials_model: ModelMaterialsList = ModelMaterialsList()
        self.surfaces_model: ModelSurfacesList = ModelSurfacesList()
        self.detectors_model: ModelDetectorsList = ModelDetectorsList()
        self.calculation_parameters_model: ModelCalculationParameters = ModelCalculationParameters()
        self.input_data_model: ModelInputData = ModelInputData()

        self.universes_model.materials_model = self.materials_model
        self.universes_model.surfaces_model = self.surfaces_model

        self.detectors_model.materials_model = self.materials_model
        self.detectors_model.universes_model = self.universes_model

        self.materials_model.input_data_model = self.input_data_model
        self.surfaces_model.input_data_model = self.input_data_model
        self.universes_model.input_data_model = self.input_data_model

        self.universes_view_model: ViewModelUniversesTree = ViewModelUniversesTree()
        self.materials_view_model: ViewModelMaterialsList = ViewModelMaterialsList()
        self.surfaces_view_model: ViewModelSurfacesList = ViewModelSurfacesList()
        self.detectors_view_model: ViewModelDetectorsList = ViewModelDetectorsList()
        self.calculation_parameters_view_model: ViewModelCalculationParameters = ViewModelCalculationParameters()
        self.input_data_view_model: ViewModelInputData = ViewModelInputData()

        self.universes_view_model.add_model(self.universes_model)
        self.materials_view_model.add_model(self.materials_model)
        self.surfaces_view_model.add_model(self.surfaces_model)
        self.detectors_view_model.add_model(self.detectors_model)
        self.calculation_parameters_view_model.add_model(self.calculation_parameters_model)
        self.input_data_view_model.add_model(self.input_data_model)

    def load_views(self, *args: View):
        (universes_view, materials_view, surfaces_view, detectors_view, material_properties_view,
         surface_properties_view, detector_properties_view,
         universe_properties_view, calculation_parameters_properties_view, surfaces_renderer_view, input_data_view) = args
        self.universes_view_model.add_view(universes_view)
        self.materials_view_model.add_view(materials_view)
        self.surfaces_view_model.add_view(surfaces_view)
        self.detectors_view_model.add_view(detectors_view)
        self.materials_view_model.add_view(material_properties_view)
        self.surfaces_view_model.add_view(surface_properties_view)
        self.detectors_view_model.add_view(detector_properties_view)
        self.universes_view_model.add_view(universe_properties_view)
        self.calculation_parameters_view_model.add_view(calculation_parameters_properties_view)
        self.surfaces_view_model.add_view(surfaces_renderer_view)
        self.input_data_view_model.add_view(input_data_view)

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
        self.input_data_model.update_basic_data((self.settings.project_name,
                                                 self.solver.nuclear_data.__dict__,
                                                 self.replace_disk_letter_with_mnt(
                                                     self.settings.nuclear_data_library_directory)))

    def save_settings(self):
        with open(f'{self.settings.project_directory}/SettingsConfig.json', 'w') as settings_file:
            json.dump(self.settings.__dict__, settings_file, indent=4)

    def save_objects(self):
        materials_data = self.materials_model.dump_data()
        surfaces_data = self.surfaces_model.dump_data()
        universes_data = self.universes_model.dump_data()
        data = {'Materials': materials_data,
                'Surfaces': surfaces_data,
                'Universes': universes_data}

        with open(f'{self.settings.project_directory}/ObjectsConfig.json', 'w') as objects_file:
            json.dump(data, objects_file, indent=4)

    def save_input_data(self):
        self.solver.save_input_data_file(self.settings.project_name, self.input_data_model.data)

    def set_new(self, settings: dict):
        self.settings = ProjectSettings(**settings)
        self.create_project_directory()
        self.create_calculation_data_directory()
        self.initialize_solver()
        self.clear_data_in_models()
        self.input_data_model.create_input_data_generator(self.settings.solver)
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
            self.materials_model.load_data(data['Materials'])
            self.surfaces_model.load_data(data['Surfaces'])

    def load(self, path: str):
        self.load_settings(path)
        self.initialize_solver()
        self.clear_data_in_models()
        self.input_data_model.create_input_data_generator(self.settings.solver)
        self.set_basic_input_data()
        self.load_objects(path)
        self.state = ProjectState.EXISTING.value

    def clear_data_in_models(self):
        self.universes_model.clear_data()
        self.materials_model.clear_data()
        self.surfaces_model.clear_data()

    def write_input_data(self):
        self.input_data_model.add_item(self.materials_model.get_input_data(), self.surfaces_model.get_input_data())
        self.input_data_model.write_to_file()

    def open_calculation_parameters(self, parameter_type: str):
        self.calculation_parameters_view_model.select_item_in_models(parameter_type)

    def run_simulation(self):
        self.save_input_data()
        self.solver.start_calculation(self.settings.project_name)

    @staticmethod
    def replace_disk_letter_with_mnt(file_path):
        drive_letter, rest_of_path = os.path.splitdrive(file_path)
        mnt_path = "/mnt/" + drive_letter[0].lower() + rest_of_path
        return mnt_path
