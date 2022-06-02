import glm
from numpy import cos, sin

from constants import DEFAULT_WINDOW_SIZE


class Camera:
    def __init__(self, pos=glm.vec3(0.0, 1.5, 3.0), front=glm.vec3(0.0, 0.0, -1.0),
                 up=glm.vec3(0.0, 1.0, 0.0), fov=45.0, aspect_ratio=DEFAULT_WINDOW_SIZE[0] / DEFAULT_WINDOW_SIZE[1]) -> None:
        self.position = pos
        self.front = front
        self.up = up
        self.fov = fov
        self.aspect_ratio = aspect_ratio
        self.window_size = DEFAULT_WINDOW_SIZE
        self.speed = 1.0  # meters / second

        self.yaw = -90.0
        self.pitch = 0.0

    def set_aspect_ratio(self, aspect_ratio):
        self.aspect_ratio = aspect_ratio

    def view_matrix(self):
        return glm.lookAt(self.position, self.position + self.front, self.up)

    def projection_matrix(self):
        return glm.perspective(self.fov, self.aspect_ratio, 0.1, 100)

    def view_projection_matrix(self):
        return self.projection_matrix() * self.view_matrix()

    def update(self, delta_mouse, forward: float, right: float, up_motion: float, dt: float) -> None:
        delta_pos = forward * self.speed * dt
        delta_pos_side = right * self.speed * dt

        self.position += glm.vec3(0, up_motion * self.speed * dt, 0)

        self.position += self.speed * self.front * delta_pos
        self.position += glm.normalize(glm.cross(self.front, self.up)
                                       ) * self.speed * delta_pos_side

        dx, dy = delta_mouse[0] * 0.1, delta_mouse[1] * 0.1

        self.yaw += dx
        self.pitch -= dy

        if self.pitch > 89.0:
            self.pitch = 89.0

        if self.pitch < -89.0:
            self.pitch = -89.0

        front = glm.vec3()
        front.x = cos(glm.radians(self.yaw)) * cos(glm.radians(self.pitch))
        front.y = sin(glm.radians(self.pitch))
        front.z = sin(glm.radians(self.yaw)) * cos(glm.radians(self.pitch))
        self.front = glm.normalize(front)
