class Person:
    def __init__(self, name):
        self._name = name  # private attribute

    @property
    def name(self):
        """The name property getter."""
        return self._name

    @name.setter
    def name(self, value):
        """The name property setter."""
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

# Usage
p = Person("Alice")
print(p.name)     # Accesses _name via the getter
print(Person.name.__doc__)

p.name = "Bob"    # Sets _name via the setter
print(p.name)     # Output: Bob

# p.name = ""     # Would raise ValueError: Name cannot be empty
