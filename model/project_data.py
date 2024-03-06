from model.model_materials_list import ModelMaterialsList
from model.model_surfaces_list import ModelSurfacesList
from model.model_universes_tree import ModelUniversesTree
from model.view_model import ViewModel
from model.view_model_materials_list import ViewModelMaterialsList
from model.view_model_properties import ViewModelProperties
from model.view_model_surfaces_list import ViewModelSurfacesList
from model.view_model_universes_tree import ViewModelUniversesTree
from widgets.view import View


class ProjectData:
    def __init__(self):
        self.universes_model: ModelUniversesTree = ModelUniversesTree()
        self.materials_model: ModelMaterialsList = ModelMaterialsList()
        self.surfaces_model: ModelSurfacesList = ModelSurfacesList()

        self.universes_view_model: ViewModelUniversesTree = ViewModelUniversesTree()
        self.materials_view_model: ViewModelMaterialsList = ViewModelMaterialsList()
        self.surfaces_view_model: ViewModelSurfacesList = ViewModelSurfacesList()

        self.universes_view_model.add_model(self.universes_model)
        self.materials_view_model.add_model(self.materials_model)
        self.surfaces_view_model.add_model(self.surfaces_model)

    def load_views(self, *args: View):
        (universes_view, materials_view, surfaces_view, material_properties_view,
         surface_properties_view, surfaces_renderer_view) = args
        self.universes_view_model.add_view(universes_view)
        self.materials_view_model.add_view(materials_view)
        self.surfaces_view_model.add_view(surfaces_view)
        self.materials_view_model.add_view(material_properties_view)
        self.surfaces_view_model.add_view(surface_properties_view)
        self.surfaces_view_model.add_view(surfaces_renderer_view)


