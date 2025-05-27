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
