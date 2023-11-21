import ctypes

from OpenGL.GL import glGenBuffers, glGenVertexArrays, glBufferData, glVertexAttribPointer
from OpenGL.GL.shaders import compileProgram, compileShader
from OpenGL.raw.GL.VERSION.GL_1_0 import glClear, GL_COLOR_BUFFER_BIT, GL_TRIANGLES
from OpenGL.raw.GL.VERSION.GL_1_1 import glDrawArrays
from OpenGL.raw.GL.VERSION.GL_1_5 import glBindBuffer, GL_ARRAY_BUFFER, GL_STATIC_DRAW
from OpenGL.raw.GL.VERSION.GL_2_0 import GL_VERTEX_SHADER, GL_FRAGMENT_SHADER, glUseProgram, glEnableVertexAttribArray
from OpenGL.raw.GL.VERSION.GL_3_0 import glBindVertexArray
from OpenGL.raw.GL._types import GL_FLOAT, GL_FALSE
from PySide6.QtOpenGLWidgets import QOpenGLWidget

from renderer.shaders.base_shader import vertex_shader_src, fragment_shader_src

from PySide6.QtGui import QSurfaceFormat
from PySide6.QtOpenGL import QOpenGLVersionProfile

import numpy as np


class ViewPort(QOpenGLWidget):
    def initializeGL(self):
        self.format = QOpenGLVersionProfile()
        self.format.setVersion(4, 6)
        self.format.setProfile(QSurfaceFormat.OpenGLContextProfile.CoreProfile)

        self.shader = compileProgram(compileShader(vertex_shader_src, GL_VERTEX_SHADER),
                                     compileShader(fragment_shader_src, GL_FRAGMENT_SHADER))

        glUseProgram(self.shader)

        self.vertices = (
            -0.5, -0.5, 2.0, 1.0, 1.0, 1.0,
            0.5, -0.5, 1.0, 0.0, 1.0, 0.0,
            0.0, 0.5, 0.0, 0.0, 0.0, 1.0
        )
        self.vertices = np.array(self.vertices, dtype=np.float32)

        self.vbo = glGenBuffers(1)
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.vao)

        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(self.shader)
        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, 6)
