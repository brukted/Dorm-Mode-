from OpenGL.GL import *
import glm

from core.types import vec3


class Mesh:
    def __init__(self):
        self.material_name = None
        self.vertices = None  # (u, v, x, y, z)
        self.name = "untitled_mesh"
        self.material_name = "default_material"
        self.position = vec3(0.0, 0.0, 0.0)
        self.rotation = vec3(0.0, 0.0, 0.0)
        self.vao = None
        self.vbo = None

    def bind(self):
        if self.vao is None:
            self.build_buffers()
        glBindVertexArray(self.vao)

    def model_matrix(self):
        pos = self.position
        model = glm.mat4(1.0)
        model = glm.translate(model, glm.vec3(pos.x, pos.y, pos.z))
        return model

    def unbind(self):
        glBindVertexArray(0)

    def build_buffers(self):
        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)

        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes,
                     self.vertices, GL_STATIC_DRAW)

        # UV
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE,
                              self.vertices.itemsize * 5, ctypes.c_void_p(0))

        # Position
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE,
                              self.vertices.itemsize * 5, ctypes.c_void_p(8))

    def __del__(self):
        glDeleteBuffers(1, self.vao)
        glDeleteBuffers(1, self.vbo)
