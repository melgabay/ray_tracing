
from dataclasses import dataclass
from Models.Vector3D import Vector3

@dataclass
class Material:
    ambient: Vector3
    diffuse: Vector3
    specular: Vector3 = Vector3(0.7, 0.7, 0.7)
    shininess: float = 10.0
