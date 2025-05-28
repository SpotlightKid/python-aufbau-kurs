# Überblick: Nebenläufigkeit und parallele Ausführung in Python (Standardbibliothek)

Python bietet verschiedene Möglichkeiten zur nebenläufigen (concurrent) und parallelen
(parallel) Verarbeitung direkt in der Standardbibliothek. In diesem Überblick werden die
Hauptmethoden erklärt und ihre Unterschiede sowie Einschränkungen beleuchtet.

---

## 1. Threads (`threading`-Modul)

**Threads** ermöglichen das gleichzeitige Ausführen mehrerer Aufgaben innerhalb eines einzigen
Prozesses. Jeder Thread teilt sich dabei den gleichen Speicherraum.

**Beispiel:**

```python
import threading

def worker():
    print("Worker runs in thread:", threading.current_thread().name)

t = threading.Thread(target=worker)
t.start()
t.join()
```

### Vorteile
- Einfach zu benutzen für I/O-lastige Aufgaben (z.B. Netzwerk, Dateizugriff).
- Threads laufen im selben Speicherbereich und können Daten leicht teilen.

### Nachteile
- Wegen des **Global Interpreter Lock (GIL)** können Threads in CPython nicht gleichzeitig
  Python-Bytecode ausführen. Das bedeutet: Threads sind für CPU-lastige Aufgaben ineffizient,
  da immer nur ein Thread zur Zeit Python-Code ausführen darf!
- Für echte Parallelität auf mehreren Kernen sind Threads in Python daher ungeeignet.

---

## 2. Prozesse (`multiprocessing`-Modul)

**Prozesse** ermöglichen echte Parallelität, da jeder Prozess einen eigenen Python-Interpreter
und Speicherbereich erhält.

**Beispiel:**

```python
from multiprocessing import Process

def worker():
    print("Worker runs in process")

p = Process(target=worker)
p.start()
p.join()
```

### Vorteile
- Echte Parallelität auf mehreren CPU-Kernen ist möglich.
- Keine Einschränkung durch den GIL: Jeder Prozess hat seinen eigenen Interpreter.
- Geeignet für CPU-lastige Aufgaben (z.B. Rechnen, Bildverarbeitung).

### Nachteile
- Höherer Speicherverbrauch als Threads (getrennter Speicher für jeden Prozess).
- Kommunikation zwischen Prozessen ist komplexer (z.B. via Queues, Pipes) und i.A. langsamer.
- Gemeinsame Daten müssen explizit übertragen werden.

---

## 3. Asynchrone Programmierung (`asyncio`-Modul)

**Asyncio** implementiert ein asynchrones, ereignisbasiertes Ausführungsmodell
("single-threaded concurrency"). Hierbei werden Aufgaben ("coroutines") kooperativ nacheinander
ausgeführt, indem sie explizit den Kontrollfluss abgeben.

**Beispiel:**

```python
import asyncio

async def worker():
    print("Worker runs in coroutine")
    await asyncio.sleep(1)

asyncio.run(worker())
```

### Vorteile
- Sehr effizient für viele gleichzeitige I/O-Operationen (z.B. viele Netzwerkverbindungen).
- Weniger Overhead als Threads oder Prozesse.
- Kein Kontextwechsel zwischen Betriebssystem-Threads.

### Nachteile
- Kein echter Parallelismus für CPU-lastige Aufgaben.
- Code muss explizit mit `async`/`await` geschrieben werden.
- Bibliotheken müssen asynchrones API unterstützen.

---

## 4. Weitere Mechanismen

### ThreadPoolExecutor und ProcessPoolExecutor (`concurrent.futures`)

Diese High-Level-APIs vereinfachen die Nutzung von Threads und Prozessen:

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def task(x):
    return x * x

with ThreadPoolExecutor() as executor:
    result = executor.submit(task, 5)
    print(result.result())

with ProcessPoolExecutor() as executor:
    result = executor.submit(task, 5)
    print(result.result())
```

- `ThreadPoolExecutor`: Gut für I/O-Aufgaben.
- `ProcessPoolExecutor`: Gut für CPU-Aufgaben.

---

## 5. Unterschiede Threads vs. Prozesse

| Aspekt         | Threads                   | Prozesse                  |
|----------------|--------------------------|---------------------------|
| Speicher       | geteilt                  | getrennt                  |
| Kommunikation  | direkt, Variablen        | explizit (Queue, Pipe)    |
| Parallelität   | GIL: Nein (CPython)      | Ja                        |
| Overhead       | gering                   | höher                     |
| Nutzung        | I/O-Aufgaben             | CPU-Aufgaben              |

---

## 6. Der Global Interpreter Lock (GIL)

- Der **GIL** ist ein Mechanismus in CPython, der verhindert, dass mehrere Threads gleichzeitig
  Python-Bytecode ausführen.
- Grund: Vereinfachung der Speicherverwaltung und Vermeidung von Race Conditions.
- Auswirkungen:
    - Für reine Python-Berechnungen ist echter Parallelismus mit Threads nicht möglich.
    - Für I/O-Aufgaben (Netzwerk, Datei) können Threads durch das Freigeben des GILs sinnvoll
      genutzt werden, da Python während blockierender I/O-Operationen andere Threads laufen lässt.
    - Für echte Parallelität bei rechenintensiven Aufgaben sind **Prozesse** oder externe
      (C-)Bibliotheken nötig.

---

## 7. Zusammenfassung

- **Threads**: Einfach, teilen Speicher, GIL limitiert Parallelität (gut für I/O).
- **Prozesse**: Echte Parallelität, separater Speicher (gut für CPU).
- **Asyncio**: Effizient für viele I/O-Aufgaben, kein echter Parallelismus.
- **concurrent.futures**: High-Level-Interface für Threads/Prozesse.
- **GIL**: Limitiert Threads, nicht Prozesse.

---

## 8. Wann welche Methode?

- **Viele langsame Netzwerk- oder Dateioperationen**: `threading` oder `asyncio`
- **Viele parallele CPU-intensive Aufgaben**: `multiprocessing`
- **Einfaches paralleles Mapping**: `ThreadPoolExecutor` oder `ProcessPoolExecutor`
- **Sehr viele gleichzeitige Verbindungen**: `asyncio`

---

## 9. Weiterführende Links

- [threading — Thread-based parallelism](https://docs.python.org/3/library/threading.html)
- [multiprocessing — Process-based parallelism](https://docs.python.org/3/library/multiprocessing.html)
- [asyncio — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [concurrent.futures — Launching parallel tasks](https://docs.python.org/3/library/concurrent.futures.html)
- [Global Interpreter Lock](https://wiki.python.org/moin/GlobalInterpreterLock)
