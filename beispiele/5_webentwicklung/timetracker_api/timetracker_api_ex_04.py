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
