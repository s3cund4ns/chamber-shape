from renderer.entities.line_entity import LineEntity
from renderer.entities.surface_entity import SurfaceEntity
from renderer.mesh_creator import create_mesh
from project_data.view import View


class ViewLatticeRenderer(View):
    def __init__(self):
        super().__init__()
        self.scene = None
        self.lattice_renders: list = []

    def set_scene(self, scene):
        self.scene = scene

    def add_item(self, *args):
        parent, item_text, item = args
        if item.get_type != 'Lattice':
            return
        lattice_size = item.get_size()
        x_number, y_number = lattice_size[0], lattice_size[1]
        lattice_pitch = item.get_pitch()
        vertical_lines_render = LineEntity(0, self.scene)
        vertical_lines_render.add_vertices(y_number, x_number, lattice_pitch)
        vertical_lines_render.set_geometry()
        vertical_lines_render.add_components()
        horizontal_lines_render = LineEntity(1, self.scene)
        horizontal_lines_render.add_vertices(y_number, x_number, lattice_pitch)
        horizontal_lines_render.set_geometry()
        horizontal_lines_render.add_components()

    def select_item(self, *args):
        pass

    def change_item(self, index, value, item_text):
        pass

    def delete_render_components(self, index):
        pass

    def delete_item(self, index):
        pass

    def clear(self):
        pass
