from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return area of rectangle."""
        return self.width * self.height

# Usage
# shape = Shape()         # Raises TypeError: Can't instantiate abstract class
rect = Rectangle(3, 4)
print(rect.area())        # Output: 12
