@app.route('/api/entries/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    """Delete an entry by id."""
    global entries
    before = len(entries)
    entries = [e for e in entries if e['id'] != entry_id]
    if len(entries) == before:
        abort(404, description="Entry not found")
    return '', 204
