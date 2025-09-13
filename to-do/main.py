# To-Do List Console App
# Add and remove tasks using a text-based interface

def show_menu():
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def add_task(tasks):
    # TODO: Ask user for a task and append to the list
    pass

def remove_task(tasks):
    # TODO: Show task list and allow user to remove by index
    pass

def view_tasks(tasks):
    # TODO: Display current list of tasks
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
