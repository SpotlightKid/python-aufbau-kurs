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
