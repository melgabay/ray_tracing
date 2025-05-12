
from Models.Vector3D import Vector3
from Models.Lights.Light import Light

class DirectionalLight(Light):
    """Directional light like the sun: direction vector points FROM light TO scene.
    We store the vector from a point TO the light = -direction."""
    def __init__(self, direction: Vector3, color: Vector3):
        super().__init__(color)
        self.direction = direction.normalize()

    def L_vector(self):
        # returns vector from point to light (opposite of direction)
        return -self.direction
