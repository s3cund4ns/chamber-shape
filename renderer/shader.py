from sys import getsizeof

from OpenGL.GL.shaders import compileProgram, compileShader
from OpenGL.raw.GL.ARB.vertex_shader import GL_FLOAT
from OpenGL.raw.GL.VERSION.GL_2_0 import glCreateProgram, glCreateShader, GL_VERTEX_SHADER, glShaderSource, \
    glCompileShader, glGetShaderiv, GL_COMPILE_STATUS, glGetShaderInfoLog, glAttachShader, GL_FRAGMENT_SHADER, \
    glLinkProgram, GL_LINK_STATUS, glValidateProgram, GL_VALIDATE_STATUS, glUseProgram, glGetProgramiv, \
    glGetProgramInfoLog
from PySide6.QtOpenGL import QOpenGLShaderProgram, QOpenGLShader

from renderer.vertex import Vertex


class ShaderProgram:
    # def __init__(self):
    #     self.vertex_shader = None
    #     self.fragment_shader = None
    #     self.program = None
    #
    # def compile(self, *shader_files: str):
    #     vertex_shader_file, fragment_shader_file = shader_files
    #     self.vertex_shader = compileShader(self.load_shader(vertex_shader_file), GL_VERTEX_SHADER)
    #     self.fragment_shader = compileShader(self.load_shader(fragment_shader_file), GL_FRAGMENT_SHADER)
    #     self.program = compileProgram(self.vertex_shader, self.fragment_shader)
    #
    # @staticmethod
    # def load_shader(shader_file: str) -> str:
    #     # try:
    #         with open(shader_file, 'r') as file:
    #             shader_src = file.read()
    #             return shader_src
    #     # except FileNotFoundError:
    #     #     return 'Shader is not found!'
    #
    # def bind(self):
    #     glUseProgram(self.program)

    def __init__(self, vertex_shader_src: str, fragment_shader_src: str):
        self.shader_program = QOpenGLShaderProgram()
        self.shader_program_id = QOpenGLShaderProgram.programId(self.shader_program)
        self.vertex_shader_src: str = vertex_shader_src
        self.fragment_shader_src: str = fragment_shader_src

    def init_shaders(self):
        if not (
                self.shader_program.addShaderFromSourceFile(QOpenGLShader.ShaderTypeBit.Vertex,
                                                            self.vertex_shader_src)):
            self.shader_program.log()

        if not (
                self.shader_program.addShaderFromSourceFile(QOpenGLShader.ShaderTypeBit.Fragment,
                                                            self.fragment_shader_src)):
            self.shader_program.log()

        if not (
                self.shader_program.link()):
            self.shader_program.log()

    def bind(self):
        self.shader_program.bind()

    def set_attribute(self, location: int):
        self.shader_program.enableAttributeArray(location)
        self.shader_program.setAttributeBuffer(location, GL_FLOAT, 0, 3, getsizeof(Vertex))

    def set_uniform_value(self, name: str, value: any):
        self.shader_program.setUniformValue(name, value)
