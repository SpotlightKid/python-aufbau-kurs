# 10 Tipps für idiomatisches Python – Mit Beispielen

Hier findest du 10 wichtige Tipps für "pythonic" (idiomatisches) Programmieren.
Jeder Tipp hat ein Beispiel und eine kurze Erklärung.

---

## 1. Nutze Listen-Komprehension statt Schleifen für neue Listen

```python
# Statt:
squares = []
for x in range(10):
    squares.append(x * x)

# Schöner (meistens):
squares = [x * x for x in range(10)]
```
**Erklärung:**  
Listen-Komprehension ist kompakter, klarer und oft schneller als for-Schleifen zum Erzeugen 
neuer Listen.

---

## 2. Verwende sprechende Namen für Variablen und Funktionen

```python
# Nicht ideal:
def f(x):
    return x * 2

# Klarer:
def double(value):
    return value * 2
```
**Erklärung:**  
Gute Namen machen den Code leichter verständlich und wartbar.

---

## 3. Nutze "enumerate" statt Zählen mit Index-Variablen

```python
# Statt:
i = 0
for item in items:
    print(i, item)
    i += 1

# Besser:
for i, item in enumerate(items):
    print(i, item)
```
**Erklärung:**  
`enumerate` gibt direkt Index und Wert zurück – weniger Fehler und klarer.

---

## 4. Setze Standardwerte für Funktionsargumente

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")
greet("Bob", "Hi")
```
**Erklärung:**  
Standardwerte machen Funktionen vielseitiger und vermeiden viele Overloads.

---

## 5. Verwende Multiple Assignment zum Tauschen von Variablen

```python
a, b = 1, 2
a, b = b, a
print(a, b)  # 2 1
```
**Erklärung:**  
Python erlaubt elegantes Tauschen ohne Hilfsvariable.

---

## 6. Nutze "with" für Ressourcen-Management (z.B. Dateien)

```python
with open("file.txt", "w") as f:
    f.write("Hello!")
```
**Erklärung:**  
Der Kontextmanager schließt die Datei automatisch, auch bei Fehlern.

---

## 7. Setze "f-Strings" für formatierte Strings ein

```python
name = "Alice"
age = 30
print(f"{name} is {age} years old.")
```
**Erklärung:**  
f-Strings sind lesbarer und effizienter als `%` oder `str.format()`.

---

## 8. Verwende "dict.get()" für optionale Werte in Dictionaries

```python
person = {"name": "Bob"}
age = person.get("age", 0)  # 0 ist der Default
```
**Erklärung:**  
`get()` verhindert Fehler bei fehlenden Keys und ermöglicht Default-Werte.

---

## 9. Nutze Generatoren mit "yield" für große Datenmengen

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for number in count_up_to(5):
    print(number)
```
**Erklärung:**  
Generatoren sparen Speicher, da sie Werte einzeln liefern statt große Listen zu erzeugen.

---

## 10. Nutze "unpacking" für das Entpacken von Sequenzen

```python
data = (1, 2, 3)
a, b, c = data
print(a, b, c)  # 1 2 3
```
**Erklärung:**  
Unpacking macht Code lesbar und vermeidet Index-Zugriffe.

