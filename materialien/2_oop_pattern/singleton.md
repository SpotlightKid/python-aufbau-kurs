# Singleton-Pattern in Python

Das **Singleton-Pattern** stellt sicher, dass von einer Klasse nur eine einzige Instanz existiert.
Dieses Entwurfsmuster ist nützlich, wenn ein Objekt global verfügbar und eindeutig sein soll, z.B.
bei Konfigurationen oder Loggern. In Python kann das Singleton-Pattern auf verschiedene Arten umgesetzt
werden, z.B. durch Überschreiben der `__new__`-Methode.

## Beispiel: Singleton mit `__new__`

```python
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
```

### Erklärung

- Die Klasse hält eine Klassenvariable `_instance`, welche die einzige Instanz speichert.
- Bei jeder weiteren Instantiierung von `Singleton()` wird dieselbe Instanz zurückgegeben.

## Borg-Pattern als Alternative

Das **Borg-Pattern** (auch "Monostate") sorgt dafür, dass alle Instanzen einer Klasse denselben
Zustand (also das gleiche Attribut-Dictionary) teilen, aber unterschiedliche Instanzen existieren.
Das kann flexibler als das klassische Singleton sein.

### Beispiel: Borg-Pattern

```python
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
```

### Erklärung

- In Python werden die Attribute einer Objekt-Instanz in dem speziellen Dictionary `__dict__`
  gespeichert. Dieses Dictionary kann wie jedes andere Attribut gelesen, geschrieben und
  zugewiesen werden.
- Im Borg-Pattern teilen alle Instanzen dasselbe Attribut-Dictionary (`__dict__`), das
  gleichzeitig in dem *Klassenattribut* `_shared_state` referenziert ist.
- Änderungen bei einer Instanz sind damit bei allen anderen sichtbar.
- Es können beliebig viele Instanzen existieren.

---

## Programmierübungen

1. **Singleton `__init__`:**

   Füge in die `__init__`-Methode der Singleton-Klasse eine `print`-Meldung ein, die anzeigt,
   dass die Klasse nur einmal instantiiert wird (z.B. "Singleton instance created").

   Überprüfe das erwartete Verhalten.

2. **Borg mit mehreren Attributen:**

   Erweitere das Borg-Beispiel so, dass mehrere Attribute (z.B. `name`, `state`) von mehreren
   Instanzen gesetzt und gelesen werden und überprüfe, dass die Attributwerte jeweils in allen
   Instanzen den gleichen Wert haben (Hinweis: benutze zum Überprüfen der Annahmen `assert`.)

3. **Singleton für Konfiguration:**

    * Implementiere einen Singleton namens `Config`, der Konfigurationswerte abrufen kann und
      speichere die Definition in einem Modul (`config.py`).
    * Erstelle zwei Module (`a.py`, `b.py`) und importiere darin jeweils die Klasse `Config` aus
      dem Modul `config` und erstelle eine Instanz (`cfg = Config()`).
    * Erstelle ein Skript `main.py` und importiere darin jeweils die Instanz `cfg` aus den Modulen
      `a` und `b`:

        ```python
        from a import cfg as cfg_a
        from b import cfg as cfg_b
        ```

    * Überprüfe, ob `cfg_a` und `cfg_b` die gleiche Instanz sind und ob sich Änderungen an
      einer Instanz in der anderen widerspiegeln.
