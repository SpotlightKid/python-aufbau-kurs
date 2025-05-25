class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """Return a generic animal sound."""
        return "Some sound"

class Dog(Animal):
    def speak(self):
        """Return the sound of a dog."""
        return "Woof!"


# Usage
animal = Animal("Generic animal")
print(animal.name)            # Output: Generic animal
print(animal.speak())         # Output: Some sound
print(dog.__class__.__name__) # Output: Animal

dog = Dog("Fifi")
print(dog.name)               # Output: Fifi
print(dog.speak())            # Output: Woof!
print(dog.__class__.__name__) # Output: Dog
