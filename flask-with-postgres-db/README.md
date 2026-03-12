# Minimalist To-Do App (Flask + PostgreSQL)

A lightweight to-do list application built with **Flask** and **PostgreSQL**.  
This app supports adding tasks, marking them as completed (with strikethrough styling), and deleting tasks.  
Unlike the earlier JSON-based version, tasks are now stored in a proper relational database for reliability and scalability.

---

## Features
- Add new tasks via a simple form
- Mark tasks as completed (completed tasks appear gray with strikethrough)
- Delete tasks
- Tasks stored in PostgreSQL (`todo_db`)
- Minimalist UI styled with `style.css`

---

## Project Structure

project/
├── app.py            # Main Flask application (PostgreSQL integrated)
├── templates/
│   └── index.html    # HTML template with Jinja placeholders
└── static/
└── style.css     # Stylesheet for the app



---

## Database Setup

### 1. Install PostgreSQL (WSL/Ubuntu)
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib -y

2. Start PostgreSQL
sudo service postgresql start

3. Create Database and User
sudo -i -u postgres
createdb todo_db
psql
```

Inside psql:
```sql
CREATE USER aswin WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE todo_db TO aswin;
\q
```

```bash
4. Create Tasks Table
psql -U aswin -d todo_db -h localhost
```

Inside psql:
```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN DEFAULT FALSE
);
\q
```
##Flask App Configuration

###Install dependencies:
```bash
pip install flask psycopg2-binary
```
### Update app.py connection details:
```python
def get_connection():
    return psycopg2.connect(
        dbname="todo_db",
        user="yourdbusername",
        password="yourdbpassword",
        host="localhost",
        port="5432"
    )
```

## Running the App
```bash
python3 app.py