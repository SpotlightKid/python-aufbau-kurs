import json

from flask import Flask, abort, render_template, request, redirect, url_for


app = Flask(__name__)
entries = []
entry_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', entries=entries, title="Meine schöne Liste")

@app.route('/add', methods=['POST'])
def add_entry():
    global entry_id_counter
    description = request.form['description']
    start = request.form['start']
    end = request.form['end']
    project = request.form.get('project')
    entry = {
        'id': entry_id_counter,
        'description': description,
        'start': start,
        'end': end,
        'project': project,
    }
    entries.append(entry)
    entry_id_counter += 1
    return redirect(url_for('index'))

@app.route('/delete/<int:entry_id>', methods=['POST'])
def delete_entry(entry_id):
    global entries
    entries = [e for e in entries if e['id'] != entry_id]
    return redirect(url_for('index'))


@app.route('/entry/<int:entry_id>')
def show_entry(entry_id):
    for e in entries:
        if e['id'] == entry_id:
            return json.dumps(e)
    else:
        raise abort(404)

if __name__ == '__main__':
    app.run(debug=True)