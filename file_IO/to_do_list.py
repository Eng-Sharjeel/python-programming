# >>>>> to-do-list  

# Append mode ensures that new tasks do not overwrite previous tasks.
def add_task():
    task = input("Enter a new task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def view_tasks():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines() # Read all lines into a list
            if tasks:
                print("\nYour To-Do List:")
                for index, task in enumerate(tasks, 1): # enumerate() is used to number each task starting from 1.
                    print(f"{index}. {task.strip()}")
            else:
                print("No tasks found!")
    except FileNotFoundError: # Exception handling for missing file
        print("No to-do list found!")

while True:
    choice = input("\n1. Add Task\n2. View Tasks\n3. Exit\nChoose: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        break
    else:
        print("Invalid choice! Try again.")
