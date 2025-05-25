# Python Dekoratoren: Erklärung und Beispiele

Dekoratoren sind ein leistungsfähiges Konzept in Python, das es erlaubt, Funktionen oder Methoden 
mit zusätzlicher Funktionalität zu versehen, ohne deren Quellcode zu verändern. Ein Dekorator ist 
im Grunde eine Funktion, die eine andere Funktion entgegennimmt und eine neue Funktion zurückgibt.

Dekoratoren werden häufig verwendet, um *Querschnittsfunktionen* wie Logging, Timing, Validierung 
oder Caching zu implementieren.

## Wann werden Dekoratoren ausgeführt?

Dekoratoren werden beim Laden des Moduls ausgeführt, also zu dem Zeitpunkt, an dem die Python-Datei 
importiert oder direkt ausgeführt wird. Die dekorierte Funktion wird beim Dekorieren durch die vom 
Dekorator zurückgegebene Funktion ersetzt. Das bedeutet:  
- **Dekoratoren werden nicht beim Funktionsaufruf ausgeführt, sondern einmalig beim Definieren der 
  Funktion.**  
- Der dekorierte Funktionsname verweist anschließend auf das vom Dekorator zurückgegebene Objekt.

## Beispiel 1: Einfacher Logging-Dekorator

Hier ein Beispiel, wie man einen eigenen Logging-Dekorator definiert und verwendet:

```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    """Adds two numbers."""
    return a + b

add(2, 3)
```

**Erklärung:**  
- Der Dekorator `log_decorator` nimmt eine Funktion entgegen und gibt eine neue Funktion `wrapper` 
  zurück, die vor und nach dem Aufruf der Originalfunktion Logging ausführt.
- Mit `@log_decorator` wird die Funktion `add` dekoriert.


## Beispiel 2: Verwendung von `functools.wraps`

Ohne weitere Maßnahmen "verliert" die dekorierte Funktion ihre Metadaten wie Name und Docstring. 
Mit `functools.wraps` kann man diese Metadaten erhalten:

```python
import functools

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    """Adds two numbers."""
    return a + b

print(add.__name__)      # Output: add
print(add.__doc__)       # Output: Adds two numbers.
```

**Erklärung:**  
- `@functools.wraps(func)` überträgt Name, Docstring und andere Attribute auf den Wrapper.
- Damit bleibt die Originalfunktion auch nach der Dekoration gut dokumentiert und introspektierbar.


## Beispiel 3: Timing-Dekorator

Hier ein Dekorator, der die Ausführungszeit der dekorierten Funktion misst:

```python
import time
import functools

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start:.6f} seconds.")
        return result
    return wrapper

@timeit
def slow_add(a, b):
    """Adds two numbers with artificial delay."""
    time.sleep(0.5)
    return a + b

slow_add(4, 5)
```

---

## Dekoratoren mit Argumenten

Manchmal möchte man einen Dekorator mit zusätzlichen Parametern verwenden, z.B. um das Logging-Level 
anzugeben. Dafür muss man eine zusätzliche verschachtelte Funktionsebene einführen:

```python
def log_with_level(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{level}] Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_with_level("INFO")
def add(a, b):
    return a + b

add(3, 4)
```

Hier gibt `log_with_level("INFO")` zunächst die eigentliche Dekoratorfunktion zurück, die dann wie 
gewohnt die Funktion übernimmt und wrappen kann.

## Reihenfolge mehrerer gestapelter Dekoratoren

Wendet man mehrere Dekoratoren auf eine Funktion an, werden sie **von innen nach außen** angewendet, 
d.h. der innerste Dekorator (der direkt über der Funktion steht) wird als erstes ausgeführt und 
dessen Rückgabe wird an den nächst-äußeren übergeben.

Beispiel:

```python
@deco1
@deco2
def func():
    pass
```

ist äquivalent zu:

```python
func = deco1(deco2(func))
```

Das bedeutet:  
- **Der innerste Dekorator wird zuerst angewendet, der äußerste zuletzt.**
- Die Reihenfolge der Ausführung von zusätzlicher Logik (z.B. Logging, Timing) kann sich dadurch 
  ändern.


## Zusammenfassung

- Dekoratoren sind Funktionen, die andere Funktionen annehmen und erweitern können.
- Sie werden mit der `@dekoratorname`-Syntax direkt über der Funktionsdefinition angewendet.
- Mit `functools.wraps` bleiben wichtige Funktions-Metadaten erhalten.
- Typische Anwendungsfälle sind Logging, Timing, Validierung und Caching.

---

## Übungen

1. **Logging für mehrere Funktionen:**  

   Wende den Logging-Dekorator aus Beispiel 1 auf mindestens zwei weitere eigene Funktionen an.

2. **Argumentprüfung:**  

   Schreibe einen Dekorator, der prüft, ob alle Argumente einer Funktion vom Typ `int` sind, 
   und ansonsten eine Fehlermeldung ausgibt.

3. **Timing für Methoden:**  

   Verwende den Timing-Dekorator aus Beispiel 3 auf einer Methode einer eigenen Klasse.

4. **Optionales Logging:**  

   Erweitere den Logging-Dekorator so, dass das Logging nur erfolgt, wenn ein zusätzlicher 
   Parameter (`enabled=True`) übergeben wird. Der Defaultwert für den `enabled`-Parameter soll eine
   globale Variable sein. Beobachte, was passiert, wenn diese globale Variable zwischen zwei
   Aufrufen einer dekorierten Funktion geändert wird.

5. **Dekorator-Kombination:**  

   Dekoriere eine Funktion gleichzeitig mit einem Logging- und einem Timing-Dekorator und beobachte 
   die Reihenfolge der Ausgaben.
