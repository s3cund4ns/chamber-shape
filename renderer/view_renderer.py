from renderer.entities.surface_entity import SurfaceEntity
from renderer.mesh_creator import create_mesh
from widgets.view import View


class ViewRenderer(View):
    def __init__(self):
        super().__init__()
        self.scene = None
        self.surface_renders: list[SurfaceEntity] = []

    def set_scene(self, scene):
        self.scene = scene

    def add_item(self, *args):
        index, item_text, item = args
        surface_render = create_mesh(item_text, self.scene)
        self.surface_renders.append(surface_render)

    def select_item(self, *args):
        pass

    def change_item(self, index, value):
        self.surface_renders[index].set_data(value)

    def delete_item(self, index):
        self.surface_renders[index].removeComponent(self.surface_renders[index].mesh)
        self.surface_renders[index].removeComponent(self.surface_renders[index].material)
        self.surface_renders[index].removeComponent(self.surface_renders[index].transform)
        del self.surface_renders[index]

