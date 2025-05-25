# Das Strategy-Pattern in der objektorientierten Programmierung

Das **Strategy-Pattern** (Strategie-Muster) ist ein Verhaltensmuster, das es ermöglicht, das
Verhalten eines Algorithmus zur Laufzeit auszuwählen. Anstatt einen einzelnen Algorithmus direkt zu
implementieren, erhält der Code zur Laufzeit Anweisungen, welchen Algorithmus er verwenden soll.
Dadurch wird der Algorithmus von dem Kontext entkoppelt, in dem er verwendet wird, was den Code
flexibler und leichter wartbar macht.

## Hauptmerkmale

- **Kapselung:** Jeder Algorithmus ist in einer eigenen Klasse gekapselt, die ein gemeinsames
  Interface teilt.
- **Austauschbarkeit:** Algorithmen können zur Laufzeit gewechselt werden, ohne die Context-Klasse
  zu verändern.
- **Open/Closed-Prinzip:** Neue Algorithmen können hinzugefügt werden, ohne bestehenden Code zu
  ändern.

## Beispiel in Python

Angenommen, wir möchten einen Text-Formatter implementieren, der Text auf verschiedene Weisen
formatieren kann (z.B. Groß- oder Kleinschreibung):

```python
from typing import Protocol

# Strategy Interface
class TextFormatter(Protocol):
    def format(self, text: str) -> str:
        return text

# Concrete Strategies
class UpperCaseFormatter:
    def format(self, text: str) -> str:
        return text.upper()

class LowerCaseFormatter:
    def format(self, text: str) -> str:
        return text.lower()

# Context
class TextEditor:
    def __init__(self, formatter: TextFormatter):
        self.formatter = formatter

    def set_formatter(self, formatter: TextFormatter):
        self.formatter = formatter

    def publish(self, text: str) -> str:
        return self.formatter.format(text)

# Usage
editor = TextEditor(UpperCaseFormatter())
print(editor.publish("Hello World"))  # Ausgabe: HELLO WORLD

editor.set_formatter(LowerCaseFormatter())
print(editor.publish("Hello World"))  # Ausgabe: hello world
```


### Wie es funktioniert

- `TextFormatter` ist ein Protokoll (Interface), das die `format`-Methode definiert.
- `UpperCaseFormatter` und `LowerCaseFormatter` sind konkrete Strategien, die verschiedene
  Formatierungsalgorithmen implementieren.
- `TextEditor` ist die Context-Klasse; sie verwendet eine Formatter-Strategie, die zur Laufzeit
  durch `set_formatter()` gewechselt werden kann.

---

## Programmierübungen

1. **Füge einen Title Case Formatter hinzu:**

   Implementiere eine neue Strategie namens `TitleCaseFormatter`, die den Text im Title Case
   (erster Buchstabe jedes Wortes großgeschrieben) formatiert. Passe das Nutzungsbeispiel an, um
   den Wechsel zu diesem Formatter zu demonstrieren.

2. **Unterstütze mehrere Ausgabestile:**

   Modifiziere die Klasse `TextEditor`, sodass sie eine Liste von Formatter-Strategien akzeptiert
   und diese nacheinander auf jede Texteingabe anwendet.

3. **Formatter-Auswahl durch Benutzereingabe:**

   Schreibe Code, der dem Benutzer erlaubt, den Formatter (uppercase, lowercase oder title case)
   zur Laufzeit per Konsoleneingabe auszuwählen und den gewählten Algorithmus auf einen vom
   Benutzer eingegebenen String anzuwenden.
