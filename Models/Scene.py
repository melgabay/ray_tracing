
from typing import List
from Models.Vector3D import Vector3
from Models.Material import Material
from Models.Objects.Object import Object3D
from Models.Lights.Light import Light

class Scene:
    def __init__(self, eye: Vector3, ambient: Vector3):
        self.eye = eye
        self.ambient = ambient
        self.objects: List[Object3D] = []
        self.lights: List[Light] = []

    def add_object(self, obj: Object3D):
        self.objects.append(obj)

    def add_light(self, light: Light):
        self.lights.append(light)
