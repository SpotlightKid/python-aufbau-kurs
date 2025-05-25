# Magische Objektattribute und Methoden in Python (Special/Magic Methods)

In Python sind magische Methoden (auch "doppel-unterstrich Methoden" oder "Dunder Methods" genannt)
besondere Methoden, die durch Python aufgerufen werden, um das Verhalten von Objekten zu beeinflussen.
Sie ermöglichen es, eigene Klassen so zu gestalten, dass sie sich wie eingebaute Typen verhalten,
z.B. bei Vergleichen, Repräsentationen, Addition, Iteration usw.

Neben diesen Methoden gibt es auch spezielle Objektattribute wie `__name__`, `__class__` und `__doc__`,
die Informationen über ein Objekt oder eine Klasse bereitstellen. Diese Attribute werden oft für
Reflexion, Debugging oder Dokumentation genutzt.

Magische Methoden und Attribute haben Namen im Format `__name__`, z.B. `__init__`, `__str__`, `__add__`.

## Wichtige magische Methoden

### 1. `__init__`: Initialisierung (Konstruktor)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(p.x, p.y)  # Output: 1 2
```

### 2. `__str__` und `__repr__`: String-Repräsentation

- `__str__`: Was `print(obj)` oder `str(obj)` ausgibt (benutzerfreundlich)
- `__repr__`: Offizielle Repräsentation, nützlich für Debugging

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

p = Point(1, 2)
print(str(p))   # Output: Point(1, 2)
print(repr(p))  # Output: Point(1, 2)
```

### 3. Operatoren überladen: `__add__`, `__eq__`, etc.

#### Addition

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)  # Nutzt __str__ oder __repr__
```

#### Gleichheit

```python
class Point:
    # ...
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # Output: True
```

### 4. `__len__`, `__getitem__`, `__setitem__`: Verhalten wie Listen

```python
class MyList:
    def __init__(self, items):
        self._items = list(items)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

ml = MyList([1, 2, 3])
print(len(ml))      # Output: 3
print(ml[1])        # Output: 2
ml[1] = 99
print(ml[1])        # Output: 99
```

### 5. Iterierbarkeit: `__iter__`, `__next__`

```python
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

for num in Counter(3, 6):
    print(num)  # Output: 3, 4, 5, 6
```

### 6. Kontextmanager: `__enter__`, `__exit__`

```python
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with ManagedFile('test.txt') as f:
    f.write('Hello World!')
# Datei wird automatisch geschlossen
```

## Weitere nützliche magische Methoden

- `__call__(self, ...)`: Objekt wie Funktion aufrufbar machen
- `__del__(self)`: Destruktor
- `__contains__(self, item)`: Verhalten für `in`
- `__bool__(self)`: Boolescher Wert des Objekts

## Beispiele für eigene magische Methoden

### Callable-Objekt

```python
class Greeter:
    def __call__(self, name):
        print(f"Hello, {name}!")

g = Greeter()
g("Alice")  # Output: Hello, Alice!
```

### `in`-Operator anpassen

```python
class MyRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __contains__(self, item):
        return self.start <= item < self.stop

r = MyRange(1, 5)
print(3 in r)   # Output: True
print(6 in r)   # Output: False
```

---

## Spezielle Objektattribute (`__name__`, `__class__`, `__doc__`)

Python-Objekte und insbesondere Klassen und Funktionen verfügen über spezielle Attribute, die
Metainformationen bereitstellen:

- **`__name__`**: Name der Funktion oder Klasse.
- **`__class__`**: Die Klasse (der Typ) eines Objekts.
- **`__doc__`**: Der Docstring (Dokumentationsstring) einer Funktion, Methode oder Klasse.

### Beispiele für die Nutzung

```python
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
```

Diese Attribute sind nützlich für Debugging, automatische Dokumentation und Reflexion.

---

## Zusammenfassung

Magische Methoden und spezielle Objektattribute erlauben es, das Verhalten von eigenen Objekten
an die Erwartungen von Python anzupassen und Metainformationen über Objekte und Klassen
bereitzustellen. Dadurch können eigene Klassen mit eingebauten Funktionen und Operatoren
zusammenarbeiten und sich wie native Python-Typen verhalten.

---

## Übungen

1. Ergänze die Klasse `Point` aus den Beispielen so, dass sie auch für Subtraktion (`-`)
   den Operator unterstützt.

2. Schreibe eine Klasse `ReversedList`, die wie eine Liste funktioniert, aber das Iterieren gibt
   die Elemente in umgekehrter Reihenfolge zurück. Überlade dazu die passenden magischen Methoden.

3. Erstelle eine Klasse `HistoryDict`, die wie ein Dictionary funktioniert, aber sich merkt,
   in welcher Reihenfolge Keys hinzugefügt wurden. Implementiere dafür z.B. `__setitem__`,
   `__getitem__` und `__iter__`.

4. Passe die Klasse `MyList` so an, dass sie auch den `in`-Operator (`__contains__`) unterstützt.

5. Schreibe eine Klasse `Multiplier`, bei der das Objekt wie eine Funktion aufgerufen werden kann
   und dabei ein Argument mit einem im Objekt gespeicherten Wert multipliziert. Gib mit `__doc__`
   einen passenden Docstring an und zeige, wie man diesen abruft.
