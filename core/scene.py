import numpy as np
import glm
from OpenGL.GL import *
from core.camera import Camera
from core.mesh import Mesh
from util.obj_loader import load_obj


class Scene:
    def __init__(self) -> None:
        self.meshs: list[Mesh] = []

    def load_mesh(self, filename, name="Untitled Mesh", material_name="default_material"):
        mesh = Mesh()

        with open(filename, "r") as file:
            vertex_shader_code = file.read()
        faces = load_obj(vertex_shader_code)

        mesh.vertices = np.array(faces, dtype='float32')

        mesh.name = name
        mesh.material_name = material_name
        self.meshs.append(mesh)
        return mesh

    def draw(self, context):
        camera: Camera = context.camera
        proj = camera.projection_matrix()
        view = camera.view_matrix()

        for mesh in self.meshs:
            model = mesh.model_matrix()
            material = mesh.material_name
            material = context.materials[material]

            shader = material.use(context)

            glUniformMatrix4fv(glGetUniformLocation(
                shader.get_program(), "model"), 1, GL_FALSE, glm.value_ptr(model))
            glUniformMatrix4fv(glGetUniformLocation(
                shader.get_program(), "projection"), 1, GL_FALSE, glm.value_ptr(proj))
            glUniformMatrix4fv(glGetUniformLocation(
                shader.get_program(), "view"), 1, GL_FALSE, glm.value_ptr(view))

            mesh.bind()
            glDrawArrays(GL_TRIANGLES,0, len(
                mesh.vertices) // 5, GL_UNSIGNED_INT, None)
            mesh.unbind()
