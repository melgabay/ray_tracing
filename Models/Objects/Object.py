
from abc import ABC, abstractmethod
from typing import Optional, Tuple
from Models.Objects.Ray import Ray
from Models.Vector3D import Vector3
from Models.Material import Material

Intersection = Tuple[float, Vector3, Vector3, Material]  # t, point, normal, material

class Object3D(ABC):
    def __init__(self, material: Material):
        self.material = material

    @abstractmethod
    def intersect(self, ray: Ray) -> Optional[Intersection]:
        pass
