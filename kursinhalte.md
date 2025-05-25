# Python Aufbau Training: Kursinhalte

## Objektorientierte Programmierung (OOP) in Python

- Klassen und Objekte im Detail
- Klassenmethoden vs. statische Methoden
- Der `@property`-Dekorator und Getter/Setter-Methoden
- Vererbung und Polymorphismus
    - Methodenüberschreibung
    - Mehrfachvererbung und die `super()`-Funktion
    - Abstrakte Basisklassen (ABCs)
- Metaklassen und dynamische Klassenerstellung
    - Verständnis des Metaklassensystems in Python
    - Eigene Metaklassen erstellen
    - Anwendungsfälle für Metaklassen

## Testing, Deployment und Web-Entwicklung

- Unit Testing und testgetriebene Entwicklung (TDD)
    - Einführung in `unittest` und `pytest`
    - Schreiben von Unit-Tests für Python-Code
    - Mocking und Patching
    - Testabdeckungs-Tools
- Einführung in Web-Frameworks
    - Überblick über beliebte Frameworks: Flask vs. Django
    - Erstellen einer einfachen Web-API mit Flask
    - Einführung in RESTful APIs in Python
- Deployment-Techniken
    - Verpacken und Verteilen von Python-Code
    - Virtuelle Umgebungen und Abhängigkeitsmanagement
    - Docker für Python-Anwendungen

## Design Patterns, Threading und Multiprocessing

- Design Patterns in Python
- Funktionale Programmierung in Python
- Pythonic Design Patterns
- Threading in Python
    - Einführung in Threading: Wie es sich von Prozessen unterscheidet
    - Erstellen und Starten von Threads mit dem `threading` Modul
    - Thread-Synchronisation: Locks, RLocks, Semaphoren und Events
    - Thread-Sicherheit: Gemeinsame Daten sicher zwischen Threads verwalten
- Effizienteres Programmieren
    - Verbesserung der Skriptstrukturen
- Multiprocessing
    - Effizientes Multiprocessing
    - Problembehandlung bei der Verarbeitung großer Rasterdatensätze
    - Ressourcen effizient nutzen ohne Überlastung des PCs
    - Nutzung der Grafikkarte: Wann und wie kann sie angesteuert werden?

## Design Patterns und Best Practices

- Singleton-Pattern
- Factory-Pattern
- Strategy-Pattern
- Funktionale Programmierung in Python
    - Höherwertige Funktionen
    - Closures und Currying
- Pythonic Design Patterns
    - Idiomatische Python-Code-Praktiken
    - „The Zen of Python“ und das Schreiben von sauberem, lesbarem Code
    - Effektive Nutzung eingebauter Funktionen
- Context Manager
    - Die `with`-Anweisung
    - Erstellen von benutzerdefinierten Context Managern
    - Praktische Beispiele für Context Manager

## Asynchrone Programmierung

- Einführung in asynchrone Programmierung
    - Verständnis von Konkurrenz vs. Parallelismus
    - `asyncio` und Event-Schleifen
    - `async` und `await` Schlüsselwörter
- Asynchrone Programmierung in der Praxis
    - Erstellen von `async` Funktionen
    - Umgang mit mehreren asynchronen Aufgaben
    - Arbeiten mit `asyncio`-Aufgaben und `gather()`
- Asynchrone I/O in Python
    - Arbeiten mit asynchronen I/O-Operationen
    - Nutzung von `aiohttp` für HTTP-Anfragen
    - Dateioperationen im asynchronen Code

## Arbeiten mit großen Datensätzen

- Speicherverwaltung mit `sys` und `gc`
- Leistungsüberlegungen beim Arbeiten mit großen Dateien
- Effiziente Datenhandhabung in Python
