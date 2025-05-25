import math

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
        return self.__mul__(scalar)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

    def __lt__(self, other):
        # Vergleich nach Betrag (Länge)
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude() < other.magnitude()

    def __le__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude() <= other.magnitude()

    def __gt__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude() > other.magnitude()

    def __ge__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude() >= other.magnitude()

    def magnitude(self):
        """Compute the vector's magnitude (length)."""
        return math.hypot(self.x, self.y)

v1 = Vector(3, 4)
v2 = Vector(6, 8)
v3 = Vector(3, 4)

print(v1 == v3)      # True
print(v1 == v2)      # False
print(v1 < v2)       # True (5 < 10)
print(v2 > v1)       # True
print(v1 >= v3)      # True
print(v1 <= v3)      # True
