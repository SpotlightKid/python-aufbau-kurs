# Objekte und OO-Programmierung - Review Grundlagen

## Ausgangslage

```python
employees = {
    "name 1": {
        "salary": ...,
        "skills": [...],
    },
    "name 2": {
        "salary": ...,
        "skills": [...],
    },
    ...
}
```

## Klasse als Kapselung eines Datensatzes

```python
class Employee:
    name = "Unknown"
    gehalt = 0
    skills = []
```

Benutzung:

```python
employee1 = Employee()
print(employee1.name)
print(employee1.gehalt)
print(employee1.skills)

employee2 = Employee()
print(employee2.name)
print(employee2.gehalt)
print(employee2.skills)

employee1.name = "Joe Doe"
print(employee1.name)
print(employee2.name)
```

## Objekt-Initialisierung (`__init__`)

```python
class Employee:
    def __init__(self):
        print("Init!")

employee3 = Employee()
```

### Instanzattribute initialisieren

```python
class Employee:
    def __init__(self, name="", gehalt=0, skills=[]):
        self.name = name
        self.gehalt = gehalt

        if skills is None:
            self.skills = []
        else:
            self.skills = skills

employee4 = Employee("Joe Doe", 2000, [])
print(type(employee4))
print(employee4.name)
print(employee4.gehalt)
print(employee4.skills)

employee5 = Employee("Jane Oh", 3000, ["marketing"])
print(employee5.name)
print(employee5.gehalt)
print(employee5.skills)
```

Geht nicht, weil die Klasse kein Attribut "name" definiert:

```python
print(Employee.name)
```


## "Magische" Methoden (Einführung)

### String-Repräsentation

#### Exkurs: "f-Strings" und `format()`

```python
s = "Hallo, {}"
print(s.format("Welt"))

s = "{}, {}"
print(s.format("Guten Tag", "Welt"))

s = "{name}, {grussformel}"
print(s.format(grussformel="Guten Tag", name="Welt"))

grussformel="Guten Tag"
name="Welt"
print(f"{name}, {grussformel}")


def sagehallo(name):
    # 'grussformel' ist eine globale variable!
    print(f"{grussformel}, {name}")

sagehallo("Welt")
```

#### `__str__`-Methode

```python
class Employee:
    def __init__(self, name="", gehalt=0, skills=[]):
        self.name = name
        self.gehalt = gehalt

        if skills is None:
            self.skills = []
        else:
            self.skills = skills

    def __str__(self):
        s  = [f"Employee '{self.name}'"]
        s.append(f"    gehalt: {self.gehalt}")
        s.append(f"    skills:")
        for skill in self.skills:
            s.append(f"        - {skill}")
        return "\n".join(s)
```

Die String-Repräsentation folgt diesem Muster:

```
Employee 'name':
    gehalt: XXX
    skills:
        - skill 1
        - skill 2
```

Test:

```python
employee7 = Employee(name="Bob Smith", skills=["software development", "it support"])
print(employee7)
```


## Methoden, Datenkapselung und Typprüfung

```python
class Employee:
    def __init__(self, name="", gehalt=0, skills=[]):
        self.name = name
        self.gehalt = gehalt

        if skills is None:
            self.skills = []
        else:
            self.skills = skills

    def set_gehalt(self, neues_gehalt):
        if not isinstance(neues_gehalt, int):
            raise TypeError("gehalt muss ein Integer sein")
        if neues_gehalt < 4000:
            self.gehalt = neues_gehalt
        else:
            raise ValueError("Zu hohes gehalt!")


employee8 = Employee()
# Ok
employee8.gehalt = 5000
# Auch ok (aber unsinnig!)
employee8.gehalt = "feuchter Händedruck"

print(employee8.gehalt)
# ValueError!
employee8.set_gehalt(4000)
# TypeError!
employee8.set_gehalt("feuchter Händedruck")
```
