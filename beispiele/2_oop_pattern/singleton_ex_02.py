class Borg:
    """We are all one!"""
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

# Usage
x = Borg()
y = Borg()
x.answer = 42
print(y.answer)    # Output: 42
print(x is y)      # Output: False (verschiedene Instanzen)
