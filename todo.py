def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add? "))
            
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':
            print("\nTasks:")
            if not tasks:
                print("No tasks found.")
            else:
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            if not tasks:
                print("No tasks to mark as done.")
            else:
                task_index = int(input("Enter the task number to mark as done: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    print("Task marked as done!")
                else:
                    print("Invalid task number.")

        elif choice == '4':  # Update Task
            if not tasks:
                print("No tasks to update.")
            else:
                task_index = int(input("Enter the task number to update: ")) - 1
                if 0 <= task_index < len(tasks):
                    new_task = input("Enter the new task description: ")
                    tasks[task_index]["task"] = new_task
                    print("Task updated successfully!")
                else:
                    print("Invalid task number.")

        elif choice == '5':  # Delete Task
            if not tasks:
                print("No tasks to delete.")
            else:
                task_index = int(input("Enter the task number to delete: ")) - 1
                if 0 <= task_index < len(tasks):
                    deleted_task = tasks.pop(task_index)
                    print(f"Task '{deleted_task['task']}' deleted successfully!")
                else:
                    print("Invalid task number.")

        elif choice == '6':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")



main()
