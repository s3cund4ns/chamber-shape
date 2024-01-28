from OpenGL.GL import glGenBuffers
from OpenGL.raw.GL.VERSION.GL_1_5 import glBindBuffer, GL_ELEMENT_ARRAY_BUFFER, glBufferData, GL_ARRAY_BUFFER, \
    GL_STATIC_DRAW


class IndexBuffer:
    def __init__(self):
        self.ibo = glGenBuffers(1)

    def bind(self):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ibo)

    @staticmethod
    def copy_data(size, data):
        glBufferData(GL_ARRAY_BUFFER, size, data, GL_STATIC_DRAW)
