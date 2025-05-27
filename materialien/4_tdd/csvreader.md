# Test Driven Development: ein einfacher CSV Reader

Hier ist ein Tutorial, wie du mit Test-Driven Development (TDD) ein einfaches
`csvreader.py`-Modul baust. Wir nutzen `pytest` in einem separaten Testmodul
`test_csvreader.py`. Nach jedem Schritt werden die notwendigen Änderungen an beiden
Dateien gezeigt.  
**Nach jeder Änderung führst du `pytest` aus, um zu sehen, dass der neue Test zunächst
fehlschlägt, und nach der Implementierung die Tests alle grün sind.**

---

## Einführung und Beispiel: Die API von `csvreader`

Das Modul `csvreader` stellt eine einfache, flexible Schnittstelle zum Parsen von CSV-Dateien mit 
beliebigem Trennzeichen bereit. Du kannst damit Zeilen aus einer Datei oder einer beliebigen 
iterierbaren Quelle einlesen und optional eine eigene `row_factory`-Funktion verwenden, um jede 
Zeile in ein gewünschtes Format (z.B. Liste, Tupel, benanntes Tupel) zu bringen.

### Beispiel für die Verwendung

```python filename=csvreader_usage.py
from csvreader import CSVReader

with open("data.csv") as f:
    parser = CSVReader(f, separator=";", row_factory=tuple)
    for row in parser:
        print(row)

# Ausgabe:
# ('a', 'b', 'c')
# ('1', '2', '3')
```

**API-Überblick:**

- Erstes Argument: das Dateiobjekt (oder jedes iterierbare Objekt mit Zeilen).
- `separator`: Das Zeichen, das die Werte in einer Zeile trennt (z.B. `,` oder `;`).
- `row_factory`: Eine Funktion, mit der jede Zeile verarbeitet wird (z.B. `list`, `tuple` oder 
  eine eigene Funktion). Standard ist `None` (liefert Listen zurück).
- Iteriere über das `CSVReader`-Objekt, um die geparsten Zeilen zu erhalten.

Dieses einfache API-Design erlaubt es dir, CSV-Daten flexibel und pythonisch zu verarbeiten.

---

## **1. Schritt: Test für die Existenz der Klasse schreiben**

**test_csvreader.py**

```python filename=step_1/test_csvreader.py
def test_csvreader_exists():
    from csvreader import CSVReader
    parser = CSVReader([])
    assert parser is not None
```

**csvreader.py**

```python filename=step_1/csvreader.py
class CSVReader:
    pass
```

**Test ausführen:**  
```sh
pytest
```
Du solltest sehen, dass der Test fehlschlägt, weil `CSVReader` noch keine Argumente annimmt.

**Jetzt die Implementierung anpassen und erneut testen:**  
Nachdem du die Klasse ergänzt hast, läuft der Test durch.

---

## **2. Schritt: Initialisierung und Separator testen**

**test_csvreader.py** (neuer Test)

```python filename=step_2/test_csvreader.py
def test_init_separator():
    from csvreader import CSVReader
    parser = CSVReader([], separator=";")
    assert parser.separator == ";"
    assert parser.row_factory == None
    assert parser.fileobj == []
```

**Test ausführen:**  
```sh
pytest
```
Der neue Test schlägt fehl, da der Konstruktor noch nicht implementiert ist.

**csvreader.py** (anpassen)

```python filename=step_2/csvreader.py
class CSVReader:
    def __init__(self, fileobj, separator=",", row_factory=None):
        self.fileobj = fileobj
        self.separator = separator
        self.row_factory = row_factory
```

**Test erneut ausführen:**  
```sh
pytest
```
Jetzt sollten beide Tests erfolgreich sein.

---

## **3. Schritt: Iterierbarkeit testen**

**test_csvreader.py** (neuer Test)

```python filename=step_3/test_csvreader.py
def test_iterable():
    from csvreader import CSVReader
    parser = CSVReader([])
    assert hasattr(parser, "__iter__")
```

**Test ausführen:**  
```sh
pytest
```
Der neue Test schlägt fehl, da `__iter__` noch nicht existiert.

**csvreader.py** (anpassen)

```python filename=step_3/csvreader.py
class CSVReader:
    def __init__(self, fileobj, separator=",", row_factory=None):
        self.fileobj = fileobj
        self.separator = separator
        self.row_factory = row_factory

    def __iter__(self):
        return self
```

**Test erneut ausführen:**  
```sh
pytest
```
Alle Tests sollten bestehen.

---

## **4. Schritt: Zeilen parsen aus einer Liste (simulate file input)**

Wir fügen die Möglichkeit hinzu, eine Liste von Zeilen als Input zu geben
(zum Testen ohne echte Datei).

**test_csvreader.py** (neuer Test)

```python filename=step_4/test_csvreader.py
def test_parse_lines():
    from csvreader import CSVReader
    lines = ["a,b,c", "1,2,3"]
    parser = CSVReader(iter(lines))
    result = list(parser)
    assert result == [["a", "b", "c"], ["1", "2", "3"]]
```

**Test ausführen:**  
```sh
pytest
```
Der Test schlägt fehl (StopIteration oder NotImplementedError).

**csvreader.py** (anpassen)

```python filename=step_4/csvreader.py
class CSVReader:
    def __init__(self, fileobj, separator=",", row_factory=None):
        self.fileobj = fileobj
        self.separator = separator
        self.row_factory = row_factory
        self._iter = iter(self.fileobj)

    def __iter__(self):
        return self

    def __next__(self):
        line = next(self._iter)
        row = line.strip().split(self.separator)
        if self.row_factory:
            row = self.row_factory(row)
        return row
```

**Test erneut ausführen:**  
```sh
pytest
```
Jetzt sollten alle Tests bestehen.

---

## **5. Schritt: Unterstützung für verschiedene Separatoren testen**

**test_csvreader.py** (neuer Test)

```python filename=step_5/test_csvreader.py
def test_different_separator():
    from csvreader import CSVReader
    lines = ["a;b;c", "1;2;3"]
    parser = CSVReader(iter(lines), separator=";")
    result = list(parser)
    assert result == [["a", "b", "c"], ["1", "2", "3"]]
```

**Test ausführen:**  
```sh
pytest
```
Alle Tests inklusive des neuen sollten erfolgreich durchlaufen.

---

## **6. Schritt: row_factory unterstützen**

**test_csvreader.py** (neuer Test)

```python filename=step_6/test_csvreader.py
def test_row_factory():
    from csvreader import CSVReader
    lines = ["a,b,c", "1,2,3"]
    parser = CSVReader(iter(lines), row_factory=tuple)
    result = list(parser)
    assert result == [("a", "b", "c"), ("1", "2", "3")]
```

**Test ausführen:**  
```sh
pytest
```
Auch dieser Test sollte ohne weitere Änderungen bestehen.

---

## **7. Schritt: Dateiunterstützung (echter Dateitest)**

**test_csvreader.py** (neuer Test)

```python filename=step_7/test_csvreader.py
def test_from_file(tmp_path):
    from csvreader import CSVReader
    with open("data.csv", "w") as csv:
        csv.write("a,b,c\n1,2,3\n")
    
    with open("data.csv") as csv:
        parser = CSVReader(csv)
        result = list(parser)
        assert result == [["a", "b", "c"], ["1", "2", "3"]]
```

**Test ausführen:**  
```sh
pytest
```
Der Test sollte grün sein, da file-like Objekte schon unterstützt werden.

---

## **Fazit**

Mit jedem Schritt hast du einen neuen Test geschrieben, den Code angepasst und grünes Licht
abgewartet. So wächst das Modul sicher und nachvollziehbar!