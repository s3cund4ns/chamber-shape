import json

from models.model_materials_list import ModelMaterialsList
from models.model_detectors_list import ModelDetectorsList
from models.model_surfaces_list import ModelSurfacesList
from models.model_universes_tree import ModelUniversesTree
from project_data.view import View
from viewmodels.view_model_materials_list import ViewModelMaterialsList
from viewmodels.view_model_detectors_list import ViewModelDetectorsList
from viewmodels.view_model_surfaces_list import ViewModelSurfacesList
from viewmodels.view_model_universes_tree import ViewModelUniversesTree

PROJECTS_DIRECTORY = 'Projects/'


class ProjectData:
    def __init__(self):
        self.projects_directory: str = PROJECTS_DIRECTORY
        self.project_name: str = ''

        self.universes_model: ModelUniversesTree = ModelUniversesTree()
        self.materials_model: ModelMaterialsList = ModelMaterialsList()
        self.detectors_model: ModelDetectorsList = ModelDetectorsList()
        self.surfaces_model: ModelSurfacesList = ModelSurfacesList()

        self.universes_view_model: ViewModelUniversesTree = ViewModelUniversesTree()
        self.materials_view_model: ViewModelMaterialsList = ViewModelMaterialsList()
        self.detectors_view_model: ViewModelDetectorsList = ViewModelDetectorsList()
        self.surfaces_view_model: ViewModelSurfacesList = ViewModelSurfacesList()

        self.universes_view_model.add_model(self.universes_model)
        self.materials_view_model.add_model(self.materials_model)
        self.detectors_view_model.add_model(self.detectors_model)
        self.surfaces_view_model.add_model(self.surfaces_model)

    def load_views(self, *args: View):
        (universes_view, materials_view, detectors_view, surfaces_view, material_properties_view,
         detectors_properties_view, surface_properties_view, universe_properties_view, surfaces_renderer_view) = args
        self.universes_view_model.add_view(universes_view)
        self.materials_view_model.add_view(materials_view)
        self.detectors_view_model.add_view(detectors_view)
        self.surfaces_view_model.add_view(surfaces_view)
        self.materials_view_model.add_view(material_properties_view)
        self.detectors_view_model.add_view(detectors_properties_view)
        self.surfaces_view_model.add_view(surface_properties_view)
        self.universes_view_model.add_view(universe_properties_view)
        self.surfaces_view_model.add_view(surfaces_renderer_view)

    def save_data(self, project_name):
        if self.project_name == '':
            with open(project_name, 'w+') as file:
                file.write('')

            self.project_name = project_name

        data = json.dumps(self.materials_model, indent=4)
        print(data)



