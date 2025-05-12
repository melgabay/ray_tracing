
from Models.Vector3D import Vector3

class Ray:
    __slots__ = ("origin", "direction")

    def __init__(self, origin: Vector3, direction: Vector3):
        self.origin = origin
        self.direction = direction.normalize()

    def point_at(self, t: float) -> Vector3:
        return self.origin + self.direction * t
