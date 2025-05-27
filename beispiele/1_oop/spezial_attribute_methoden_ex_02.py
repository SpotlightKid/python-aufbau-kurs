class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

p = Point(1, 2)
print(str(p))   # Output: Point(1, 2)
print(repr(p))  # Output: Point(1, 2)
