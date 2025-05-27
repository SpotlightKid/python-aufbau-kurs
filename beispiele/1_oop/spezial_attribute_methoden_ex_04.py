class Point:
    # ...
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # Output: True
