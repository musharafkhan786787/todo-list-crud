class ToDoList:
    def __init__(self):
        self.todo_list = []

    def view_tasks(self):
        if not self.todo_list:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.todo_list, 1):
                status = "Completed" if task["completed"] else "Not completed"
                print(i, "", task['Task'], "", status)

    def add_task(self):
        task = input("Enter a new task: ").strip()
        if task:
            self.todo_list.append({"Task": task, "completed": False})
            print("Task added.")
        else:
            print("You added nothing.")

    def delete_task(self):
        self.view_tasks()
        if self.todo_list:
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(self.todo_list):
                    removed = self.todo_list.pop(task_num - 1)
                    print(f"Removed task: {removed['Task']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    def complete_task(self):
        try:
            compl = int(input("Please enter the number of the task you completed: "))
            if 1 <= compl <= len(self.todo_list):
                self.todo_list[compl - 1]["completed"] = True
                print("The task is now marked as completed.")
            else:
                print("Invalid value.")
        except ValueError:
            print("Please enter a valid number.")

    def update_task(self):
        self.view_tasks()
        if self.todo_list:
            try:
                task_num = int(input("Enter the task number to update: "))
                if 1 <= task_num <= len(self.todo_list):
                    new_task = input("Enter the new task description: ").strip()
                    if new_task:
                        self.todo_list[task_num - 1]["Task"] = new_task
                        print("Task updated successfully.")
                    else:
                        print("Task description cannot be empty.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    def run(self):
        while True:
            print("\n--- To-Do List ---")
            print("1. View tasks")
            print("2. Add task")
            print("3. Delete task")
            print("4. Complete a task")
            print("5. Update task")
            print("6. Exit")

            choice = input("Choose an option (1 to 6): ")

            if choice == '1':
                self.view_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.complete_task()
            elif choice == '5':
                self.update_task()
            elif choice == '6':
                print("Bye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    todo = ToDoList()
    todo.run()
