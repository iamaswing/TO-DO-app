# Minimalist To-Do App

A lightweight to-do list application built with **Flask** and **JSON** for storage.  
The app supports adding tasks, marking them as completed (with strikethrough styling), and deleting tasks.

---

## Features
- Add new tasks via a simple form
- Mark tasks as completed (completed tasks appear gray with strikethrough)
- Delete tasks
- Tasks are stored in a `tasks.json` file (no database required)
- Minimalist UI styled with `style.css`

---

## Project Structure
project/
├── app.py            # Main Flask application
├── tasks.json        # JSON file storing tasks
├── templates/
│   └── index.html    # HTML template with Jinja placeholders
└── static/
└── style.css     # Stylesheet for the app

---

## Getting Started

### 1. Install dependencies
Make sure you have Python 3 installed. Then install Flask:

```bash
pip install flask

python app.py

By default, the app runs at http://127.0.0.1:5000/