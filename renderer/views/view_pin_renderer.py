from PySide6.QtGui import QRgba64, QVector3D

from cshape_objects.material import Material
from cshape_objects.pin import Pin
from project_data.view import View
from renderer.entities.z_cylinder_entity import ZCylinderEntity


class ViewPinRenderer(View):
    def __init__(self):
        super().__init__()
        self.pins: list[Pin] = []
        self.instances: list = []
        self.selected_pin_index: int = -1
        self.z_cylinder_entities: list[ZCylinderEntity] = []
        self.scene = None

    def set_scene(self, scene):
        self.scene = scene

    def add_item(self, index, item_text, item: Pin):
        self.pins.append(item)

    def select_item(self, index, item):
        self.selected_pin_index = index

    def change_item(self, *args):
        pass

    def delete_item(self, index):
        self.pins.pop(self.selected_pin_index)

    def __find_pin_by_universe(self, universe_number: int) -> Pin:
        for pin in self.pins:
            if pin.get_universe_index() == universe_number:
                return pin

    def create_instance(self, universe_number: int, pos_x: float, pos_y: float) -> int:
        pin: Pin = self.__find_pin_by_universe(universe_number)
        regions = pin.get_regions()
        z_cylinder_entities = []
        for region in regions:
            material: Material = region[0]
            material_color = material.color
            red, green, blue = material_color
            radius: float = region[1]
            z_cylinder_entity = ZCylinderEntity(self.scene)
            z_cylinder_entity.material.setAmbient(QRgba64.fromRgba(red, green, blue, 255))
            z_cylinder_entity.mesh.setRadius(radius)
            pos_z = float(regions.index(region)) * -0.1
            z_cylinder_entity.transform.setTranslation(QVector3D(pos_x, pos_y, pos_z))
            z_cylinder_entities.append(z_cylinder_entity)
        self.instances.append([universe_number, z_cylinder_entities])
        return len(self.instances)-1

    def change_instance_position(self, index: int, pos_x: float, pos_y: float) -> None:
        if index is None:
            return
        z_cylinder_entities: list[ZCylinderEntity] = self.instances[index][1]
        for z_cylinder_entity in z_cylinder_entities:
            z_pos = z_cylinder_entity.transform.translation().z()
            z_cylinder_entity.transform.setTranslation(QVector3D(pos_x, pos_y, z_pos))
