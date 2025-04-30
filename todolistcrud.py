class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "✅ Completed" if self.completed else "Not completed"
        return f"{self.description} - {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add(self, description):
        self.tasks.append(Task(description))

    def view(self):
        if not self.tasks:
            print("📭 No tasks found.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def delete(self, number):
        if self.valid(number):
            print(f"🗑️ Removed: {self.tasks.pop(number - 1).description}")

    def complete(self, number):
        if self.valid(number):
            self.tasks[number - 1].completed = True
            print("✅ Marked as completed.")

    def update(self, number, new_desc):
        if self.valid(number):
            self.tasks[number - 1].description = new_desc
            print(" Task updated.")

    def valid(self, number):
        if 1 <= number <= len(self.tasks):
            return True
        print(" Invalid task number.")
        return False


def main():
    todo = ToDoList()

    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks\n2. Add task")
        if todo.tasks:
            print("3. Delete task\n4. Complete task\n5. Update task")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            todo.view()
        elif choice == '2':
            desc = input("Enter task: ").strip()
            if desc: todo.add(desc)
        elif choice == '3' and todo.tasks:
            todo.view()
            todo.delete(input_number("Delete task number: "))
        elif choice == '4' and todo.tasks:
            todo.view()
            todo.complete(input_number("Complete task number: "))
        elif choice == '5' and todo.tasks:
            todo.view()
            num = input_number("Update task number: ")
            new_desc = input("New description: ").strip()
            if new_desc: todo.update(num, new_desc)
        elif choice == '6':
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice.")


def input_number(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print(" Please enter a valid number.")
        return -1


if __name__ == "__main__":
    main()
