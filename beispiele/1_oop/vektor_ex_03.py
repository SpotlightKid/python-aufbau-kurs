class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented

    def __rmul__(self, scalar):
        # Ermöglicht auch: scalar * vector
        return self.__mul__(scalar)

v1 = Vector(2, 3)
v2 = Vector(1, 1)

print(v1 + v2)       # Vector(3, 4)
print(v1 - v2)       # Vector(1, 2)
print(v1 * 2)        # Vector(4, 6)
print(3 * v2)        # Vector(3, 3)
print(v1 / 2)        # Vector(1.0, 1.5)
