# Klassenmethoden und statischen Methoden

In Python sind **Klassenmethoden** (`@classmethod`) und **statische Methoden** (`@staticmethod`)
spezielle Methodenarten, die sich in ihrer Funktionsweise und ihrem Anwendungsbereich
unterscheiden.

## Klassenmethoden (`@classmethod`)

- Sie empfangen die Klasse selbst als ersten Parameter (meist `cls` genannt).
- Sie können auf Klassenattribute und andere Klassenmethoden zugreifen oder diese ändern.
- Sie werden mit dem Decorator `@classmethod` definiert.

## Statische Methoden (`@staticmethod`)

- Sie empfangen weder die Instanz (`self`) noch die Klasse (`cls`) als ersten Parameter.
- Sie sind wie normale Funktionen, aber werden aus Gründen der Übersichtlichkeit innerhalb der
  Klasse definiert, da sie einen logischen Bezug zur Klasse haben.
- Sie werden mit dem Decorator `@staticmethod` definiert.

## Beispielcode

```python
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
```


## Klassenmethode als Factory-Methode: Beispiel mit `Color`

Eine häufige Anwendung von Klassenmethoden ist die Implementierung von "Factory"-Methoden. Hier ein
Beispiel mit einer Klasse `Color`, die eine RGB-Farbe repräsentiert und eine Factory-Methode
`from_hex` bietet, um eine Instanz aus einem CSS-ähnlichen Hex-String zu erzeugen:

```python
class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    @classmethod
    def from_hex(cls, hexstr):
        """Create instance from CSS-like hex color string (e.g. '#FFAA00')."""
        hexstr = hexstr.lstrip('#')
        red = int(hexstr[0:2], 16)
        green = int(hexstr[2:4], 16)
        blue = int(hexstr[4:6], 16)
        return cls(red, green, blue)

# Instanziierung mit Standard-Konstruktor
c1 = Color(128, 200, 255)
print(c1.red, c1.green, c1.blue)  # Ausgabe: 128 200 255

# Instanziierung mit Factory-Methode
c2 = Color.from_hex("#FFAA00")
print(c2.red, c2.green, c2.blue)  # Ausgabe: 255 170 0
```

## Zusammenfassung

- **Klassenmethoden** arbeiten mit Klassenattributen und können die Klasse verändern.

  Sie werden in Python häufig für "Factory"-Methoden verwendet.

- **Statische Methoden** sind unabhängige Hilfsfunktionen, die weder Klasse noch eine Instanz
  benötigen.

  Sie werden in Python hauptsächlich als Möglichkeit zur Strukturierung von Code und Namensräumen
  verwendet.

---

## Programmierübungen

1. **Klassenmethode erweitern:**

   Ergänze eine neue Klassenmethode `increment_class_var`, die das Klassenattribut `class_var` um
   eins (1) erhöht.

2. **Statische Methode anpassen:**

   Passe die statische Methode `add` so an, dass sie eine beliebige Anzahl von Zahlen (z.B. mit
   `*args`) addieren kann.

3. **Fabrikmethode als Klassenmethode:**

   Füge zur Klasse `Color` eine Klassenmethode `from_normalized`, die den rot-, grün- und blau-Wert
   als normalsierte Fließkommazahlen mit Wertbereich 0.0..1.0 entgegen nimmt und eine neue Instanz
   von `Color` erstellt, und die `red`, `green` und `blue` Attribute der Instanz gemäß den
   übergebenen Werten setzt, die in den Bereich 0..255 konvertiert wurden.
