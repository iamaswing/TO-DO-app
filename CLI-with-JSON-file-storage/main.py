import json
import os

TASKS_FILE = "tasks.json"

# --- Persistence Helpers ---
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# --- Core Functions ---
def add_task(tasks, title):
    tasks.append({"title": title, "status": "pending"})
    save_tasks(tasks)
    print(f'Task added: "{title}"')

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['title']} [{task['status']}]")

def mark_task(tasks, number):
    try:
        index = number - 1
        tasks[index]["status"] = "done"
        save_tasks(tasks)
        print(f'Task {number} marked as done.')
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task(tasks, number):
    try:
        index = number - 1
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f'Task deleted: \"{removed["title"]}\"')
    except (IndexError, ValueError):
        print("Invalid task number.")

# --- Command Parser ---
def parse_command(tasks, raw_input):
    parts = raw_input.strip().split(" ", 1)
    command = parts[0].lower()

    if command == "add":
        if len(parts) > 1:
            add_task(tasks, parts[1])
        else:
            print("Please provide a task title.")
    elif command == "list":
        list_tasks(tasks)
    elif command == "mark":
        if len(parts) > 1 and parts[1].isdigit():
            mark_task(tasks, int(parts[1]))
        else:
            print("Please provide a valid task number.")
    elif command == "delete":
        if len(parts) > 1 and parts[1].isdigit():
            delete_task(tasks, int(parts[1]))
        else:
            print("Please provide a valid task number.")
    elif command == "exit":
        return False
    else:
        print("Unknown command. Try: add, list, mark, delete, exit.")
    return True

# --- Main Loop ---
def main():
    tasks = load_tasks()
    print("Welcome to the To-Do App!")
    print("Commands: add <task>, list, mark <number>, delete <number>, exit")
    while True:
        raw_input = input("> ")
        if not parse_command(tasks, raw_input):
            break

if __name__ == "__main__":
    main()
