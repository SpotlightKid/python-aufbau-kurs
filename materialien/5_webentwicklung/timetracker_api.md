# Time Tracker REST API

In diesem Tutorial entwickelst du Schritt für Schritt eine REST API für eine kleine
Zeiterfassungs-App mit Flask. Wir beginnen mit einer einzigen Endpoint für die
Anzeige aller Einträge und fügen dann Endpoints für das Erstellen, Löschen und
Aktualisieren von Einträgen hinzu.

---

## 1. Schritt: Minimale Flask-API mit GET aller Einträge (JSON)

Installiere Flask, falls noch nicht geschehen:

```sh
pip install flask
```

Erzeuge die Datei `app.py` mit folgendem Inhalt:

```python
from flask import Flask, jsonify

app = Flask(__name__)

# In-memory entries list
entries = [
    {'id': 1, 'description': 'Meeting', 'duration': 30},
    {'id': 2, 'description': 'Coding', 'duration': 120}
]

@app.route('/api/entries', methods=['GET'])
def get_entries():
    """Return all entries as JSON list."""
    return jsonify(entries)

if __name__ == '__main__':
    app.run(debug=True)
```

Starte die App mit:

```sh
flask run
```

Rufe im Browser oder mit `curl` auf:

```sh
curl http://localhost:5000/api/entries
```

Du siehst eine JSON-Liste aller Einträge.

---

## 2. Schritt: Endpoint zum Erstellen eines Eintrags (POST)

Wir fügen jetzt eine Route hinzu, mit der man per POST einen Eintrag anlegen kann.

Erweitere `app.py`:

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

entries = []
entry_id_counter = 1

@app.route('/api/entries', methods=['GET'])
def get_entries():
    """Return all entries as JSON list."""
    return jsonify(entries)

@app.route('/api/entries', methods=['POST'])
def create_entry():
    """Create a new time entry from JSON payload."""
    global entry_id_counter
    data = request.get_json()
    if not data or 'description' not in data or 'duration' not in data:
        abort(400, description="Missing description or duration")
    entry = {
        'id': entry_id_counter,
        'description': data['description'],
        'duration': data['duration']
    }
    entries.append(entry)
    entry_id_counter += 1
    return jsonify(entry), 201

if __name__ == '__main__':
    app.run(debug=True)
```

Teste mit `curl`:

```sh
curl -X POST -H "Content-Type: application/json" \
     -d '{"description": "Test", "duration": 10}' \
     http://localhost:5000/api/entries
```

Du erhältst den neuen Eintrag als JSON.

---

## 3. Schritt: Endpoint zum Löschen eines Eintrags (DELETE)

Jetzt kannst du Einträge per ID löschen.

In `app.py`:

```python
@app.route('/api/entries/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    """Delete an entry by id."""
    global entries
    before = len(entries)
    entries = [e for e in entries if e['id'] != entry_id]
    if len(entries) == before:
        abort(404, description="Entry not found")
    return '', 204
```

Teste mit `curl`:

```sh
curl -X DELETE http://localhost:5000/api/entries/1
```

Antwort ist leer mit Status 204, wenn erfolgreich.

---

## 4. Schritt: Endpoint zum Aktualisieren eines Eintrags (PUT)

Füge eine Route hinzu, um einen Eintrag zu ändern.

```python
@app.route('/api/entries/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id):
    """Update an entry by id."""
    data = request.get_json()
    if not data:
        abort(400, description="Missing JSON body")
    for entry in entries:
        if entry['id'] == entry_id:
            entry['description'] = data.get('description', entry['description'])
            entry['duration'] = data.get('duration', entry['duration'])
            return jsonify(entry)
    abort(404, description="Entry not found")
```

Teste mit `curl`:

```sh
curl -X PUT -H "Content-Type: application/json" \
     -d '{"description": "Updated", "duration": 60}' \
     http://localhost:5000/api/entries/2
```

Du erhältst den aktualisierten Eintrag als JSON zurück.

---

## 5. Schritt: Optional – Einzelnen Eintrag anzeigen

Wenn du möchtest, füge einen GET-Endpoint für einen einzelnen Eintrag hinzu:

```python
@app.route('/api/entries/<int:entry_id>', methods=['GET'])
def get_entry(entry_id):
    """Return a single entry by id."""
    for entry in entries:
        if entry['id'] == entry_id:
            return jsonify(entry)
    abort(404, description="Entry not found")
```

Teste mit:

```sh
curl http://localhost:5000/api/entries/2
```

---

## 6. Schritt: Kompletter Beispiel-Code

So sieht dein `app.py` jetzt aus:

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

entries = []
entry_id_counter = 1

@app.route('/api/entries', methods=['GET'])
def get_entries():
    return jsonify(entries)

@app.route('/api/entries', methods=['POST'])
def create_entry():
    global entry_id_counter
    data = request.get_json()
    if not data or 'description' not in data or 'duration' not in data:
        abort(400, description="Missing description or duration")
    entry = {
        'id': entry_id_counter,
        'description': data['description'],
        'duration': data['duration']
    }
    entries.append(entry)
    entry_id_counter += 1
    return jsonify(entry), 201

@app.route('/api/entries/<int:entry_id>', methods=['GET'])
def get_entry(entry_id):
    for entry in entries:
        if entry['id'] == entry_id:
            return jsonify(entry)
    abort(404, description="Entry not found")

@app.route('/api/entries/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    global entries
    before = len(entries)
    entries = [e for e in entries if e['id'] != entry_id]
    if len(entries) == before:
        abort(404, description="Entry not found")
    return '', 204

@app.route('/api/entries/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id):
    data = request.get_json()
    if not data:
        abort(400, description="Missing JSON body")
    for entry in entries:
        if entry['id'] == entry_id:
            entry['description'] = data.get('description', entry['description'])
            entry['duration'] = data.get('duration', entry['duration'])
            return jsonify(entry)
    abort(404, description="Entry not found")

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 7. Hinweise

- Dies ist ein einfaches Beispiel mit einer In-Memory-Liste. In einer echten App würdest du 
  eine Datenbank verwenden.
- Die API antwortet mit standardisierten HTTP-Statuscodes (z.B. 201, 204, 404).
- Du kannst Tools wie [Postman](https://www.postman.com/) oder `curl` zum Testen nutzen.
- Für die Produktion solltest du Fehlerbehandlung, Validierung und Authentifizierung verbessern.

---

## 8. Nächste Schritte

- Füge Pagination hinzu, wenn die Liste groß wird.
- Implementiere Authentifizierung (z.B. mit Flask-Login, JWT).
- Speichere die Daten in einer Datenbank (z.B. SQLite, SQLAlchemy).
- Schreibe Tests für deine API.
- Dokumentiere die API (z.B. mit OpenAPI/Swagger).
