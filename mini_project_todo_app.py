# mini_project_todo_app.py
# A simple command-line To-Do List app using Python and File Handling

TODO_FILE = "todos.txt"

def load_tasks():
    """Load tasks from the file."""
    try:
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save all tasks to the file."""
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nYour To-Do list is empty!\n")
        return

    print("\nYour To-Do List:")
    print("-----------------")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()


def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")


def delete_task(tasks):
    """Delete a task by number."""
    show_tasks(tasks)

    if not tasks:
        return

    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed}\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


def main():
    print("============== TODO LIST APP ==============")

    tasks = load_tasks()

    while True:
        print("Choose an option:")
        print("1. Show all tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
