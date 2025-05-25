# Prinzipien von Metaklassen in Python

**Metaklassen** sind Klassen, die andere Klassen erzeugen. In Python ist alles ein Objekt, auch Klassen
selbst. Die Metaklasse steuert, wie Klassen erstellt und konfiguriert werden. Die Standard-Metaklasse
ist `type`, aber man kann eigene Metaklassen definieren, um das Verhalten neuer Klassen anzupassen.

## Voraussetzungen zum Verständnis

- **Klassen und Objekte:** Verstehe, dass Klassen Baupläne für Objekte sind.
- **Vererbung:** Wissen, wie Klassen und Instanzen zusammenhängen.
- In Python sind alle Klassen selbst Instanzen von anderen Klassen. Die Klasse einer Klasse ist
  als *Metaklasse* dieser Klasse bekannt, und die meisten Klassen haben die Klasse `type` als
  Metaklasse.
- **`type`-Funktion:** In Python ist `type(obj)` der Typ eines Objekts, und `type` selbst ist die
  Metaklasse aller Klassen.
- **`__new__` und `__init__`:** Diese Methoden werden beim Erstellen von Klassen und Instanzen
  genutzt.

## Beispiel: Eigene Metaklasse

```python
class UpperAttrMeta(type):
    """Metaclass that makes class attributes uppercase."""

    def __new__(metaklass, name, baseclasses, members):
        uppercase_attrs = {}
        for name, value in members.items():
            if not name.startswith('__'):
                uppercase_attrs[name.upper()] = value
            else:
                uppercase_attrs[name] = value
        return super().__new__(metaklass, name, baseclasses, uppercase_attrs)


class MyClass(metaclass=UpperAttrMeta):
    foo = 'bar'

    def hello(self):
        return "hello"


# Usage
obj = MyClass()
print(hasattr(obj, 'foo'))   # Output: False
print(hasattr(obj, 'FOO'))   # Output: True
print(obj.FOO)               # Output: bar
```

### Erklärung

- Die Metaklasse `UpperAttrMeta` wandelt alle Attributnamen einer Klasse in Großbuchstaben um.
- Die Klasse `MyClass` verwendet diese Metaklasse.
- Das Attribut `foo` wird als `FOO` gespeichert, daher ist nur `obj.FOO` verfügbar.

## Typische Anwendungsfälle für Metaklassen

- Validierung oder Erweiterung von Klassenattributen beim Erstellen einer Klasse
- Automatisches Registrieren von Klassen in einer Registry
- Beeinflussung von Vererbung oder MRO
- Dynamisches Hinzufügen von Methoden zu Klassen
- Erzwingen von Namenskonventionen oder Schnittstellen

---

## Programmierübungen

1. **Attribute filtern:**

   Passe die Metaklasse so an, dass nur Attribute übernommen werden, die nicht mit `_` beginnen.

2. **Automatische Registrierung:**

   Erweitere die Metaklasse so, dass jede erzeugte Klasse automatisch in einer globalen Variable
   `class_registry` (Typ: `list`) registriert wird.

   Definiere mehrere Klassen, die diese Metaklasse benutzen und gebe am Ende der Definitionen den
   Inhalt der `class_registry` aus.

3. **Neue Methode hinzufügen:**

   Modifiziere die Metaklasse so, dass jede Klasse eine Methode `describe()` erhält, die
   alle Attributnamen der Klasse auflistet.
