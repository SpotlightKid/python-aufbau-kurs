# Einführung in Python Dataclasses

Dataclasses sind ein Feature von Python (ab Version 3.7), welches das Definieren von Klassen für 
Datenobjekte deutlich vereinfacht. Mit der Dekorator-Syntax `@dataclass` wird der Boilerplate-Code 
für Initialisierung, Vergleich und Repräsentation automatisch generiert.

---

## Klassische Klasse: Viel Boilerplate

Ohne Dataclasses muss man Konstruktor und oft Vergleichs-/Repräsentationsmethoden selbst schreiben:

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"

p = Person("Alice", 30)
print(p)  # Person(name='Alice', age=30)
```

Hier muss man die Attribute mehrfach angeben (als Parameter und als Zuweisung im Konstruktor).

---

## Mit `@dataclass`: Weniger Code, mehr Komfort

Mit `@dataclass` werden `__init__`, `__repr__` und `__eq__` automatisch erzeugt:

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person("Alice", 30)
print(p)            # Person(name='Alice', age=30)
print(p.name)       # Alice
print(p.age)        # 30
```

- Die Attribute werden als Felder der Klasse angegeben.
- Der Konstruktor (`__init__`) wird automatisch erstellt.
- Auch Methoden wie `__repr__` (für die Ausgabe) und `__eq__` (Vergleich mit `==`) sind dabei.

---

## Weitere Features von Dataclasses

### Standardwerte

```python
@dataclass
class Person:
    name: str
    age: int = 0

p = Person("Bob")
print(p)  # Person(name='Bob', age=0)
```

### Vergleich von Objekten

```python
p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
print(p1 == p2)  # True
```

### Unveränderliche Dataclasses (immutable)

```python
@dataclass(frozen=True)
class Person:
    name: str
    age: int

p = Person("Carol", 22)
# p.age = 23  # Raises error (cannot assign to field 'age')
```

---

## Felder mit `field()`

Mit `field()` können zusätzliche Optionen wie Standardwerte, Ausschluss vom Vergleich, etc., 
festgelegt werden.

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    id: int = field(default=0, compare=False)

p1 = Person("Dave", 40, id=1)
p2 = Person("Dave", 40, id=2)
print(p1 == p2)  # True, da id nicht verglichen wird
```

---

## Zusammenfassung

- Dataclasses reduzieren Boilerplate-Code bei Datenobjekten.
- Automatisch erzeugt: `__init__`, `__repr__`, `__eq__` und mehr.
- Flexibel anpassbar durch Argumente und `field()`.

---

## Übungen

1. Ergänze die Dataclass `Person` um ein Feld `email` mit Standardwert `""` und teste die Ausgabe.
2. Schreibe eine Dataclass `Book` mit Feldern `title`, `author` und `year`, alle als Strings.
3. Passe die Dataclass `Person` so an, dass, wenn eine Liste von `Person`-Objekten sortiert wird, nur das Alter für die Sortierung berücksichtigt wird.

   Hinweis: benutze `order=True` und `field(compare=False)` an den angemessenen Stellen im Code.
