# Prinzipien der Vererbung in der objektorientierten Programmierung mit Python

**Vererbung** ist ein zentrales Konzept der objektorientierten Programmierung. Sie erlaubt es, von
einer bestehenden Klasse (Basisklasse oder Superklasse) eine neue Klasse (Unterklasse oder
Subklasse) abzuleiten. Die Unterklasse erbt dabei Attribute und Methoden der Basisklasse und kann
sie erweitern oder überschreiben.

## Wichtige Prinzipien

- **Wiederverwendbarkeit:** Gemeinsame Funktionalität wird in der Basisklasse definiert und von
  Unterklassen wiederverwendet.
- **Erweiterbarkeit:** Unterklassen können zusätzliche Attribute oder Methoden hinzufügen.
- **Überschreiben von Methoden (Override):** Unterklassen können Methoden der Basisklasse mit einer
  eigenen Implementierung überschreiben.
- **`super()`-Funktion:** Mit `super()` kann auf die Methoden der Basisklasse zugegriffen werden.


## Beispielcode 1: Animal

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """Return a generic animal sound."""
        return "Some sound"

class Dog(Animal):
    def speak(self):
        """Return the sound of a dog."""
        return "Woof!"


# Usage
animal = Animal("Generic animal")
print(animal.name)               # Output: Generic animal
print(animal.speak())            # Output: Some sound
print(animal.__class__.__name__) # Output: Animal

dog = Dog("Fifi")
print(dog.name)               # Output: Fifi
print(dog.speak())            # Output: Woof!
print(dog.__class__.__name__) # Output: Dog
```


## Beispielcode 2: Person und Employee

Ein weiteres Beispiel für Vererbung mit einer Basisklasse `Person` und einer Unterklasse
`Employee`:

```python
class Person:

    def __init__(self, name="", age=0, gender=None):
        print(type(self))
        print(self.__class__.__name__)
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Person: name={self.name} ({self.age})"


class Employee(Person):

    def __init__(self, name="", age=0, gender=None, employee_id=None, salary=0):
        super().__init__(name=name, age=age, gender=gender)
        self.employee_id = employee_id
        self.salary = salary

    def __str__(self):
        return f"Employee: name={self.name} employee_id={self.employee_id}"


# Usage
person = Person("Alice", 30, "female")
print(person)  # Output: Person: name=Alice (30)

employee = Employee("Bob", 40, "male", employee_id="E123", salary=50000)
print(employee)  # Output: Employee: name=Bob employee_id=E123
```

### Erklärung

- Die Klasse `Employee` erbt von `Person` und erweitert sie um die Attribute `employee_id` und
  `salary`.
- Der Konstruktor von `Employee` ruft mit `super().__init__()` den Konstruktor der Basisklasse auf.
- Die Methode `__str__` wird in beiden Klassen definiert und in `Employee` überschrieben, um eine
  speziellere Darstellung zu liefern.

---

## Programmierübungen

**Zu Beispiel 1:**

1. **Füge eine weitere Unterklasse hinzu:**

   Definiere eine Klasse `Cat`, die von `Animal` erbt und die Methode `speak()` so überschreibt,
   dass sie `"Meow!"` zurückgibt.

2. **Nutze `super()` im Konstruktor:**

   Ergänze die Unterklasse `Dog` um ein zusätzliches Attribut `breed` und verwende `super()` im
   Konstruktor, um die Initialisierung der Basisklasse aufzurufen.

3. **Überlade die Methode `speak()`:**

   Passe die Methode `speak()` in der Basisklasse so an, dass sie auch den Namen des Tiers im
   Rückgabewert enthält. Die Unterklassen sollen diese Änderung übernehmen und entsprechend
   anpassen.

**Zu Beispiel 2:**

4. **Füge eine weitere Unterklasse hinzu:**

   Definiere eine Klasse `Manager`, die von `Employee` erbt und ein zusätzliches Attribut
   `department` besitzt. Überschreibe die Methode `__str__`, damit auch die Abteilung
   angezeigt wird.
