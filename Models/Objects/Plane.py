
import math
from typing import Optional, Tuple
from Models.Vector3D import Vector3
from Models.Objects.Ray import Ray
from Models.Material import Material
from Models.Objects.Object import Object3D, Intersection

class Plane(Object3D):
    def __init__(self, normal: Vector3, d: float, material: Material):
        super().__init__(material)
        self.normal = normal.normalize()
        self.d = d  # plane equation n·x + d = 0
        # mark material for checker effect
        setattr(self.material, "checker", True)

    def intersect(self, ray: Ray) -> Optional[Intersection]:
        denom = self.normal.dot(ray.direction)
        if abs(denom) < 1e-6:
            return None
        t = -(self.normal.dot(ray.origin) + self.d) / denom
        if t < 1e-4:
            return None
        point = ray.point_at(t)
        # ensure normal faces against ray
        normal = self.normal if denom < 0 else -self.normal
        return (t, point, normal, self.material)
