# Python-Paket mit Hatch bauen

Dieses Tutorial zeigt dir, wie du ein Python-Modul, das aus einem einzigen Package-Verzeichnis 
(z.B. `mypkg/`) besteht, mit [Hatch](https://hatch.pypa.io/) verpackst. Zusätzlich lernst du, wie 
du das Paket mit den Tools [`build`](https://pypa-build.readthedocs.io/) und 
[`installer`](https://installer.readthedocs.io/) bauen und installieren kannst.

---

## 1. Voraussetzungen

- **Python** (empfohlen: 3.8+)
- **Hatch** installieren  
  ```sh
  pip install hatch
  ```
- Optional:  
  **build** und **installer** installieren  
  ```sh
  pip install build installer
  ```

---

## 2. Neues Projektverzeichnis anlegen

Lege ein neues Verzeichnis an und wechsle hinein:

```sh
mkdir myproject
cd myproject
```

---

## 3. Das Projekt mit Hatch initialisieren

Starte die Initialisierung:

```sh
hatch init
```

Folge dem Dialog und gib z.B. `mypkg` als Namen für dein Package an, wenn dein Verzeichnis
so heißen soll.

---

## 4. Projektstruktur prüfen

Nach der Initialisierung sieht die Struktur so aus:

```
myproject/
├── mypkg/
│   └── __init__.py
└── pyproject.toml
```

---

## 5. pyproject.toml anpassen

Öffne die `pyproject.toml` und prüfe folgende Einträge:

```toml
[project]
name = "mypkg"
version = "0.1.0"
description = "Mein tolles Python-Paket"
authors = [{ name = "Dein Name", email = "du@example.com" }]
readme = "README.md"
requires-python = ">=3.8"
license = { text = "MIT" }

[tool.hatch.build.targets.wheel]
packages = ["mypkg"]
```

Passe ggf. die Werte an deinen Paketnamen und deine Infos an.

---

## 6. Paket mit Hatch bauen

Starte den Build-Prozess:

```sh
hatch build
```

Das erzeugt z.B. eine Wheel-Datei im Ordner `dist/`.

---

## 7. Paket testen

Installiere das Paket in einer virtuellen Umgebung:

```sh
pip install dist/mypkg-0.1.0-py3-none-any.whl
```

Teste die Installation:

```python
import mypkg
print(mypkg.__version__)
```

## Hinweise

- Das Package-Verzeichnis (`mypkg/`) kann beliebig viele Module enthalten.
- Weitere Einstellungen und Möglichkeiten findest du in der [Hatch-Dokumentation](https://hatch.pypa.io/latest/).

---

## Alternative: Paket mit `python -m build` bauen und mit `python -m installer` installieren

### Paket bauen mit `build`

Stelle sicher, dass `build` installiert ist:

```sh
pip install build
```

Starte den Build:

```sh
python -m build
```

Dadurch entstehen ein `.whl` und ein `.tar.gz` im `dist/`-Verzeichnis.

### Paket installieren mit `installer`

Installiere `installer`, falls nötig:

```sh
pip install installer
```

Installiere das gebaute Wheel (ersetze ggf. den Dateinamen):

```sh
python -m installer dist/mypkg-0.1.0-py3-none-any.whl
```

---

## Vorteile der verschiedenen Ansätze

- **Hatch:**  
  - Bietet viele Features (Versionierung, Umgebungen, Testen, Publishing).
  - Praktisch für komplette Entwicklungs- und Veröffentlichungs-Workflows.

- **build + installer:**  
  - `build` und `installer` sind standardisierte Tools des Python Packaging Authority (PyPA).
  - Sehr einfach, wenn du nur bauen und lokal installieren möchtest.
  - Besonders nützlich in CI/CD-Skripten, da sie keine Abhängigkeiten auflösen.

- **pip install ...:**  
  - Nutzt das Standard-Tool für Benutzerinstallation.
  - Löst automatisch Abhängigkeiten auf.
  - Ist die empfohlene Methode für Endnutzer.

---

## Fazit

Mit `hatch` kannst du Pakete modern entwickeln und veröffentlichen.  
Mit `build` und `installer` nutzt du die PyPA-Standards für das Bauen und Installieren.  
Für Endnutzer und Abhängigkeitsverwaltung ist `pip install` meist am komfortabelsten.

---

## Übungen:

Hier findest du drei praktische Übungen, um deine Kenntnisse im Umgang mit `pyproject.toml` und 
Hatch zu vertiefen.

### 1. Laufzeitabhängigkeit (run-time dependency) hinzufügen

**Aufgabe:**  
Füge deinem Projekt eine Abhängigkeit zu einem externen PyPI-Modul (z.B. `requests`) hinzu, 
sodass es bei der Installation automatisch mit installiert wird.

**Tipp:**  
- Suche in der Sektion `[project]` deiner `pyproject.toml` nach dem Feld für Abhängigkeiten.
- Trage dort das gewünschte Modul (z.B. `requests`) ein.

### 2. Entry-Point für ein Kommandozeilen-Skript definieren

**Aufgabe:**  
Stelle dein Paket so ein, dass nach der Installation ein Konsolenbefehl (z.B. `mypkg-cli`) 
verfügbar ist, der eine Funktion aus deinem Paket aufruft.

**Tipp:**  
- Suche in der Sektion `[project]` nach dem Feld für `scripts`.
- Lege einen Namen für das Skript fest und verweise auf deine Funktion nach dem Schema 
  `modulpfad:funktion`.
- Beispiel:  
  ```toml
  [project.scripts]
  mypkg-cli = "mypkg.cli:main"
  ```

### 3. Konfigurations-Sektionen für black und isort hinzufügen

**Aufgabe:**  
Füge deiner `pyproject.toml` Konfigurationsabschnitte für die Tools `black` und `isort` hinzu, 
um die Formatierung und das Sortieren der Imports zu steuern.

**Tipp:**  
- Sieh in der Dokumentation von [black](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#where-black-looks-for-the-configuration)
  und [isort](https://pycqa.github.io/isort/docs/configuration/options/) nach, wie die Einstellungen in der 
  `pyproject.toml` definiert werden.
- Beispiel:
  ```toml
  [tool.black]
  line-length = 88

  [tool.isort]
  profile = "black"
  ```
