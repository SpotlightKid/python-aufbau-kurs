# Schritt-für-Schritt-Anleitung: Python-Modulprojekt mit Code-Qualitäts-Tools

Dieses Tutorial zeigt, wie du ein neues Python-Modulprojekt (`csvreader`) einrichtest
und wichtige Code-Qualitäts-Tools konfigurierst. Das Projekt wird als Git-Repository
initialisiert und mit `pre-commit` automatisiert.

---

## 1. Projektverzeichnis anlegen

```sh
mkdir csvreader
cd csvreader
```

---

## 2. Git-Repository initialisieren

```sh
git init
```

---

## 3. Python-Modulstruktur anlegen

```sh
mkdir csvreader
touch csvreader/__init__.py
mkdir tests
touch tests/test_basic.py
```

---

## 4. Virtuelle Umgebung erstellen und aktivieren

```sh
python -m venv .venv
source .venv/bin/activate
```

---

## 5. Abhängigkeiten installieren

```sh
pip install black flake8 ruff pytest pre-commit
```

Optional für Dokumentation:

```sh
pip install sphinx mkdocs
```

---

## 6. `pyproject.toml` für Tool-Konfiguration anlegen

```toml
[tool.black]
line-length = 88

[tool.ruff]
line-length = 88
select = ["E", "F", "B", "I"]
ignore = ["E203", "W503"]

[tool.isort]
profile = "black"
```

Speichere dies als `pyproject.toml` im Projektstamm.

---

## 7. Flake8-Konfiguration anlegen

```ini
[flake8]
max-line-length = 88
ignore = E203, W503
exclude = .git,__pycache__,.venv,build,dist
```

Speichere dies als `.flake8` im Projektstamm.

---

## 8. pytest-Konfiguration (optional)

```ini
[pytest]
addopts = -ra
testpaths = tests
```

Speichere dies als `pytest.ini`.

---

## 9. pre-commit konfigurieren

Erstelle `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black
  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.3.0
    hooks:
      - id: ruff
  - repo: https://github.com/pre-commit/mirrors-flake8
    rev: v7.0.0
    hooks:
      - id: flake8
```

---

## 10. pre-commit installieren und initialisieren

```sh
pre-commit install
pre-commit run --all-files
```

---

## 11. Ersten Commit machen

```sh
git add .
git commit -m "Initial commit with code quality tools"
```

---

## 12. Beispiel: Erstes Python-Modul und Test

```python name=csvreader/__init__.py
"""csvreader: Simple CSV file reader."""

def read_csv(path):
    """Read a CSV file and return the rows as list of lists."""
    with open(path, "r") as f:
        return [line.strip().split(",") for line in f]
```

```python name=tests/test_basic.py
from csvreader import read_csv

def test_read_csv(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text("a,b,c\n1,2,3\n")
    assert read_csv(str(file)) == [["a", "b", "c"], ["1", "2", "3"]]
```

## Fazit

Mit diesen Schritten hast du ein robustes, modernes Python-Modulprojekt mit
automatischer Code-Qualitätsprüfung aufgesetzt!

---

## Übungen

Hier sind fünf Aufgaben, um die Tools praktisch einzusetzen:

1. **Formatiere alle Dateien mit `black` und überprüfe das Ergebnis in Git**
   
   *Tipp:*  
   ```sh
   black .
   git diff
   ```

2. **Führe `flake8` und `ruff` aus und behebe alle gemeldeten Fehler**
   
   *Tipp:*  
   ```sh
   flake8 .
   ruff check .
   # Passe den Code an, bis keine Fehler mehr erscheinen
   ```

3. **Füge einen weiteren Testfall in die Datei `tests/test_basic.py` hinzu und führe `pytest` aus**
   
   *Tipp:*  
   ```sh
   pytest
   ```

4. **Simuliere einen fehlerhaften Commit (z.B. unformatierten Code) und beobachte, wie `pre-commit` reagiert**

   *Tipp:*  
   ```sh
   echo "def x ():\n pass" > csvreader/bad.py
   git add csvreader/bad.py
   git commit -m "bad style"
   # pre-commit blockiert oder korrigiert automatisch
   ```

5. **Erstelle eine einfache Sphinx-Dokumentation im Unterordner `docs` und baue die HTML-Doku**

   *Tipp:*  
   ```sh
   sphinx-quickstart docs
   cd docs
   make html
   ```
