# To-Do List Console App
# Add and remove tasks using a text-based interface

def show_menu():
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")
    pass

def remove_task(tasks):
    if len(tasks) == 0:
        print("No tasks to remove.")
        pass
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to remove: "))
        if 1 <= index <= len(tasks):
            tasks.pop(index - 1)
            print("Task removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Error: please enter a valid number")
    pass

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks added yet.")
    else:
        count = 1
        print(tasks)
        for task in tasks:
            print(count, ". ", task)
            count += 1
    pass

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
