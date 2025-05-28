# Asynchrone Programmierung mit `asyncio`

Dieses Tutorial zeigt dir Schritt für Schritt, wie du das Python-Modul `asyncio` für
asynchrone, nebenläufige Aufgaben verwendest. Du lernst anhand eines praktischen Beispiels
das Grundprinzip kennen und bekommst Übungen zum Selbstprobieren.

---

## 1. Einführung

Mit `asyncio` kannst du viele Aufgaben gleichzeitig abarbeiten, ohne für jede Aufgabe
einen eigenen Thread oder Prozess zu starten. Besonders bei vielen I/O-Operationen (z.B.
Netzwerkzugriffe, Wartezeiten) ist das sehr effizient.

---

## 2. Beispiel: Mehrere Webseiten asynchron abrufen

Wir schreiben ein Skript, das mehrere Webseiten gleichzeitig herunterlädt.  
Wir verwenden dazu das Paket `aiohttp`, eine asynchrone HTTP-Bibliothek.

### Voraussetzungen

Installiere `aiohttp`:

```sh
pip install aiohttp
```

Lege eine Datei `urls.txt` an, z.B.:

```
https://www.google.com
https://www.python.org
https://www.wikipedia.org
```

---

## 3. Grundstruktur: Asynchrone Funktionen

Eine asynchrone Funktion wird mit `async def` definiert und kann mit `await` auf andere
asynchrone Operationen warten.

```python
import asyncio

async def hello():
    print("Hello ...")
    await asyncio.sleep(1)
    print("... World!")

asyncio.run(hello())
```

---

## 4. Mehrere Aufgaben gleichzeitig starten

Mit `asyncio.gather` können mehrere asynchrone Aufgaben parallel ausgeführt werden.

---

## 5. Komplettes Beispiel: Asynchrones Herunterladen mit `aiohttp`

```python
import asyncio
import aiohttp

async def download_url(session, url):
    """Download a single URL and print the size of the response."""
    try:
        async with session.get(url) as response:
            content = await response.read()
            print(f"Downloaded {url} ({len(content)} bytes)")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

async def main():
    # URLs aus Datei lesen
    with open("urls.txt") as f:
        urls = [line.strip() for line in f if line.strip()]

    async with aiohttp.ClientSession() as session:
        # Aufgabenliste erzeugen
        tasks = [download_url(session, url) for url in urls]
        # Alle Aufgaben gleichzeitig starten
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
```

**Erklärung:**
- Jede URL wird als eigene asynchrone Aufgabe gestartet.
- `aiohttp.ClientSession` wird als Kontextmanager verwendet.
- Mit `await asyncio.gather(*tasks)` laufen alle Downloads quasi gleichzeitig.

---

## 6. Hinweise & Tipps

- Die asynchrone Programmierung eignet sich besonders für viele langsame I/O-Aufgaben.
- Für CPU-lastige Aufgaben ist sie **nicht** geeignet – verwende dafür `multiprocessing`.
- Viele Bibliotheken (z.B. Datenbank-, Netzwerkclients) bieten heute asynchrone APIs an.
- Nutze asynchrone Funktionen immer mit `await`.

---

## Übungen

Hier sind drei Aufgaben, mit Hinweisen zur Lösung:

### 1. **Speichere die heruntergeladenen Inhalte in Dateien**

*Hinweis:*  
Schreibe in der Funktion `download_url` den Inhalt in eine Datei, z.B. `"output_<n>.html"`.
Du kannst den Dateinamen aus der URL oder mittels einer Zählvariable ableiten.

### 2. **Miss die Gesamtzeit aller Downloads und gib sie aus**

*Hinweis:*  
Nutze das Modul `time` oder `asyncio.get_running_loop().time()`, um Zeit vor und nach
dem Download zu messen.

### 3. **Beschränke die Anzahl gleichzeitiger Downloads auf maximal 2**

*Hinweis:*  
Verwende ein `asyncio.Semaphore`, indem du vor jedem Download `await semaphore.acquire()`
aufrufst und nach dem Download `semaphore.release()` (am besten in einem `finally`-Block).
Siehe [asyncio.Semaphore-Dokumentation](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore).
