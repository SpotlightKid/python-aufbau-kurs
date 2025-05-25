# Abstrakte Basisklassen (ABCs)

**Abstract Base Classes (ABCs)** sind abstrakte Klassen, die als Vorlage für andere Klassen dienen.
Sie werden verwendet, um Schnittstellen und gemeinsame Methoden für verschiedene Unterklassen
zu definieren. Abstrakte Methoden in einer ABC müssen von jeder konkreten Unterklasse implementiert
werden. In Python verwendet man dazu das `abc`-Modul und die Dekoratoren `@abstractmethod` und
die Basisklasse `ABC`.

## Vorteile

- **Schnittstellendefinition:** Sicherstellen, dass Unterklassen bestimmte Methoden implementieren.
- **Typsicherheit:** Verhindert die Instanziierung unvollständiger Klassen.
- **Flexibilität:** Erlaubt polymorphe Nutzung von Objekten unterschiedlicher konkreter Klassen.

## Beispielcode

```python filename=abc_shapes.py
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
```

### Erklärung

- Die Klasse `Shape` ist eine abstrakte Basisklasse, die die Methode `area` als abstrakt deklariert.
- Die konkrete Klasse `Rectangle` implementiert die Methode `area`.
- Eine Instanz der ABC kann nicht erzeugt werden; die Unterklasse muss alle abstrakten Methoden
  implementieren.

---

## Programmierübungen

1. **Weitere konkrete Unterklasse:**

   Implementiere eine Klasse `Circle`, die von `Shape` erbt und eine Methode `area` für die Fläche
   des Kreises bereitstellt.

2. **Mehrere abstrakte Methoden:**

   Ergänze die ABC `Shape` um eine weitere abstrakte Methode `perimeter()`. Implementiere sie in
   `Rectangle` und deiner neuen `Circle`-Klasse.

3. **Polymorphe Nutzung:**

   Erstelle eine Liste aus verschiedenen `Shape`-Objekten (`Rectangle`, `Circle` etc.) und gib für
   jedes Objekt Fläche und Umfang aus.
