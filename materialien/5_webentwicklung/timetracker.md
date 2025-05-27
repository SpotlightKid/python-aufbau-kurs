# Schritt-für-Schritt-Tutorial: Eine einfache Flask-App für Zeiteinträge

In diesem Tutorial entwickelst du Schritt für Schritt eine kleine Flask-App zur Verwaltung von 
Zeiteinträgen. Du beginnst mit einer statischen Startseite, fügst Templates hinzu, ergänzt eine 
Funktion zum Hinzufügen von Einträgen und schließlich eine Funktion zum Löschen von Einträgen.

---

## 1. Schritt: Minimale Flask-App mit statischer Index-Seite

Installiere Flask, falls noch nicht geschehen:

```sh
pip install flask
```

Erzeuge eine Datei `app.py` mit folgendem Inhalt:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Time Entries</h1><p>Hier erscheint später die Liste.</p>"

if __name__ == '__main__':
    app.run(debug=True)
```

Starte die App mit:

```sh
flask run --reload --debug
```

Öffne [http://localhost:5000/](http://localhost:5000/) im Browser.  
Du siehst eine einfache statische HTML-Seite.

---

## 2. Schritt: Templates mit Jinja2 verwenden

Lege ein Verzeichnis `templates` an und darin die Datei `index.html`:

```
myproject/
├── app.py
└── templates/
    └── index.html
```

Inhalt von `index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Time Entries</title>
</head>
<body>
    <h1>Time Entries</h1>
    <p>Hier erscheint später die Liste.</p>
</body>
</html>
```

Passe die Route in `app.py` an, um das Template zu rendern:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

Starte die App erneut (wenn Du `--reload` und `--debug` verwendest, reicht es, die Seite im Browser neu zu laden).  
Jetzt wird das HTML aus der Template-Datei angezeigt.

---

## 3. Schritt: Start einer einfachen Eintragsliste

Erweitere das Template und die App, um eine Liste von Einträgen (noch statisch) anzuzeigen.

In `app.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)

entries = [
    {'id': 1, 'description': 'Meeting', 'duration': 30},
    {'id': 2, 'description': 'Coding', 'duration': 120}
]

@app.route('/')
def index():
    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
```

`index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Time Entries</title>
</head>
<body>
    <h1>Time Entries</h1>
    <table>
        <tr><th>Description</th><th>Duration</th></tr>
        {% for entry in entries %}
        <tr>
            <td>{{ entry.description }}</td>
            <td>{{ entry.duration }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

Jetzt zeigt die Seite eine statische Tabelle der Einträge an.

---

## 4. Schritt: Template mit Bootstrap und Blöcken anpassen

Erstelle ein Basis-Template `base.html` für das Layout:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Time Entries</title>
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
<div class="container mt-4">
    {% block content %}{% endblock %}
</div>
</body>
</html>
```

Passe `index.html` so an, dass es von `base.html` erbt:

```html
{% extends "base.html" %}
{% block content %}
<h2>Time Entries</h2>
<table class="table">
    <tr><th>Description</th><th>Duration (minutes)</th></tr>
    {% for entry in entries %}
    <tr>
        <td>{{ entry.description }}</td>
        <td>{{ entry.duration }}</td>
    </tr>
    {% endfor %}
</table>
{% endblock %}
```

---

## 5. Schritt: Einträge dynamisch hinzufügen

Füge ein Formular zum Hinzufügen von Einträgen hinzu.

`index.html` (am Ende von `{% block content %}`):

```html
<h3>Add Entry</h3>
<form method="post" action="{{ url_for('add_entry') }}">
    <input name="description" placeholder="Description" required>
    <input name="duration" type="number" min="1" placeholder="Duration" required>
    <button type="submit" class="btn btn-primary">Add</button>
</form>
```

Erweitere `app.py` um die Route `/add`:

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
entries = []
entry_id_counter = 1

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    global entry_id_counter
    description = request.form['description']
    duration = request.form['duration']
    entry = {
        'id': entry_id_counter,
        'description': description,
        'duration': duration
    }
    entries.append(entry)
    entry_id_counter += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

Jetzt kannst du neue Zeiteinträge über das Formular hinzufügen.

---

## 6. Schritt: Einträge löschen

Erweitere die Tabelle in `index.html` um eine Löschfunktion:

```html
<table class="table">
    <tr><th>Description</th><th>Duration (minutes)</th><th>Action</th></tr>
    {% for entry in entries %}
    <tr>
        <td>{{ entry.description }}</td>
        <td>{{ entry.duration }}</td>
        <td>
            <form action="{{ url_for('delete_entry', entry_id=entry.id) }}"
                  method="post" style="display:inline;">
                <button class="btn btn-danger btn-sm">Delete</button>
            </form>
        </td>
    </tr>
    {% endfor %}
</table>
```

Füge in `app.py` die Route zum Löschen hinzu:

```python
@app.route('/delete/<int:entry_id>', methods=['POST'])
def delete_entry(entry_id):
    global entries
    entries = [e for e in entries if e['id'] != entry_id]
    return redirect(url_for('index'))
```

---

## 7. Schritt: App komplettieren

Am Ende sieht dein `app.py`-Code so aus:

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
entries = []
entry_id_counter = 1

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    global entry_id_counter
    description = request.form['description']
    duration = request.form['duration']
    entry = {
        'id': entry_id_counter,
        'description': description,
        'duration': duration
    }
    entries.append(entry)
    entry_id_counter += 1
    return redirect(url_for('index'))

@app.route('/delete/<int:entry_id>', methods=['POST'])
def delete_entry(entry_id):
    global entries
    entries = [e for e in entries if e['id'] != entry_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

Dein `index.html` sieht dann so aus:

```html
{% extends "base.html" %}
{% block content %}
<h2>Time Entries</h2>
<table class="table">
    <tr><th>Description</th><th>Duration (minutes)</th><th>Action</th></tr>
    {% for entry in entries %}
    <tr>
        <td>{{ entry.description }}</td>
        <td>{{ entry.duration }}</td>
        <td>
            <form action="{{ url_for('delete_entry', entry_id=entry.id) }}"
                  method="post" style="display:inline;">
                <button class="btn btn-danger btn-sm">Delete</button>
            </form>
        </td>
    </tr>
    {% endfor %}
</table>
<h3>Add Entry</h3>
<form method="post" action="{{ url_for('add_entry') }}">
    <input name="description" placeholder="Description" required>
    <input name="duration" type="number" min="1" placeholder="Duration" required>
    <button type="submit" class="btn btn-primary">Add</button>
</form>
{% endblock %}
```

Das `base.html`-Layout findest du weiter oben.

---

## 8. Fazit

In wenigen Schritten hast du eine Flask-App entwickelt, die Zeiteinträge anzeigt, hinzufügt und
löscht – mit sauber getrenntem HTML dank Templates.  
Du kannst nun auf dieser Basis weitere Features hinzufügen, z.B. Validierung, Speicherung oder
Benutzerauthentifizierung.

---

## Übungen: Flask-App erweitern

Hier findest du drei praktische Aufgaben, um deine Flask-App weiter auszubauen. Jede Übung enthält
einen Tipp zur Lösung.

### 1. Route für Eintrag als JSON

**Aufgabe:**  
Füge eine neue Route hinzu, die einen einzelnen Eintrag als JSON zurückgibt, wenn dieser per ID
abgerufen wird, z.B. `/entry/3`.

**Tipp:**  
- Nutze `from flask import jsonify`.
- Verwende einen URL-Parameter für die ID (`/entry/<int:entry_id>`).
- Suche den Eintrag in der Liste und gib ihn als JSON mit `jsonify(entry)` zurück.
- Siehe [Flask-Dokumentation zu jsonify](https://flask.palletsprojects.com/en/latest/api/#flask.json.jsonify)


### 2. Erfolgsmeldungen mit `flash` beim Erstellen und Löschen

**Aufgabe:**  
Zeige nach dem Hinzufügen oder Löschen eines Eintrags eine Nachricht auf der Website an, z.B.
"Eintrag hinzugefügt" oder "Eintrag gelöscht".

**Tipp:**  
- Importiere `flash` und `get_flashed_messages` aus Flask.
- Rufe `flash(...)` in der jeweiligen Route auf.
- Zeige die Nachrichten im Template (z.B. in `base.html`) mit einer Schleife über
  `get_flashed_messages()`.
- Siehe [Flask-Dokumentation zu flash](https://flask.palletsprojects.com/en/latest/quickstart/#message-flashing)


### 3. Sortier-Links für die Eintragsliste

**Aufgabe:**  
Füge Links hinzu, mit denen die Eintragsliste nach Beschreibung oder Dauer sortiert werden kann.

**Tipp:**  
- Übergib einen Query-Parameter wie `?sort=name` oder `?sort=duration` an die Startseite.
- Lese den Parameter in der Index-Route mit `request.args.get("sort")` aus.
- Sortiere die Liste vor dem Rendern entsprechend mit `sorted()`.
- Setze die Links als `<a href="{{ url_for('index', sort='name') }}">Sort by name</a>`.
- Siehe [Flask-Dokumentation zu request.args](https://flask.palletsprojects.com/en/latest/api/#flask.Request.args)
