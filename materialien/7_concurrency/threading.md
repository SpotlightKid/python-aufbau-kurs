# Concurrency mit dem `threading`-Modul

In diesem Tutorial lernst du, wie du mit dem Python-Standardmodul `threading` mehrere
Downloads gleichzeitig ausführst. Als Beispiel werden URLs aus einer Datei geladen
und parallel heruntergeladen. Anschließend siehst du, wie das gleiche mit
`ThreadPoolExecutor` funktioniert.

---

## 1. Voraussetzungen

- Python 3.x
- Das Paket `requests`:
  ```sh
  pip install requests
  ```

---

## 2. Beispiel: URLs aus einer Datei lesen

Lege eine Datei `urls.txt` an (jede Zeile eine URL):

```
https://www.google.com
https://www.python.org
https://www.wikipedia.org
```

---

## 3. Download-Funktion schreiben

Erstelle die Datei `download.py` und implementiere eine Funktion zum Herunterladen:

```python filename=download_url.py
import requests

def download_url(url):
    """Download content from a URL and print length of response."""
    try:
        response = requests.get(url)
        print(f"Downloaded {url} ({len(response.content)} bytes)")
    except Exception as e:
        print(f"Error downloading {url}: {e}")
```

---

## 4. Herunterladen mit einzelnen Threads (`threading.Thread`)

Jetzt liest du alle URLs ein und startest für jede einen eigenen Thread:

```python filename=threading_main.py
import threading

def main():
    # URLs aus Datei lesen
    with open("urls.txt") as f:
        urls = [line.strip() for line in f if line.strip()]
    threads = []
    for url in urls:
        t = threading.Thread(target=download_url, args=(url,))
        t.start()
        threads.append(t)
    # Warten, bis alle Threads fertig sind
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
```

**Erklärung:**
- Für jede URL wird ein Thread erzeugt und gestartet.
- Mit `join()` wird gewartet, bis alle fertig sind.
- Jeder Thread lädt seine URL unabhängig.

---

## 5. Das gleiche mit `ThreadPoolExecutor`

Das Modul `concurrent.futures` stellt eine High-Level-API für Thread-Pools bereit.
Dadurch wird der Code oft übersichtlicher.

```python filename=threadpool_main.py
from concurrent.futures import ThreadPoolExecutor

def main():
    with open("urls.txt") as f:
        urls = [line.strip() for line in f if line.strip()]
    # ThreadPoolExecutor mit, z.B., 4 Threads
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Alle Downloads gleichzeitig starten
        futures = [executor.submit(download_url, url) for url in urls]
        # Optional: auf Fertigstellung warten (und Fehler anzeigen)
        for future in futures:
            future.result()

if __name__ == "__main__":
    main()
```

**Erklärung:**
- `ThreadPoolExecutor` verwaltet einen Pool von Threads.
- Mit `submit()` werden Aufgaben (hier: Downloads) eingereiht.
- Mit `future.result()` werden Fehler aufgedeckt und gewartet, bis jede Aufgabe fertig ist.

---

## 6. Unterschiede und Hinweise

- Der Ansatz mit einzelnen Threads ist einfach, aber bei sehr vielen Aufgaben wird das
  Anlegen vieler Threads ineffizient.
- Mit `ThreadPoolExecutor` kannst du die maximale Anzahl an gleichzeitigen Threads begrenzen
  (`max_workers`).
- Beide Methoden eignen sich gut für I/O-lastige Aufgaben wie Netzwerk-Downloads.
- Wegen des GIL profitieren CPU-lastige Aufgaben **nicht** von Threads in Python.

---

## 7. Kompletter Beispiel-Code (`download.py`)

```python filename=download.py
import requests
import threading
from concurrent.futures import ThreadPoolExecutor

def download_url(url):
    """Download content from a URL and print length of response."""
    try:
        response = requests.get(url)
        print(f"Downloaded {url} ({len(response.content)} bytes)")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def threaded_download():
    with open("urls.txt") as f:
        urls = [line.strip() for line in f if line.strip()]
    threads = []
    for url in urls:
        t = threading.Thread(target=download_url, args=(url,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def pool_download():
    with open("urls.txt") as f:
        urls = [line.strip() for line in f if line.strip()]
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(download_url, url) for url in urls]
        for future in futures:
            future.result()

if __name__ == "__main__":
    print("Download mit threading.Thread:")
    threaded_download()
    print("\nDownload mit ThreadPoolExecutor:")
    pool_download()
```

---

## Fazit

- Für parallele I/O-Aufgaben wie Downloads sind Threads in Python sehr nützlich.
- Mit `threading.Thread` hast du viel Kontrolle, musst aber alles selbst verwalten.
- Mit `ThreadPoolExecutor` geht es meist einfacher und übersichtlicher.
- Für CPU-intensive Aufgaben verwende lieber `multiprocessing`!

---

## Übungen

Hier sind drei Aufgaben, für die du den obigen Code anpassen sollst:

1. **Speichere die heruntergeladenen Inhalte in Dateien**
   
   *Tipp:* Schreibe in der Funktion `download_url` den Inhalt in eine Datei,
   z.B. `"output_<n>.html"`, wobei `<n>` eine fortlaufende Nummer oder der Name der URL ist.

2. **Füge eine Zeitmessung für die Gesamtdauer hinzu**
   
   *Tipp:* Miss die Zeit mit `time.time()` vor und nach dem Download aller URLs
   und gib die Gesamtzeit aus.

3. **Begrenze die maximale Anzahl gleichzeitiger Downloads auf 2 im Threading-Beispiel**
   
   *Tipp:* Verwende ein `threading.Semaphore`, um nur zwei Threads gleichzeitig arbeiten zu lassen.
   Setze das Semaphore bei Thread-Start (`acquire()`), gib es am Ende des Downloads wieder frei
   (`release()`).
   Siehe [threading.Semaphore-Dokumentation](https://docs.python.org/3/library/threading.html#threading.Semaphore)