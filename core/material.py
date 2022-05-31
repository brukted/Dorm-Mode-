from OpenGL.GL import *


class Material:
    def __init__(self, shader_name, parameters: dict):
        self.shader_name = shader_name
        self.parameters = parameters

    def use(self, context):
        shader = context.shaders[self.shader_name]

        shader.use()

        for _, parameter in self.parameters.items():
            if parameter[0] == "texture":
                texture_name = parameter[1]
                texture_unit = parameter[2]

                glActiveTexture(GL_TEXTURE0 + texture_unit)
                texture_id = context.textures[texture_name].get_id()

                glBindTexture(GL_TEXTURE_2D, texture_id)
                shader.set_uniform_int(texture_name, texture_unit)

        return shader
