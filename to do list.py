def display_menu():
    """Displays the main menu."""
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    """Displays all tasks."""
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    """Adds a new task."""
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")

def update_task(tasks):
    """Updates an existing task."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the updated task: ").strip()
            if new_task:
                tasks[task_num - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Updated task cannot be empty!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task(tasks):
    """Deletes a task."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main function to run the application."""
    tasks = []
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                view_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                update_task(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice! Please select a valid option.")
        except ValueError:
            print("Please enter a valid number!")

if _name_ == "_main_":
    main()