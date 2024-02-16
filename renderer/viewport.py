from PySide6.Qt3DExtras import Qt3DExtras
from PySide6.Qt3DCore import Qt3DCore
from PySide6.Qt3DRender import Qt3DRender

from PySide6.QtGui import QVector3D, QRgba64, QQuaternion

from preprocessor.lattice import Lattice
from preprocessor.pin import Pin
from renderer.multi_parent_entity import MultiParentEntity
from surfaces.surface import SurfacesTypes

BACKGROUND_COLOR = QRgba64.fromRgba(41, 41, 41, 255)
CAMERA_FOV = 60.0
CAMERA_NEAR_PLANE = 0.1
CAMERA_FAR_PLANE = 1000.0
CAMERA_POSITION = QVector3D(0.0, 0.0, 50.0)
CAMERA_VIEW_CENTER = QVector3D(0.0, 0.0, 0.0)
CAMERA_FPS_CONTROLLER = True
CAMERA_CONTROLLER_LOOK_SPEED = 180.0
CAMERA_CONTROLLER_LINEAR_SPEED = 50.0


class ViewPort(Qt3DExtras.Qt3DWindow):
    def __init__(self):
        super().__init__()
        self.surface_entities = []
        self.universe_entities = []
        self.cell_entities = []
        self.lattice_entities = []
        self.mesh_entities = []
        self.material_entities = []
        self.transform_entities = []
        self.light_entities = []

        self.aspect: float = float(self.width()) / self.height()
        self.defaultFrameGraph().setClearColor(BACKGROUND_COLOR)
        self.root_entity: Qt3DCore.QEntity = Qt3DCore.QEntity()
        self.create_scene()
        self.camera: Qt3DRender.QCamera = self.camera()
        self.set_camera_parameters(CAMERA_FOV, self.aspect, CAMERA_NEAR_PLANE, CAMERA_FAR_PLANE,
                                   CAMERA_POSITION, CAMERA_VIEW_CENTER)
        self.camera_controller = None
        self.set_camera_controller(CAMERA_FPS_CONTROLLER, CAMERA_CONTROLLER_LOOK_SPEED, CAMERA_CONTROLLER_LINEAR_SPEED)
        self.setRootEntity(self.root_entity)

    def create_scene(self):
        transform = Qt3DCore.QTransform(self.root_entity)
        transform.setRotationX(-90.0)
        self.root_entity.addComponent(transform)
        self.add_light_entity()

    def set_camera_parameters(self, field_of_view: float, aspect: float, near_plane: float, far_plane: float,
                              position: QVector3D, view_center: QVector3D):
        self.camera.lens().setPerspectiveProjection(field_of_view, aspect,
                                                    near_plane, far_plane)
        self.camera.setPosition(position)
        self.camera.setViewCenter(view_center)

    def set_camera_controller(self, is_camera_fps_controller: bool, look_speed: float, linear_speed: float):
        if is_camera_fps_controller:
            self.camera_controller = Qt3DExtras.QFirstPersonCameraController(self.root_entity)
        else:
            self.camera_controller = Qt3DExtras.QOrbitCameraController(self.root_entity)
        self.camera_controller.setCamera(self.camera)
        self.camera_controller.setLookSpeed(look_speed)
        self.camera_controller.setLinearSpeed(linear_speed)

    def add_light_entity(self):
        light_entity: Qt3DCore.QEntity = Qt3DCore.QEntity(self.root_entity)
        point_light: Qt3DRender.QDirectionalLight = Qt3DRender.QDirectionalLight(light_entity)

        light_transform: Qt3DCore.QTransform = Qt3DCore.QTransform(light_entity)
        light_transform.setTranslation(QVector3D(0.0, 0.0, 30.0))

        light_entity.addComponent(point_light)
        light_entity.addComponent(light_transform)

        self.light_entities.append(light_entity)

    def add_surface_entity(self, surface_type: SurfacesTypes, index):
        surface_entity: MultiParentEntity = MultiParentEntity(self.root_entity)
        # surface_entity: Qt3DCore.QEntity = Qt3DCore.QEntity(self.root_entity)
        surface_mesh = None

        if surface_type == SurfacesTypes.Plane:
            surface_mesh = Qt3DExtras.QPlaneMesh(surface_entity)
            surface_mesh.setWidth(100.0)
            surface_mesh.setHeight(100.0)
        elif surface_type == SurfacesTypes.Sphere:
            surface_mesh = Qt3DExtras.QSphereMesh(surface_entity)
            surface_mesh.setRadius(5.0)
        elif surface_type == SurfacesTypes.Cylinder:
            surface_mesh = Qt3DExtras.QCylinderMesh(surface_entity)
            surface_mesh.setRadius(5.0)
            surface_mesh.setLength(100.0)
        elif surface_type == SurfacesTypes.Cone:
            surface_mesh = Qt3DExtras.QConeMesh(surface_entity)
            surface_mesh.setBottomRadius(5.0)
            surface_mesh.setLength(50.0)
        elif (surface_type == SurfacesTypes.YHexagonalPrism) or (surface_type == SurfacesTypes.XHexagonalPrism):
            surface_mesh = Qt3DExtras.QCylinderMesh()
            surface_mesh.setRadius(5.0)
            surface_mesh.setLength(100.0)
            surface_mesh.setSlices(6)
        else:
            surface_mesh = Qt3DExtras.QTorusMesh(surface_entity)
            surface_mesh.setRadius(50.0)
            surface_mesh.setMinorRadius(10.0)
            surface_mesh.setRings(100)
            surface_mesh.setSlices(32)

        surface_material: Qt3DExtras.QPhongMaterial = Qt3DExtras.QPhongMaterial(surface_entity)
        surface_material.setDiffuse(QRgba64.fromRgba(139, 0, 255, 255))
        surface_transform: Qt3DCore.QTransform = Qt3DCore.QTransform(surface_entity)
        if surface_type == SurfacesTypes.XHexagonalPrism:
            surface_transform.setRotationZ(90.0)
        else:
            surface_transform.setRotationX(90.0)

        surface_transform.setTranslation(QVector3D(0.0, 0.0, 0.0))

        surface_entity.addComponent(surface_mesh)
        surface_entity.addComponent(surface_material)
        surface_entity.addComponent(surface_transform)

        self.mesh_entities.insert(index, surface_mesh)
        self.material_entities.insert(index, surface_material)
        self.transform_entities.insert(index, surface_transform)

        self.surface_entities.insert(index, surface_entity)

    def delete_surface_entity(self, entity_id: int):
        entity = self.surface_entities[entity_id]
        mesh = self.mesh_entities[entity_id]
        material = self.material_entities[entity_id]
        transform = self.transform_entities[entity_id]
        entity.removeComponent(mesh)
        entity.removeComponent(material)
        entity.removeComponent(transform)
        self.mesh_entities.pop(entity_id)
        self.material_entities.pop(entity_id)
        self.transform_entities.pop(entity_id)
        entity.deleteLater()
        self.surface_entities.pop(entity_id)

    def select_surface_entity(self, entity_id):
        self.material_entities[entity_id].setDiffuse(QRgba64.fromRgba(200, 200, 200, 255))

    def deselect_surface_entity(self, entity_id):
        self.material_entities[entity_id].setDiffuse(QRgba64.fromRgba(139, 0, 255, 255))

    def set_surface_transform(self, entity_id: int, pos_x: float, pos_y: float, pos_z: float, ):
        self.transform_entities[entity_id].setTranslation(QVector3D(pos_x, pos_y, pos_z))

    def set_surface_color(self, entity_id: int, red: float, green: float, blue: float, alpha: float):
        self.material_entities[entity_id].setDiffuse(QRgba64.fromRgba(int(red), int(green), int(blue), int(alpha)))

    def set_surface_mesh(self, mesh_id, surface_type: SurfacesTypes, parameters):
        mesh = self.mesh_entities[mesh_id]
        if surface_type == SurfacesTypes.Plane:
            pass
        elif surface_type == SurfacesTypes.Cylinder:
            radius, = parameters
            mesh.setRadius(radius)
        elif surface_type == SurfacesTypes.Sphere:
            radius, = parameters
            mesh.setRadius(radius)
        elif surface_type == SurfacesTypes.Cone:
            radius, height = parameters
            mesh.setBottomRadius(radius)
            mesh.setLength(height)
        elif (surface_type == SurfacesTypes.XHexagonalPrism) or (surface_type == SurfacesTypes.YHexagonalPrism):
            half_width, = parameters
            mesh.setRadius(half_width)

    def add_universe_entity(self):
        universe_entity: Qt3DCore.QEntity = Qt3DCore.QEntity(self.root_entity)
        universe_transform: Qt3DCore.QTransform = Qt3DCore.QTransform(universe_entity)
        universe_transform.setTranslation(QVector3D(0.0, 0.0, 0.0))
        universe_entity.addComponent(universe_transform)
        self.universe_entities.append(universe_entity)

    def add_cell_entity(self, universe_id: int):
        cell_entity: Qt3DCore.QEntity = Qt3DCore.QEntity(self.root_entity)
        self.cell_entities.append(cell_entity)

    def add_surface_entity_to_cell(self, surface_id: int, cell_id: int):
        self.surface_entities[surface_id].add_parent(self.cell_entities[cell_id])

    def add_pin_entity_to_lattice_entity(self, position, pin: Pin):
        pin_entity: Qt3DCore.QEntity = Qt3DCore.QEntity(self.root_entity)
        pin_transform = Qt3DCore.QTransform(pin_entity)
        pin_transform.setTranslation(QVector3D(position[0], position[1], position[2]))
        pin_transform.setRotationX(90.0)
        pin_mesh = Qt3DExtras.QCylinderMesh(pin_entity)
        pin_mesh.setRadius(3.0)
        pin_mesh.setLength(50.0)
        pin_material = Qt3DExtras.QPhongMaterial(pin_entity)
        pin_material: Qt3DExtras.QPhongMaterial = Qt3DExtras.QPhongMaterial(pin_entity)
        pin_entity.addComponent(pin_transform)
        pin_entity.addComponent(pin_mesh)
        pin_entity.addComponent(pin_material)
        self.lattice_entities.append(pin_entity)
        print(pin_entity.components())

    def select_lattice_entity(self):
        pass

