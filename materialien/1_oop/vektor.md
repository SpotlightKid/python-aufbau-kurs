# Beispiel: Vektor-Klasse mit magischen Methoden in Python

In diesem ausführlichen Beispiel wird eine eigene `Vector`-Klasse schrittweise entwickelt,
um zu zeigen, wie man mit magischen Methoden (`__add__`, `__sub__`, `__mul__`, `__truediv__`, 
`__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__str__`, usw.) das Verhalten von Objekten 
anpassen kann. So wird die Klasse zunehmend benutzerfreundlicher und "pythonic".

---

## Beispiel 1: Eine einfache Vektor-Klasse

Wir beginnen mit einer simplen Klasse, die einen zweidimensionalen Vektor beschreibt.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

v = Vector(3, 4)
print(v.x)  # Output: 3
print(v.y)  # Output: 4
```

---

## Beispiel 2: String-Repräsentation mit `__str__`

Mit `__str__` kann man festlegen, was beim Ausdrucken eines Objekts angezeigt wird.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v = Vector(3, 4)
print(v)  # Output: Vector(3, 4)
```

Optional kann man noch `__repr__` ergänzen, um die offizielle Repräsentation zu bestimmen.

---

## Beispiel 3: Mathematische Operatoren überladen

Jetzt erweitern wir die Klasse so, dass man Vektoren addieren, subtrahieren, multiplizieren 
(skalare Multiplikation), und dividieren (Division durch Skalar) kann.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented

    def __rmul__(self, scalar):
        # Ermöglicht auch: scalar * vector
        return self.__mul__(scalar)

v1 = Vector(2, 3)
v2 = Vector(1, 1)

print(v1 + v2)       # Vector(3, 4)
print(v1 - v2)       # Vector(1, 2)
print(v1 * 2)        # Vector(4, 6)
print(3 * v2)        # Vector(3, 3)
print(v1 / 2)        # Vector(1.0, 1.5)
```

---

## Beispiel 4: Vergleichsoperatoren implementieren

Mit Vergleichsmethoden kann man Vektoren vergleichen, z.B. Gleichheit (`==`) und Größenvergleiche 
(z.B. nach Betrag).

```python
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

    def __lt__(self, other):
        # Vergleich nach Betrag (Länge)
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude() < other.magnitude()

    def __le__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude() <= other.magnitude()

    def __gt__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude() > other.magnitude()

    def __ge__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude() >= other.magnitude()

    def magnitude(self):
        """Compute the vector's magnitude (length)."""
        return math.hypot(self.x, self.y)

v1 = Vector(3, 4)
v2 = Vector(6, 8)
v3 = Vector(3, 4)

print(v1 == v3)      # True
print(v1 == v2)      # False
print(v1 < v2)       # True (5 < 10)
print(v2 > v1)       # True
print(v1 >= v3)      # True
print(v1 <= v3)      # True
```

---

## Fazit

Durch das schrittweise Implementieren von magischen Methoden kann man eigene Klassen so gestalten,
dass sie sich wie eingebaute Python-Typen anfühlen, Operatoren unterstützen und sich natürlich
verhalten.

---

## Übungen

1. **Negation:**  
   Ergänze die `Vector`-Klasse um die Methode `__neg__`, sodass `-v` einen negierten Vektor ergibt.

2. **Dot-Product:**  
   Implementiere die Methode `dot(self, other)`, die das Skalarprodukt (dot product) zweier Vektoren
   berechnet, und ergänze zusätzlich `__matmul__` (`@`-Operator).

3. **Repräsentation:**  
   Ergänze zusätzlich eine sinnvolle `__repr__`-Methode zur `Vector`-Klasse.

4. **Hashbarkeit:**  
   Implementiere `__hash__`, sodass Vektoren als Schlüssel in Dictionaries verwendet werden können,
   wenn sie gleich sind.

---
