import numpy as np
from PySide6.QtGui import QRgba64, QVector3D

from cshape_objects.lattices.lattice import Lattice
from project_data.view import View
from renderer.views.view_pin_renderer import ViewPinRenderer


class ViewLatticeRenderer(View):
    def __init__(self):
        super().__init__()
        self.pin_renderer_view: ViewPinRenderer | None = None
        self.lattice_renders: list = []
        self.selected_render_index: int = -1

    def add_item(self, index, item_text, item: Lattice):
        lattice_size: list[int] = item.get_size()
        rows, columns = lattice_size
        lattice_matrix: list[list] = [[None for column in range(columns)] for row in range(rows)]
        self.lattice_renders.append([item, lattice_matrix])

    def set_transforms(self):
        for cylinder_entity in self.pin_render:
            z_pos = float(self.pin_render.index(cylinder_entity)) * -0.1
            cylinder_entity.transform.setTranslation(QVector3D(0.0, 0.0, z_pos))

    def select_item(self, index, item):
        self.selected_render_index = index

    def change_item(self, index, value, item_text):
        property_name, property_value = value
        if property_name == 'Universe Matrix':
            matrix_index, universe_number = property_value
            row, column = matrix_index
            lattice: Lattice = self.lattice_renders[index][0]
            lattice_position = list(np.array(lattice.get_position(), dtype=float))
            lattice_pitch = lattice.get_pitch()
            universe_pos_x, universe_pos_y = (
                lattice_position[0] + lattice_pitch * row, lattice_position[1] + lattice_pitch * column)
            self.lattice_renders[index][1][row][column] = (
                self.pin_renderer_view.create_instance(int(universe_number), universe_pos_x, universe_pos_y)
            )
        if property_name == 'Position':
            pos_x, pos_y = property_value
            universe_matrix = self.lattice_renders[index][1]
            for row in range(len(universe_matrix)):
                for column in range(len(universe_matrix[row])):
                    self.pin_renderer_view.change_instance_position(universe_matrix[row][column], pos_x, pos_y)


    def delete_render_components(self):
        for cylinder_entity in self.pin_render:
            cylinder_entity.removeComponent(cylinder_entity.mesh)
            cylinder_entity.removeComponent(cylinder_entity.material)
            cylinder_entity.removeComponent(cylinder_entity.transform)

    def delete_item(self, index):
        self.delete_render_components()
        self.pin_render.clear()

    def clear(self):
        pass
