from flask import Flask, render_template, request, redirect
import psycopg2


# Create the Flask application instance
app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        dbname="todo_db",
        user="dbusername",
        password="dbpassword",
        host="localhost",
        port="5432"
    )

# ---------- Helper functions ----------
def load_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, done FROM tasks ORDER BY id;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "title": r[1], "done": r[2]} for r in rows]


# ---------- Routes ----------
@app.route("/")
def home():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task_route():
    # Get the task text from the form
    task_title = request.form.get("task", "").strip()

    if task_title:  # Only add if not empty
        # Insert directly into PostgreSQL
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO tasks (title, done) VALUES (%s, %s);",
            (task_title, False)
        )
        conn.commit()
        cur.close()
        conn.close()

    # Redirect back to homepage to show updated list
    return redirect("/")

@app.route("/mark/<int:task_id>")
def mark_task(task_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE tasks SET done = TRUE WHERE id = %s;",
        (task_id,)
    )
    conn.commit()
    cur.close()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM tasks WHERE id = %s;",
        (task_id,)
    )
    conn.commit()
    cur.close()
    conn.close()
    return redirect("/")

# Run the app only if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)
