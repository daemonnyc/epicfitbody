Sure! Since you asked for a **simple app in Python**, I'll create a small example — a **To-Do List App** that runs in the terminal.  
It will allow the user to:

- Add tasks  
- View tasks  
- Remove tasks  
- Exit the app  

Here’s the sample code:

```python
# Simple To-Do List App

def display_menu():
    print("\n===== To-Do List App =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' removed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        
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
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

### How to run this app:
1. Save the code in a file named `todo_app.py`.
2. Open a terminal and run:
   ```bash
   python todo_app.py
   ```
3. Follow the on-screen menu to manage your tasks.

---

If you want, I can also make a **GUI version** of this app using `tkinter` so it has a window interface instead of running in the terminal.  
Do you want me to make the GUI version next?