import json

from models.model_materials_list import ModelMaterialsList
from models.model_surfaces_list import ModelSurfacesList
from models.model_universes_tree import ModelUniversesTree
from models.model_input_data import ModelInputData
from project_data.view import View
from viewmodels.view_model_input_data import ViewModelInputData
from viewmodels.view_model_materials_list import ViewModelMaterialsList
from viewmodels.view_model_surfaces_list import ViewModelSurfacesList
from viewmodels.view_model_universes_tree import ViewModelUniversesTree

PROJECTS_DIRECTORY = 'Projects/'


class ProjectData:
    def __init__(self):
        self.projects_directory: str = PROJECTS_DIRECTORY
        self.project_name: str = ''

        self.universes_model: ModelUniversesTree = ModelUniversesTree()
        self.materials_model: ModelMaterialsList = ModelMaterialsList()
        self.surfaces_model: ModelSurfacesList = ModelSurfacesList()
        self.input_data_model: ModelInputData = ModelInputData()

        self.universes_model.materials_model = self.materials_model
        self.universes_model.surfaces_model = self.surfaces_model

        self.materials_model.input_data_model = self.input_data_model
        self.surfaces_model.input_data_model = self.input_data_model
        self.universes_model.input_data_model = self.input_data_model

        self.universes_view_model: ViewModelUniversesTree = ViewModelUniversesTree()
        self.materials_view_model: ViewModelMaterialsList = ViewModelMaterialsList()
        self.surfaces_view_model: ViewModelSurfacesList = ViewModelSurfacesList()
        self.input_data_view_model: ViewModelInputData = ViewModelInputData()

        self.universes_view_model.add_model(self.universes_model)
        self.materials_view_model.add_model(self.materials_model)
        self.surfaces_view_model.add_model(self.surfaces_model)
        self.input_data_view_model.add_model(self.input_data_model)

    def load_views(self, *args: View):
        (universes_view, materials_view, surfaces_view, material_properties_view,
         surface_properties_view, universe_properties_view, surfaces_renderer_view, input_data_view) = args
        self.universes_view_model.add_view(universes_view)
        self.materials_view_model.add_view(materials_view)
        self.surfaces_view_model.add_view(surfaces_view)
        self.materials_view_model.add_view(material_properties_view)
        self.surfaces_view_model.add_view(surface_properties_view)
        self.universes_view_model.add_view(universe_properties_view)
        self.surfaces_view_model.add_view(surfaces_renderer_view)
        self.input_data_view_model.add_view(input_data_view)

    def set_new(self):
        self.project_name = ''
        self.clear_data_in_models()

    def save_data_as_file(self, project_name):
        if self.project_name == '':
            with open(project_name, 'w+') as file:
                file.write('')

            self.project_name = project_name

            self.save_data()

    def save_data(self):
        materials_data = self.materials_model.dump_data()
        surfaces_data = self.surfaces_model.dump_data()
        universes_data = self.universes_model.dump_data()
        data = {'Materials': materials_data,
                'Surfaces': surfaces_data,
                'Universes': universes_data}

        with open(self.project_name, 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(self, project_name):
        with open(project_name, 'r') as file:
            self.project_name = project_name
            data = json.load(file)
            self.clear_data_in_models()
            self.materials_model.load_data(data['Materials'])
            self.surfaces_model.load_data(data['Surfaces'])

    def clear_data_in_models(self):
        self.universes_model.clear_data()
        self.materials_model.clear_data()
        self.surfaces_model.clear_data()

    def write_input_data(self):
        self.input_data_model.add_item(self.materials_model.get_input_data(), self.surfaces_model.get_input_data())
        self.input_data_model.write_to_file()




