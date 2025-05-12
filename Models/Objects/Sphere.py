
import math
from typing import Optional, Tuple
from Models.Vector3D import Vector3
from Models.Objects.Ray import Ray
from Models.Material import Material
from Models.Objects.Object import Object3D, Intersection

class Sphere(Object3D):
    def __init__(self, center: Vector3, radius: float, material: Material):
        super().__init__(material)
        self.center = center
        self.radius = radius

    def intersect(self, ray: Ray) -> Optional[Intersection]:
        oc = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2.0 * oc.dot(ray.direction)
        c = oc.dot(oc) - self.radius * self.radius
        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return None
        sqrt_disc = math.sqrt(discriminant)
        t1 = (-b - sqrt_disc) / (2 * a)
        t2 = (-b + sqrt_disc) / (2 * a)
        t = None
        if t1 > 1e-4:
            t = t1
        elif t2 > 1e-4:
            t = t2
        if t is None:
            return None
        point = ray.point_at(t)
        normal = (point - self.center).normalize()
        return (t, point, normal, self.material)
