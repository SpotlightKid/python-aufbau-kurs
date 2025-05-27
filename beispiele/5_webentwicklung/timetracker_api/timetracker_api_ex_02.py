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
