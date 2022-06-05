from core.camera import Camera
from core.material import Material
from core.scene import Scene
from core.shader import Shader
from core.texture import Texture
import pygame as pg


class Context:
    def __init__(self) -> None:
        self.scene: Scene = Scene()
        self.camera: Camera = Camera()
        self.shaders: dict[str, Shader] = {}
        self.textures = {}
        self.materials: dict[str, Material] = {}

    def load_shader(self, name, vertex_shader_source, fragment_shader_source):
        vertex_shader_code = ""
        fragment_shader_code = ""

        with open(vertex_shader_source, "r") as file:
            vertex_shader_code = file.read()

        with open(fragment_shader_source, "r") as file:
            fragment_shader_code = file.read()

        self.shaders[name] = Shader(
            vertex_shader_code, fragment_shader_code)
        return self.shaders[name]

    def load_texture(self, name, filepath):
        texture = Texture()
        texture.name = name

        image = pg.image.load(filepath)
        image = pg.transform.flip(image, False, True)

        image_width, image_height = image.get_rect().size
        img_data = pg.image.tostring(image, "RGBA")
        texture.width = image_width
        texture.height = image_height
        texture.data = img_data
        self.textures[name] = texture

    def create_material(self, name, shader_name, parameters):
        self.materials[name] = Material(shader_name, parameters)
