
from Models.Vector3D import Vector3
from Models.Lights.Light import Light
import math

class SpotLight(Light):
    def __init__(self, position: Vector3, direction: Vector3, cutoff_cos: float, color: Vector3):
        super().__init__(color)
        self.position = position
        self.direction = direction.normalize()
        self.cutoff_cos = cutoff_cos  # cosine theta

    def inside_cone(self, L: Vector3) -> bool:
        # L = (light_position - point)
        return self.direction.dot(L.normalize()) >= self.cutoff_cos
