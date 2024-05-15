from PySide6.QtGui import QRgba64

from renderer.entities.surface_entity import SurfaceEntity
from project_data.view import View


class ViewCellRenderer(View):
    def __init__(self):
        super().__init__()
        self.scene = None
        self.surface_renderer = None
        self.cells: list[str] = []
        self.surface_groups: list[list[SurfaceEntity]] = []
        self.selected_group_index: int = -1

    def set_scene(self, scene):
        self.scene = scene

    def add_item(self, key, item_text, item):
        self.cells.append(item)
        self.surface_groups.append([])

    def select_item(self, index, value):
        self.selected_group_index = self.cells.index(str(value[0]))

    def change_item(self, value):
        print(value)
        name, item_value = value
        if name == 'Add':
            index = item_value[0]
            self.surface_groups[self.selected_group_index].append(self.surface_renderer.surface_renders[index])
        if name == 'Color':
            red, green, blue = item_value
            surface_group: list[SurfaceEntity] = self.surface_groups[self.selected_group_index]
            for surface in surface_group:
                surface.material.setAmbient(QRgba64.fromRgba(red, green, blue, 255))

    def delete_render_components(self, index):
        pass

    def delete_item(self, index):
        pass

    def clear(self):
        pass
