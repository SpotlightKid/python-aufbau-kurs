class MyClass:
    class_attr = 0

    def __init__(self, value):
        self.value = value

    @classmethod
    def set_class_attr(cls, val):
        cls.class_attr = val

    @staticmethod
    def add(x, y):
        return x + y

# Verwendung von classmethod
MyClass.set_class_attr(10)
print(MyClass.class_attr)  # Ausgabe: 10

# Verwendung von staticmethod
result = MyClass.add(5, 7)
print(result)  # Ausgabe: 12

# Auch Instanzen können beide Methoden aufrufen
obj = MyClass(3)
obj.set_class_attr(20)
print(MyClass.class_attr) # Ausgabe: 20
print(obj.add(2, 4))      # Ausgabe: 6
