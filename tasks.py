import sys
import datetime
import json
import os

def load():
    if not os.path.exists("task.json"):
        return []
    with open("task.json", "r") as f:              
        return json.load(f)

def save(task):
    with open("task.json", "w") as f:
        json.dump(task, f)

def add():
    tasks = load()
    value = sys.argv[2]
    new_task = {"id": max([t["id"] for t in tasks], default = 0) + 1, "description": value, "status": "pending", "created_at": str(datetime.datetime.now())}
    tasks.append(new_task)
    save(tasks)
    print("New Task added")

def update():
    tasks = load()
    number = int(sys.argv[2])
    for t in tasks:
        if t["id"] == number:
            t["description"] = sys.argv[3]
    save(tasks)
    print("Task Updated")

def delete():
    tasks = load()
    task_id = int(sys.argv[2])
    tasks = [t for t in tasks if t["id"] != task_id]
    save(tasks)
    print("Task deleted")

def mark_in_progress():
    tasks = load()
    for t in tasks:
        if t["id"] == int(sys.argv[2]):
            t["status"] = "in-progress"
    save(tasks)
    print("marked in progress")

def mark_done():
    tasks = load()
    for t in tasks:
        if t["id"] == int(sys.argv[2]):
            t["status"] = "done"
    save(tasks)
    print("marked as done")

def list_tasks():
    tasks = load()
    for t in tasks:
        print(f"{t['id']}. {t['description']} - {t['status']}")

command = sys.argv[1]

if command == 'add':add()
elif command == 'update': update()
elif command == 'delete': delete()
elif command == 'mark_in_progress': mark_in_progress()
elif command == 'mark_done': mark_done()
elif command == 'list': list_tasks()