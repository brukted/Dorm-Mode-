from OpenGL.GL import *


class Texture:
    def __init__(self) -> None:
        self.name = None
        self._id = None
        self.width, self.height = None, None
        self.data = None

    def gen_buffers(self):
        self._id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self._id)
        # Set the texture wrapping parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        # Set texture filtering parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.width,
                     self.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.data)
        glGenerateMipmap(GL_TEXTURE_2D)

    def get_id(self):
        if self._id == None:
            self.gen_buffers()
        return self._id
