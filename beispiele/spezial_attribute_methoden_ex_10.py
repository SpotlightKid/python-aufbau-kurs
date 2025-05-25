class Animal:
    """A simple animal class."""

    def speak(self):
        """Makes a sound."""
        print("...")

a = Animal()
print(a.__class__)      # <class '__main__.Animal'>
print(Animal.__name__)  # Animal
print(Animal.__doc__)   # A simple animal class.
print(a.speak.__name__) # speak
print(a.speak.__doc__)  # Makes a sound.
