
import math

class Vector3:
    """Simple 3‑component vector with basic operations."""
    __slots__ = ("x", "y", "z")

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    # ----- Arithmetic -----
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __mul__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Vector3(self.x * other, self.y * other, self.z * other)
    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)

    # ----- Vector products -----
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    # ----- Magnitude -----
    def norm(self):
        return math.sqrt(self.dot(self))

    def normalize(self):
        n = self.norm()
        if n == 0:
            return self
        return self / n

    # ----- Reflection -----
    def reflect(self, normal):
        return self - normal * 2 * self.dot(normal)

    # ----- Utility -----
    def to_tuple(self):
        return (self.x, self.y, self.z)

    def __repr__(self):
        return f"Vector3({self.x:.3f},{self.y:.3f},{self.z:.3f})"
