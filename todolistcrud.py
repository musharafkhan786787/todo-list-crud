todo_list = []

while True:
    print("--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Complete a task")
    print("5. Update task")
    print("6. Exit")

    choice = input("Choose an option 1 to 6: ")

    if choice == '1':
        if not todo_list:
            print("No tasks found.")
        else:
            counter = 1
            for task in todo_list:
                status = "Completed" if task["completed"] else "Not completed"
                print(f"{counter}. {task['Task']} - {status}")
                counter += 1

    elif choice == '2':
        task = input("Enter a new task: ").strip()
        if task:
            todo_list.append({"Task": task, "completed": False})
            print("Task added.")
        else:
            print("No task added. Please enter a valid task.")

    elif choice == '3':
        if not todo_list:
            print("No tasks to delete.")
        else:
            counter = 1
            for task in todo_list:
                status = "Completed" if task['completed'] else "Not completed"
                print(f"{counter}. {task['Task']} - {status}")
                counter += 1

            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(todo_list):
                    removed = todo_list.pop(task_num - 1)
                    print(f"Removed task: {removed['Task']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':
        try:
            compl = int(input("Please enter the number of the task you completed: "))
            if 1 <= compl <= len(todo_list):
                todo_list[compl - 1]["completed"] = True
                print("The task is now marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == '5':
        if not todo_list:
            print("No tasks to update.")
        else:
            counter = 1
            for task in todo_list:
                status = "Completed" if task['completed'] else "Not completed"
                print(f"{counter}. {task['Task']} - {status}")
                counter += 1

            try:
                task_num = int(input("Enter the task number to update: "))
                if 1 <= task_num <= len(todo_list):
                    new_task = input("Enter the new task description: ")
                    todo_list[task_num - 1]["Task"] = new_task
                    print("Task updated successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '6':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
