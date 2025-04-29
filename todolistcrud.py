# todo_oop.py

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def update_description(self, new_description):
        self.description = new_description

    def __str__(self):
        status = "Completed" if self.completed else "Not completed"
        return f"{self.description} - {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("✅ Task added.")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks found.")
        else:
            print("\n📋 Task List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            print(f"🗑️ Removed task: {removed.description}")
        else:
            print(" Invalid task number.")

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_completed()
            print("✅ Task marked as completed.")
        else:
            print(" Invalid task number.")

    def update_task(self, task_number, new_description):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].update_description(new_description)
            print(" Task updated successfully.")
        else:
            print(" Invalid task number.")


def main():
    todo = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Complete a task")
        print("5. Update task")
        print("6. Exit")

        choice = input("Choose an option (1 to 6): ")

        if choice == '1':
            todo.view_tasks()

        elif choice == '2':
            desc = input("Enter a new task: ").strip()
            if desc:
                todo.add_task(desc)
            else:
                print(" Empty task not added.")

        elif choice == '3':
            todo.view_tasks()
            try:
                number = int(input("Enter the task number to delete: "))
                todo.delete_task(number)
            except ValueError:
                print(" Please enter a valid number.")

        elif choice == '4':
            todo.view_tasks()
            try:
                number = int(input("Enter the number of the task to complete: "))
                todo.complete_task(number)
            except ValueError:
                print(" Please enter a valid number.")

        elif choice == '5':
            todo.view_tasks()
            try:
                number = int(input("Enter the task number to update: "))
                new_desc = input("Enter the new task description: ").strip()
                if new_desc:
                    todo.update_task(number, new_desc)
                else:
                    print(" Task description cannot be empty.")
            except ValueError:
                print(" Please enter a valid number.")

        elif choice == '6':
            print(" Goodbye!")
            break

        else:
            print(" Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
