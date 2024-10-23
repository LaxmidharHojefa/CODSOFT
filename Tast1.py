# To-Do List application

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    def view_tasks(self):
        """View all tasks."""
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{idx}. {task['task']} - {status}")

    def update_task(self, task_number, new_task):
        """Update a task."""
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["task"] = new_task
            print(f"Task {task_number} updated to '{new_task}'.")
        else:
            print("Invalid task number.")

    def mark_completed(self, task_number):
        """Mark a task as completed."""
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        """Delete a task."""
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")

# Main code to run the application
def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            todo.update_task(task_number, new_task)
        elif choice == '4':
            task_number = int(input("Enter the task number to mark as completed: "))
            todo.mark_completed(task_number)
        elif choice == '5':
            task_number = int(input("Enter the task number to delete: "))
            todo.delete_task(task_number)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
