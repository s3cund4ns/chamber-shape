from renderer.entities.surface_entity import SurfaceEntity
from renderer.entities.entity_creator import create_entity
from project_data.view import View


class ViewSurfaceRenderer(View):
    def __init__(self):
        super().__init__()
        self.scene = None
        self.surface_renders: list[SurfaceEntity] = []

    def set_scene(self, scene):
        self.scene = scene

    def add_item(self, *args):
        index, item_text, item = args
        item_text = item_text.split()[0]
        surface_render = create_entity(item_text, self.scene)
        self.surface_renders.append(surface_render)

    def select_item(self, *args):
        pass

    def change_item(self, index, value, item_text):
        self.surface_renders[index].set_data(value)

    def delete_render_components(self, index):
        self.surface_renders[index].removeComponent(self.surface_renders[index].mesh)
        self.surface_renders[index].removeComponent(self.surface_renders[index].material)
        self.surface_renders[index].removeComponent(self.surface_renders[index].transform)

    def delete_item(self, index):
        self.delete_render_components(index)
        del self.surface_renders[index]

    def clear(self):
        for index in range(len(self.surface_renders)):
            self.delete_render_components(index)
        self.surface_renders.clear()

