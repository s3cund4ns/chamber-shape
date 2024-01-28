from OpenGL.GL import glGenVertexArrays
from OpenGL.raw.GL.VERSION.GL_1_5 import glBindBuffer, GL_ARRAY_BUFFER
from OpenGL.raw.GL.VERSION.GL_3_0 import glBindVertexArray


class VertexArray:
    def __init__(self):
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

    def bind(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vao)
