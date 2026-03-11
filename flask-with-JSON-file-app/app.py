from flask import Flask, render_template, request, redirect
import json
import os

# Create the Flask application instance
app = Flask(__name__)

TASKS_FILE = "tasks.json"

# ---------- Helper functions ----------
def load_tasks():
    """Load tasks from JSON file, return as list of dicts."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    """Save list of tasks back to JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


# Define a single route for the homepage
@app.route("/")
def home():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    # Get the task text from the form
    task_title = request.form.get("task", "").strip()

    if task_title:  # Only add if not empty
        tasks = load_tasks()

        # Generate a new ID (simple approach: length + 1)
        new_id = len(tasks) + 1

        # Create new task dictionary
        new_task = {"id": new_id, "title": task_title, "done": False}

        # Append and save
        tasks.append(new_task)
        save_tasks(tasks)

    # Redirect back to homepage to show updated list
    return redirect("/")

@app.route("/mark/<int:task_id>")
def mark_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            break
    save_tasks(tasks)
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks = load_tasks()
    # Filter out the task with the matching ID
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    return redirect("/")

# Run the app only if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)
