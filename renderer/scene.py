import numpy as np

from cshape_objects.surfaces.surface import Surface

vertices = (
    np.array([-0.5, 0.5, 0.0], dtype=np.float32),
    np.array([-0.5, -0.5, 0.0], dtype=np.float32),
    np.array([0.5, -0.5, 0.0], dtype=np.float32),
    np.array([0.5, 0.5, 0.0], dtype=np.float32)
)
vertices = np.array(vertices, dtype=np.float32)

indices = (
    0, 1, 2,
    0, 2, 3
)

indices = np.array(indices, dtype=np.uint32)


class Scene:
    def __init__(self):
        self.surface_classes = []
        self.vertices = np.array((), dtype=np.float32)
        self.indices = np.array((), dtype=np.uint32)

    def add_surface(self, surface: Surface):
        self.surface_classes.append(surface)
        for vertex in surface.get_vertices():
            vertex = np.array(vertex, dtype=np.float32)
            self.vertices = np.append(self.vertices, vertex)
        self.indices = np.append(self.indices, surface.get_indices())
        print(self.surface_classes, self.vertices, self.indices, surface.get_vertices(), surface.get_indices())

    def delete_surface(self, surface_id):
        vertices_count = np.size(self.surface_classes[surface_id].get_vertices())
        indices_count = np.size(self.surface_classes[surface_id].get_indices())

    def change_surface(self, surface_id):
        pass

    def get_vertices(self):
        return self.vertices

    def get_indices(self):
        return self.indices


scene = Scene()
