# Der "property"-Decorator in Python

Der **`property`-Decorator** in Python ermöglicht es, Methoden einer Klasse wie Attribute zu
verwenden. Dadurch können **Getter**, **Setter** und **Deleter** für private Attribute definiert
werden, ohne die Schnittstelle der Klasse nach außen zu verändern. Dies ist besonders nützlich, um
die Kapselung zu gewährleisten und die interne Implementierung zu verstecken.

Referenz-Dokumentation: https://docs.python.org/3/library/functions.html#property


## Vorteile von `property`

- **Kapselung:** Ermöglicht die Kontrolle darüber, wie auf Attribute zugegriffen wird.
- **Kompatibilität:** Die API bleibt nach außen gleich, auch wenn interne Änderungen vorgenommen
  werden.
- **Validierung:** Setter können genutzt werden, um Werte vor der Zuweisung zu überprüfen.
- **Konvertierung:** Setter können genutzt werden, um Werte vor der Zuweisung zu konvertieren.
- **Dynaisierung:**
    * Setter können verwendet werden, um abgeleitete Attribute automatisch beim Setzen einer
      Property zu berechnen und zu setzen.
    * Getter können verwendet werden, um Werte "on-demand" zu berechnen und zurückzugeben, z.B.
      Werte, die sich aus anderen Attributen oder der Kombination mehrerer Attribute ableiten.
    * Getter können verwendet werden, um Werte "on-demand" von externen Quellen abzurufen
      (z.B. Datenbank, Netzwerk, Dateisystem usw.) und zurückzugeben.

## Beispielcode

```python
class Person:
    def __init__(self, name):
        self._name = name  # private attribute

    @property
    def name(self):
        """The name property getter."""
        return self._name

    @name.setter
    def name(self, value):
        """The name property setter."""
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

# Usage
p = Person("Alice")
print(p.name)     # Accesses _name via the getter
print(Person.name.__doc__)

p.name = "Bob"    # Sets _name via the setter
print(p.name)     # Output: Bob

# p.name = ""     # Would raise ValueError: Name cannot be empty
```

### Erklärung

- Mit `@property` wird die Methode `name()` zum **Getter** für das Attribut `name`.
- Mit `@name.setter` wird die Methode `name()` als **Setter** definiert.
- Der Zugriff auf `name` sieht aus wie ein normaler Attribut-Zugriff, intern wird aber die
  entsprechende Methode aufgerufen.

---

## Programmierübungen

1. **Füge einen Deleter hinzu:**

   Ergänze die Klasse `Person` um einen `@name.deleter`, sodass das Attribut `_name` auf
   `None` gesetzt wird, wenn `del p.name` aufgerufen wird.

   **Achtung:** Was passiert, wenn versucht wird, direkt `p.name = None` zu setzen?

2. **Validierung erweitern:**

   Passe den Setter so an, dass der Name ein String aus mindestens zwei Bestandteilen (Vor- und
   Nachname, getrennt durch Leerzeichen) sein muss.

3. **Weitere Property:**

   Füge eine weitere Property `age` hinzu, die nur positive ganzzahlige Werte akzeptiert, und
   implementiere Getter und Setter dafür.

4. **Abgeleitete Property:**

   Füge einen Getter für eine weitere Property `firstname` hinzu, die den ersten Bestandteil des
   Namens zurückgibt.

