@app.route('/api/entries/<int:entry_id>', methods=['GET'])
def get_entry(entry_id):
    """Return a single entry by id."""
    for entry in entries:
        if entry['id'] == entry_id:
            return jsonify(entry)
    abort(404, description="Entry not found")
