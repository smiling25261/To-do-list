file = "tasks.txt"

def add_task():
    task = input("Enter the task: ")
    with open(file, "a") as f:
        f.write(task + "\n")
    print("Task added successfully")

def view_tasks():
    try:
        with open(file, "r") as f:
            tasks = f.readlines()

        if len(tasks) == 0:
            print("No tasks found")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(i, ".", task.strip())
    except FileNotFoundError:
        print("No tasks found")

def delete_task():
    try:
        with open(file, "r") as f:
            tasks = f.readlines()

        if len(tasks) == 0:
            print("No tasks to delete")
            return

        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(i, ".", task.strip())

        num = int(input("Enter task number to delete: "))

        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)

            with open(file, "w") as f:
                for task in tasks:
                    f.write(task)

            print("Task deleted successfully")
        else:
            print("Invalid task number")

    except FileNotFoundError:
        print("There are no tasks to be deleted")

while True:
    print("\n~ TO DO LIST ~")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Save and Exit")

    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Saving and exiting program...")
        break
    else:
        print("Invalid choice. Please enter 1-4.")