def view_tasks(tasks):

    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def todo_list_app():
    tasks = []

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ")
            tasks.append(task)
            print("Task added successfully!")
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
            task_no = int(input("Enter the task number to update: ")) - 1
            if 0 <= task_no < len(tasks):
                updated_task = input("Enter the updated task: ")
                tasks[task_no] = updated_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")
        elif choice == "4":
            view_tasks(tasks)
            task_no = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_no < len(tasks):
                tasks.pop(task_no)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


todo_list_app()