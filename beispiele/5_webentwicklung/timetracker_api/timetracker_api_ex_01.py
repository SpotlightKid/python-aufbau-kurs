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
