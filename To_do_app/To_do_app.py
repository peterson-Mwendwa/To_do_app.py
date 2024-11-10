import json
from datetime import datetime, timedelta

# Task structure: Each task has a name, priority, category, due date, and completion status.
tasks = []

# Function to load tasks from a JSON file (Data Persistence)
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            global tasks
            tasks = json.load(file)
            print("💾 Tasks loaded successfully!")
    except FileNotFoundError:
        print("🗂️ No saved tasks found. Starting a new list.")

# Function to save tasks to a JSON file (Data Persistence)
def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)
        print("💾 Tasks saved successfully!")

# Function to display tasks with color-coded priorities and emojis for categories
def display_tasks():
    if not tasks:
        print("📭 No tasks in your to-do list. Add some tasks to get started!")
    else:
        print("\n📝 Your To-Do List:")
        for index, task in enumerate(tasks):
            priority_color = {
                "High": "\033[91m",  # Red
                "Medium": "\033[93m",  # Yellow
                "Low": "\033[92m",  # Green
            }.get(task['priority'], "\033[0m")
            icon = {
                "Work": "💼",
                "Home": "🏠",
                "Study": "🏫",
            }.get(task['category'], "📂")
            status = "✅" if task['completed'] else "❌"
            print(f"{index + 1}. {priority_color}{task['name']} | {task['priority']} Priority{icon} | Due: {task['due_date']} | Status: {status}\033[0m")

# Function to add a new task with due date and other attributes
def add_task():
    name = input("✏️ Enter the task name: ")
    priority = input("🔺 Set priority (High, Medium, Low): ")
    category = input("📂 Enter the task category (e.g., Work, Home, Study): ")
    due_date = input("📅 Enter due date (YYYY-MM-DD): ")
    task = {
        "name": name,
        "priority": priority,
        "category": category,
        "due_date": due_date,
        "completed": False,
    }
    tasks.append(task)
    print(f"✅ Task '{name}' added successfully!\n")

# Function to mark a task as complete
def mark_task_complete():
    display_tasks()
    if tasks:
        try:
            task_num = int(input("✅ Enter the task number to mark as complete: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num]["completed"] = True
                print(f"✅ Task '{tasks[task_num]['name']}' marked as complete!\n")
            else:
                print("🚫 Invalid task number!")
        except ValueError:
            print("🚫 Please enter a valid number!")

# Function to search tasks by name or filter by category or priority
def search_tasks():
    search_term = input("🔍 Enter search term or category/priority filter: ").lower()
    results = [task for task in tasks if search_term in task["name"].lower() or
               search_term == task["priority"].lower() or search_term == task["category"].lower()]
    if results:
        print("\n🔍 Search Results:")
        for task in results:
            print(f" - {task['name']} | Priority: {task['priority']} | Category: {task['category']} | Due: {task['due_date']} | Status: {'✅' if task['completed'] else '❌'}")
    else:
        print("🚫 No tasks found matching that term.")

# Function to delete a task
def delete_task():
    display_tasks()
    if tasks:
        try:
            task_num = int(input("🗑️ Enter the task number to delete: ")) - 1
            if 0 <= task_num < len(tasks):
                removed_task = tasks.pop(task_num)
                print(f"🗑️ Task '{removed_task['name']}' deleted successfully!\n")
            else:
                print("🚫 Invalid task number!")
        except ValueError:
            print("🚫 Please enter a valid number!")

# Function to display tasks sorted by priority
def prioritize_tasks():
    if not tasks:
        print("📭 No tasks to prioritize!")
    else:
        sorted_tasks = sorted(tasks, key=lambda x: {"High": 1, "Medium": 2, "Low": 3}.get(x["priority"], 4))
        print("\n🔺 Prioritized To-Do List:")
        for task in sorted_tasks:
            print(f" - {task['name']} | {task['priority']} Priority | Due: {task['due_date']} | Status: {'✅' if task['completed'] else '❌'}")

# Function to show the main menu and handle user actions
def main_menu():
    load_tasks()
    while True:
        print("\n🌟 To-Do List App Menu 🌟")
        print("1️⃣ Add a Task")
        print("2️⃣ Mark Task as Complete")
        print("3️⃣ Delete a Task")
        print("4️⃣ View All Tasks")
        print("5️⃣ Prioritize Tasks")
        print("6️⃣ Search Tasks")
        print("0️⃣ Exit\n")

        choice = input("Select an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            mark_task_complete()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            prioritize_tasks()
        elif choice == "6":
            search_tasks()
        elif choice == "0":
            save_tasks()
            print("👋 Thank you for using the To-Do List App! Goodbye!")
            break
        else:
            print("🚫 Invalid choice. Please try again.\n")

# Run the main menu
if __name__ == "__main__":
    print("🎉 Welcome to the Enhanced To-Do List App! 🎉\n")
    main_menu()
