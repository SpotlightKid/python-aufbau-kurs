# Wichtige Python-Tools für Code-Qualitätssicherung

In diesem Dokument werden die wichtigsten Tools für Code-Qualitätssicherung in Python-Projekten
vorgestellt: Linter, Code-Formatter, Unit-Testing, Coverage und Dokumentation.

---

## 1. Flake8

**Was ist das?**  
`flake8` ist ein Linter, der den Python-Code auf Stil- und Syntaxfehler sowie
potenzielle Bugs prüft. Er kombiniert PyFlakes, pycodestyle und McCabe Complexity Checker.

**Warum benutzen?**  
Automatische Erkennung von Fehlerquellen und Einhaltung von Style-Guides
fördert sauberen und wartbaren Code.

**Konfiguration** (`setup.cfg` oder `.flake8`):

```ini
[flake8]
max-line-length = 88
ignore = E203, W503
exclude = .git,__pycache__,build,dist
```

**Ausführen:**

```sh
flake8 .
```

---

## 2. Pylint

**Was ist das?**  
`pylint` prüft Code auf Fehler, Stil, Best Practices und kann auch eine Punktzahl für
die Codequalität liefern.

**Warum benutzen?**  
Sehr gründlicher Linter, deckt auch strukturelle Codeprobleme auf.

**Konfiguration** (`.pylintrc`):

```ini
[MASTER]
ignore=build,dist,venv
[FORMAT]
max-line-length=88
[MESSAGES CONTROL]
disable=C0114,C0115,C0116  # disables missing docstring warnings
```

**Ausführen:**

```sh
pylint my_package/
```

---

## 3. Ruff

**Was ist das?**  
`ruff` ist ein sehr schneller Linter und Fixer, der viele Checks (auch von flake8) abdeckt.

**Warum benutzen?**  
Sehr schnell, deckt viele Regeln ab und kann viele Probleme direkt automatisch beheben.

**Konfiguration** (`pyproject.toml`):

```toml
[tool.ruff]
line-length = 88
select = ["E", "F", "B", "I"]
ignore = ["E203", "W503"]
```

**Ausführen:**

```sh
ruff check .
# oder mit automatischer Korrektur:
ruff check . --fix
```

---

## 4. Black

**Was ist das?**  
`black` ist ein Code-Formatter, der Python-Code automatisch nach festen Regeln formatiert.

**Warum benutzen?**  
Sorgt für ein einheitliches Format und erspart Diskussionen über Code-Stil.

**Konfiguration** (`pyproject.toml`):

```toml
[tool.black]
line-length = 88
target-version = ['py38']
```

**Ausführen:**

```sh
black .
```

---

## 5. pytest

**Was ist das?**  
`pytest` ist ein beliebtes Framework für Unit- und Integrationstests in Python.

**Warum benutzen?**  
Einfach zu schreiben, leistungsfähig, viele Plugins, automatische Testentdeckung.

**Beispiel-Test** (`tests/test_example.py`):

```python
def test_add():
    assert 1 + 1 == 2
```

**Ausführen:**

```sh
pytest
```

---

## 6. Coverage.py

**Was ist das?**  
`coverage` misst, wie viel Prozent des Codes durch Tests abgedeckt werden.

**Warum benutzen?**  
Hilft, ungetesteten Code zu finden und die Testqualität zu verbessern.

**Konfiguration** (`.coveragerc`):

```ini
[run]
branch = True
source = my_package
omit =
    tests/*
[report]
show_missing = True
skip_covered = True
```

**Ausführen:**

```sh
coverage run -m pytest
coverage report -m
coverage html
```

---

## 7. Sphinx

**Was ist das?**  
`sphinx` ist ein Tool zur Generierung von Projektdokumentation aus ReStructuredText oder
Markdown und Docstrings.

**Warum benutzen?**  
Automatische, konsistente, durchsuchbare und schöne Dokumentation.

**Konfiguration** (`docs/conf.py`, generiert durch `sphinx-quickstart`):

```python
project = 'My Project'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
```

**Ausführen:**

```sh
cd docs
make html
```

---

## 8. MkDocs

**Was ist das?**  
`mkdocs` erstellt eine statische Projekt-Webseite aus Markdown-Dateien.

**Warum benutzen?**  
Schnell und einfach für benutzerfreundliche Entwicklerdokumentation.

**Konfiguration** (`mkdocs.yml`):

```yaml
site_name: My Project
nav:
  - Home: index.md
  - API: api.md
theme: readthedocs
```

**Ausführen:**

```sh
mkdocs build
mkdocs serve
```

---

## 9. pre-commit

**Was ist das?**  
`pre-commit` ermöglicht das Ausführen von Prüf- und Formatierungs-Tools vor jedem Commit,
z.B. Black, Flake8, Ruff, isort.

**Warum benutzen?**  
Verhindert, dass schlechter oder unformatierter Code ins Repository gelangt.

**Konfiguration** (`.pre-commit-config.yaml`):

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
```

**Installieren und ausführen:**

```sh
pre-commit install
pre-commit run --all-files
```

---

## 10. Git

**Was ist das?**  
`git` ist das verbreitetste Versionskontrollsystem für Quellcode.

**Warum benutzen?**  
Ermöglicht Zusammenarbeit, Nachvollziehbarkeit, Branching und Code-Reviews.

**Typische Befehle:**

```sh
git init
git add .
git commit -m "Initial commit"
git status
git log
git diff
```

---

## 11. Weitere nützliche Tools

### isort

Sortiert automatisch Imports nach festen Regeln.

Konfiguration (`pyproject.toml`):

```toml
[tool.isort]
profile = "black"
```

Ausführen:

```sh
isort .
```

### mypy

Statischer Typprüfer für Python, prüft Typannotationen.

Konfiguration (`mypy.ini`):

```ini
[mypy]
ignore_missing_imports = True
strict = True
```

Ausführen:

```sh
mypy my_package/
```

---

## 12. Zentrale Konfiguration mit `pyproject.toml`

Viele der genannten Tools unterstützen die Konfiguration direkt in der Datei `pyproject.toml`.
Dies ist ein moderner, zentraler Ort für Build- und Tool-Konfigurationen in Python-Projekten.

**Vorteile:**
- Weniger Konfigurationsdateien im Projekt.
- Einheitlicher Aufbau, leicht verständlich für neue Entwickler.
- Einfachere Weitergabe und Wiederverwendung von Einstellungen.

**Beispiele für Konfigurationen in `pyproject.toml`:**

```toml
[tool.black]
line-length = 88

[tool.isort]
profile = "black"

[tool.ruff]
line-length = 88
select = ["E", "F", "B", "I"]

[tool.pytest.ini_options]
addopts = "-ra"
testpaths = ["tests"]
```

Nicht alle Tools (z.B. Flake8, Pylint, Coverage) unterstützen `pyproject.toml` vollständig,
aber die meisten modernen Werkzeuge wie Black, isort, Ruff und Pytest können so zentral
und bequem konfiguriert werden.

---

## Fazit

Diese Tools helfen, die Codequalität und Wartbarkeit in Python-Projekten erheblich zu
verbessern. Viele davon lassen sich gut über `pre-commit` automatisieren und in CI/CD-Pipelines
einbinden.