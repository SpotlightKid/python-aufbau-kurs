# Factory Pattern in der objektorientierten Programmierung (Python)

Das Factory Pattern (Fabrikmuster) ist ein Entwurfsmuster, das das Erzeugen von Objekten kapselt.
Statt Objekte direkt mit `ClassName()` zu erzeugen, ruft man eine Factory-Funktion oder -Klasse auf.
Das ermöglicht mehr Flexibilität (z.B. Rückgabe unterschiedlicher Typen) und trennt die Logik zur
Objekterstellung von der Nutzung.

---

## Einfaches Factory-Pattern Beispiel

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_factory(animal_type):
    """Return an animal instance based on the string argument."""
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()
    else:
        raise ValueError(f"Unknown animal type: {animal_type}")

# Usage:
animal = animal_factory("dog")
print(animal.speak())  # Woof!
```
**Erklärung:**  
Die Funktion `animal_factory` entscheidet anhand des Arguments, welches Objekt erzeugt wird.
Der Nutzer muss die konkreten Klassen nicht kennen.

---

## Factory mit Klassenmethoden

Man kann Factories auch als Klassenmethoden einbauen:

```python
class Animal:
    @classmethod
    def create(cls, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Usage:
animal = Animal.create("cat")
print(animal.speak())  # Meow!
print(animal.__class__.__name__)  # Cat
```
**Erklärung:**  
Die Klassenmethode `create` erzeugt Objekte der passenden Unterklasse und kapselt die Logik.

---

## Wann das Factory Pattern nützlich ist

- Wenn die genaue Klasse zur Laufzeit entschieden werden soll.
- Wenn viele Details der Objekterstellung versteckt werden sollen.
- Wenn die Initialisierung komplex ist (z.B. mit vielen Parametern oder Abhängigkeiten).

---

## Vorteile

- Flexibilität bei der Objekterstellung.
- Trennung von Erzeugung und Nutzung.
- Einfaches Austauschen/Erweitern von Klassen.

---

## Übungen

1. Erweitere das erste Beispiel so, dass auch ein Tier vom Typ "bird" erzeugt werden kann,
   mit einer passenden `speak`-Methode.
2. Baue das Factory-Muster so um, dass ein Dictionary statt einer if-elif-Kette verwendet wird.
3. Ergänze das Klassenmethoden-Beispiel, sodass zusätzliche Argumente (z.B. Name des Tiers)
   an die Unterklassen weitergegeben und gespeichert werden.
