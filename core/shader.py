from logging import critical
from OpenGL.GL import *


class Shader:
    def __init__(self, vertex_shader_code, fragment_shader_code) -> None:
        self._vertex_shader_code = vertex_shader_code
        self._fragment_shader_code = fragment_shader_code
        self._program = None

    def compile(self) -> None:
        """Compile the shader program."""
        vertex_shader = self.compile_shader(
            self._vertex_shader_code, GL_VERTEX_SHADER)
        fragment_shader = self.compile_shader(
            self._fragment_shader_code, GL_FRAGMENT_SHADER)

        self._program = glCreateProgram()

        glAttachShader(self._program, vertex_shader)
        glAttachShader(self._program, fragment_shader)
        glLinkProgram(self._program)

        self.check_program_link_status()

        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)

    def compile_shader(self, source, shader_type) -> int:
        """Compile a shader."""
        shader = glCreateShader(shader_type)
        glShaderSource(shader, source)
        glCompileShader(shader)
        self.check_shader_compile_status(shader)
        return shader

    def check_shader_compile_status(self, shader):
        success = glGetShaderiv(shader, GL_COMPILE_STATUS)
        if (not success):
            infoLog = glGetShaderInfoLog(shader)
            critical("ERROR::SHADER_COMPILATION_ERROR: \n" + infoLog.decode())
            exit()

    def check_program_link_status(self):
        success = glGetProgramiv(self._program, GL_LINK_STATUS)
        if (not success):
            infoLog = glGetProgramInfoLog(self._program)
            critical("ERROR::PROGRAM_LINKING_ERROR of type: \n" +
                     infoLog.decode())
            exit()

    def use(self):
        glUseProgram(self._program)

    def get_program(self) -> int:
        return self._program

    def set_uniform_int(self, name, value):
        assert self._program != None
        glUniform1i(glGetUniformLocation(self._program, name), value)

    def __del__(self) -> None:
        if self._program:
            glDeleteProgram(self._program)
