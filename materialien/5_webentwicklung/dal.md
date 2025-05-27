# Datenbankzugriffsschicht (Data Access Layer) für Time Tracker

In diesem Tutorial entwickelst du Schritt für Schritt das Datenbankmodul `database.py` für eine 
Aktivitätenverwaltung mit SQLite und Python. Ziel ist es, Aktivitäten zu speichern, abzurufen, 
zu beenden und zu löschen.

---

## 1. Schritt: Datenklasse für Activity definieren

Nutze das Python-Modul `dataclasses`, um eine einfache Datenstruktur für Aktivitäten zu erstellen.

```python
from dataclasses import dataclass

@dataclass
class Activity:
    id: int | None  # None when not yet stored in DB
    description: str
    start_time: str
    end_time: str
    tags: str
```

- `id` ist `None`, solange die Aktivität noch nicht gespeichert wurde.
- Die Zeitstempel werden als Strings gespeichert (z.B. ISO-Format).

---

## 2. Schritt: Die Klasse ActivityDB und Konstruktor

Erstelle eine Klasse für die Datenbankoperationen und initialisiere die SQLite-Datenbankverbindung.

```python
import sqlite3

class ActivityDB:
    def __init__(self, db_path="activities.db"):
        self.db_path = db_path
        self._init_db()
```

- `db_path` ist standardmäßig `"activities.db"`.
- Im Konstruktor wird direkt `_init_db()` aufgerufen, um die Tabelle ggf. zu erstellen.

---

## 3. Schritt: Datenbankverbindung als Property

Füge eine Property hinzu, die bei jedem Zugriff eine neue Verbindung öffnet:

```python
@property
def conn(self):
    return sqlite3.connect(self.db_path)
```

---

## 4. Schritt: Tabelle für Aktivitäten anlegen

Implementiere `_init_db`, um die Tabelle beim ersten Start anzulegen:

```python
def _init_db(self):
    with self.conn as cnx:
        c = cnx.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS activities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                start_time TEXT NOT NULL,
                end_time TEXT,
                tags TEXT
            )
        """)
        self.conn.commit()
```

- Die Methode wird beim Initialisieren der Klasse aufgerufen.
- Achtung: `end_time` und `tags` dürfen `NULL` sein.

---

## 5. Schritt: Alle Aktivitäten abrufen

Füge eine Methode hinzu, um alle Aktivitäten nach Startzeit sortiert zurückzugeben:

```python
def get_activities(self):
    with self.conn as cnx:
        c = cnx.cursor()
        c.execute("""
            SELECT id, description, start_time, end_time, tags
            FROM activities
            ORDER BY start_time DESC
        """)
        rows = c.fetchall()
        return [Activity(*row) for row in rows]
```

---

## 6. Schritt: Eine neue Aktivität speichern

Implementiere das Speichern einer Aktivität:

```python
def store_activity(self, activity: Activity) -> int:
    with self.conn as cnx:
        c = cnx.cursor()
        c.execute("""
            INSERT INTO activities (description, start_time, end_time, tags)
            VALUES (?, ?, ?, ?)
            """,
            (activity.description, activity.start_time, activity.end_time, activity.tags),
        )
        activity_id = c.lastrowid
        self.conn.commit()
    return activity_id
```

- Nach dem Einfügen erhältst du die neue `id` mit `c.lastrowid`.

---

## 7. Schritt: Einzelne Aktivität abrufen

Füge eine Methode hinzu, um eine Aktivität anhand der ID zu laden:

```python
def get_activity(self, activity_id: int) -> Activity | None:
    with self.conn as cnx:
        c = cnx.cursor()
        c.execute(
            "SELECT id, description, start_time, end_time, tags FROM activities WHERE id = ?",
            (activity_id,),
        )
        row = c.fetchone()
    if row:
        return Activity(*row)
    return None
```

---

## 8. Schritt: Aktivität löschen

Aktivität per ID aus der Datenbank entfernen:

```python
def delete_activity(self, activity_id: int):
    with self.conn as cnx:
        c = cnx.cursor()
        c.execute("DELETE FROM activities WHERE id = ?", (activity_id,))
        self.conn.commit()
```

---

## 9. Schritt: Aktivität beenden (Endzeit setzen)

Eine Methode, um das Enddatum einer Aktivität zu speichern:

```python
def end_activity(self, activity_id: int, end_time: str):
    with self.conn as cnx:
        c = cnx.cursor()
        c.execute("""
            UPDATE activities
            SET end_time = ?
            WHERE id = ?
            """,
            (end_time, activity_id)
        )
        self.conn.commit()
```

---

## Zusammenfassung und Tipps

- Die Klasse `ActivityDB` kapselt alle Datenbankoperationen.
- Jede Methode öffnet automatisch eine neue Verbindung und schließt sie nach der Aktion.
- Die Datenklasse `Activity` macht den Umgang mit Einträgen übersichtlich.
- Für Produktivbetrieb empfiehlt sich eine persistentere Verbindung oder ein ORM wie SQLAlchemy.

---

## Beispiel: Nutzung im Python-Skript

```python
db = ActivityDB()
new = Activity(None, "Test", "2025-05-27T08:00", None, "work")
activity_id = db.store_activity(new)
print(f"Neue ID: {activity_id}")
for a in db.get_activities():
    print(a)
```

---

Mit diesen Schritten hast du ein robustes Datenbankmodul für Zeit- oder Aktivitäten-Tracking 
entwickelt!