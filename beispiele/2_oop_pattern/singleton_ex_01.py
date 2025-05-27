class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        self.value = value

# Usage
a = Singleton(1)
b = Singleton(2)
print(a is b)        # Output: True
print(a.value)       # Output: 2 (letzter Wert, da gleiche Instanz)
print(b.value)       # Output: 2
