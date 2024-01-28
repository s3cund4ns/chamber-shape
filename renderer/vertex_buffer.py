from OpenGL.GL import glGenBuffers
from OpenGL.raw.GL.VERSION.GL_1_5 import glBindBuffer, GL_ARRAY_BUFFER, glBufferData, GL_STATIC_DRAW


class VertexBuffer:
    def __init__(self):
        self.vbo = glGenBuffers(1)

    def bind(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

    @staticmethod
    def copy_data(size, data):
        glBufferData(GL_ARRAY_BUFFER, size, data, GL_STATIC_DRAW)

