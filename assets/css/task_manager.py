import sqlite3
import sys
from tabulate import tabulate 

# Connect to SQLite database
conn = sqlite3.connect('tasks.db')
c = conn.cursor()

# Create tasks table if not exists
c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT
    )
''')
conn.commit()

def add_task(title, description=None):
    """Add a new task to the database."""
    c.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (title, description))
    conn.commit()
    print("Task added successfully!")

def view_tasks():
    """View all tasks in the database."""
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    if tasks:
        print("\nAll Tasks:")
        print(tabulate(tasks, headers=['ID', 'Title', 'Description']))
    else:
        print("No tasks found.")

def update_task(task_id, title, description=None):
    """Update an existing task in the database."""
    c.execute('UPDATE tasks SET title = ?, description = ? WHERE id = ?', (title, description, task_id))
    conn.commit()
    print("Task updated successfully!")

def delete_task(task_id):
    """Delete a task from the database."""
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    print("Task deleted successfully!")

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            add_task(title, description)

        elif choice == '2':
            view_tasks()

        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter updated title: ")
            description = input("Enter updated description (optional): ")
            update_task(task_id, title, description)

        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)

        elif choice == '5':
            print("Exiting Task Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

# Close database connection
conn.close()
