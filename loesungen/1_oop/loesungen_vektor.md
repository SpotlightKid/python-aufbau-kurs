# Beispiel-Lösungen für die `Vector`-Übungen

## 1. Negation: `__neg__`

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Vector(-self.x, -self.y)

v = Vector(3, -4)
print(-v)  # Output: <__main__.Vector object ...>
# Für schönere Ausgabe siehe Aufgabe 3!
```

---

## 2. Dot-Product und `__matmul__`

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dot(self, other):
        """Return the dot product of self and other."""
        return self.x * other.x + self.y * other.y

    def __matmul__(self, other):
        """Enable the @ operator for dot product."""
        return self.dot(other)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1.dot(v2))     # Output: 11
print(v1 @ v2)        # Output: 11
```

---

## 3. Repräsentation: `__repr__`

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

v = Vector(7, -5)
print(repr(v))  # Output: Vector(7, -5)
```

---

## 4. Hashbarkeit: `__hash__`

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

v1 = Vector(1, 2)
v2 = Vector(1, 2)
v3 = Vector(2, 3)

s = set([v1, v2, v3])
print(len(s))  # Output: 2, da v1 == v2
print(v1 in s) # Output: True
print(v2 in s) # Output: True
print(v3 in s) # Output: True
```
