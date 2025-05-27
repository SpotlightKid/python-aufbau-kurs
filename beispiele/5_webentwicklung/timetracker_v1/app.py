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
