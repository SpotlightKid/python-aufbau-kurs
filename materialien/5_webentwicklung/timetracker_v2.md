## Time Tracker Version 2

```python
from datetime import datetime

from flask import Flask, redirect, render_template, request, url_for

from database import Activity, ActivityDB

TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M"

app = Flask(__name__)
db = ActivityDB("activities.db")


def parse_tags(tags_input):
    # Convert comma/whitespace separated tags to a clean, comma-separated string
    tags = [tag.strip() for tag in tags_input.replace(",", " ").split() if tag.strip()]
    return ",".join(tags)


@app.route("/", methods=["GET"])
def index():
    # List all activities (most recent first)
    activities = db.get_activities()
    return render_template("index.html", activities=activities)


@app.route("/add", methods=["POST"])
def add_activity():
    description = request.form["description"]
    start_time = request.form.get("start_time") or datetime.now().strftime(TIMESTAMP_FORMAT)

    end_time = request.form.get("end_time")
    tags = parse_tags(request.form.get("tags", ""))
    activity = Activity(
        id=None, description=description, start_time=start_time, end_time=end_time, tags=tags
    )
    activity_id = db.store_activity(activity)
    #print(activity_id, activity)
    return redirect(url_for("index"))


@app.route("/delete/<int:activity_id>", methods=["POST"])
def delete_activity(activity_id):
    db.delete_activity(activity_id)
    return redirect(url_for("index"))


@app.route("/end/<int:activity_id>", methods=["GET", "POST"])
def end_activity(activity_id):
    activity = db.get_activity(activity_id)
    if not activity:
        return redirect(url_for("index"))

    if request.method == "POST":
        end_time = datetime.now().strftime(TIMESTAMP_FORMAT)
        db.end_activity(activity_id, end_time)

        return redirect(url_for("index"))

    # Show edit form
    return render_template("edit.html", activity=activity)


if __name__ == "__main__":
    app.run(debug=True)
```