print()
print("1. Add task")
print("2. View tasks")
print("3. Remove task")
print("4. Exit")
print()
tasks = []

def add_task(tasks):
    task = input("Enter the task: ").strip().capitalize()
    if not task:
        print("Task cannot be empty.")
        return
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("======== Tasks=========:")
        print()
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        print()

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return
    try:
        task_number = int(input("Enter the task number to remove: ").strip())
        if task_number < 1 or task_number > len(tasks):
          print("Invalid task number.")
          return
        removed_task =  tasks.pop(task_number -1)
        print(f"{removed_task} removed successfully.")
    except ValueError:
         print("Please enter a valid number.")
    print ()
print("===== Welcome to the To-Do List App! =====")
print()
while True:
    try:
        choice = int(input("Enter your choice (1-4): ").strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if choice == 1:
        add_task(tasks)
    elif choice == 2:
        view_tasks(tasks)
    elif choice == 3:
        remove_task(tasks)
    elif choice == 4:
        print("Exiting the To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")