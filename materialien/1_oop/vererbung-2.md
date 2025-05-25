# Prinzipien der Mehrfachvererbung in Python

**Mehrfachvererbung** erlaubt es in Python, dass eine Klasse von mehreren Basisklassen erbt.
Das bedeutet, eine Unterklasse kann Attribute und Methoden von mehr als einer Elternklasse übernehmen.
Python nutzt den sogenannten **Method Resolution Order (MRO)**, um zu bestimmen, in welcher
Reihenfolge Basisklassen nach Attributen und Methoden durchsucht werden. Die Funktion `super()`
ermöglicht, Methoden der nächsten Klasse gemäß MRO aufzurufen. Dies erlaubt elegante Erweiterung
und Kombination von Funktionalitäten.

## Vorteile

- **Wiederverwendbarkeit:** Code aus mehreren Basisklassen kann kombiniert werden.
- **Flexibilität:** Funktionalität kann modular und schrittweise aufgebaut werden.

## Beispielcode

```python
class A:
    def action(self):
        print("A.action start")
        super().action()
        print("A.action end")

class B:
    def action(self):
        print("B.action start")
        super().action()
        print("B.action end")

class C:
    def action(self):
        print("C.action start")
        # No super() here, last in chain
        print("C.action end")

class D(A, B, C):
    def action(self):
        print("D.action start")
        super().action()
        print("D.action end")

# Usage
d = D()
d.action()

# Ausgabe:
# D.action start
# A.action start
# B.action start
# C.action start
# C.action end
# B.action end
# A.action end
# D.action end
```

### Erklärung

- `D` erbt von `A`, `B` und `C` (in dieser Reihenfolge).
- Jede Klasse hat eine Methode `action`, die mit `super().action()` die nächste Methode im MRO aufruft.
- Die Klasse `C` ruft kein weiteres `super().action()` auf und beendet so die Aufrufkette.
- Die Reihenfolge der Methodenaufrufe folgt der Method Resolution Order (`D -> A -> B -> C`).

---

## Programmierübungen

1. **Reihenfolge ändern:**

   Ändere die Reihenfolge der Basisklassen von `D` zu `D(B, A, C)` und beobachte die Ausgabe.

2. **Neue Klasse hinzufügen:**

   Füge eine neue Klasse `E` ein, die von `D` erbt, überschreibe `action` und rufe mit `super().action()` die
   Kette fort.

3. **Funktionalität erweitern:**

   Füge in einer der Basisklassen einen weiteren Parameter zur Methode `action` hinzu, übergib diesen durch
   die Kette und passe alle Aufrufe entsprechend an.

4. **Denke über einen Anwendungsfall für Mehrfachvererbung nach:**

   Überlege dir ein Szenario, in dem Mehrfachvererbung sinnvoll eingesetzt werden kann.
   Denke dabei auch über mögliche Einschränkungen und Probleme nach, die durch Mehrfachvererbung
   entstehen können (z.B. Namenskonflikte, komplexe MRO, Diamond Problem).

   *Hinweise:*
   - Wann könnten Eigenschaften oder Methoden aus mehreren Elternklassen gleichzeitig nützlich sein?
   - Welche Schwierigkeiten könnten entstehen, wenn verschiedene Elternklassen Methoden mit
     demselben Namen haben?
   - Wie kann Python helfen, diese Probleme zu lösen?
