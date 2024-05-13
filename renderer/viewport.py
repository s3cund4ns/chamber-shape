from PySide6.Qt3DExtras import Qt3DExtras
from PySide6.Qt3DCore import Qt3DCore
from PySide6.Qt3DRender import Qt3DRender

from PySide6.QtGui import QVector3D, QRgba64

from renderer.entities.surface_entity import SurfaceEntity

BACKGROUND_COLOR = QRgba64.fromRgba(31, 31, 31, 255)
CAMERA_FOV = 60.0
CAMERA_NEAR_PLANE = 0.1
CAMERA_FAR_PLANE = 1000.0
CAMERA_POSITION = QVector3D(0.0, 0.0, 50.0)
CAMERA_VIEW_CENTER = QVector3D(0.0, 0.0, 0.0)
CAMERA_FPS_CONTROLLER = True
CAMERA_CONTROLLER_LOOK_SPEED = 180.0
CAMERA_CONTROLLER_LINEAR_SPEED = 100.0


class Viewport:
    def __init__(self):
        self.surfaces_entities: list[SurfaceEntity] = []

        self.scene: Qt3DExtras.Qt3DWindow = Qt3DExtras.Qt3DWindow()
        # self.scene.show()

        self.aspect: float = float(self.scene.width()) / self.scene.height()
        self.scene.defaultFrameGraph().setClearColor(BACKGROUND_COLOR)
        self.root_entity: Qt3DCore.QEntity = Qt3DCore.QEntity()
        self.create_scene()
        self.camera: Qt3DRender.QCamera = self.scene.camera()
        self.set_camera_parameters(CAMERA_FOV, self.aspect, CAMERA_NEAR_PLANE, CAMERA_FAR_PLANE,
                                   CAMERA_POSITION, CAMERA_VIEW_CENTER)
        self.camera_controller = None
        self.set_camera_controller(CAMERA_FPS_CONTROLLER, CAMERA_CONTROLLER_LOOK_SPEED, CAMERA_CONTROLLER_LINEAR_SPEED)
        self.scene.setRootEntity(self.root_entity)

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
        directional_light: Qt3DRender.QDirectionalLight = Qt3DRender.QDirectionalLight(light_entity)

        light_transform: Qt3DCore.QTransform = Qt3DCore.QTransform(light_entity)
        light_transform.setTranslation(QVector3D(0.0, 0.0, 30.0))

        light_entity.addComponent(directional_light)
        light_entity.addComponent(light_transform)
