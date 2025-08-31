import json
from datetime import datetime

# Load tasks from file
try:
    with open("tasks.json", "r") as f:
        todo_list = json.load(f)
        # Convert due date strings back to datetime objects
        for item in todo_list:
            item["due"] = datetime.strptime(item["due"], "%Y-%m-%d") if item["due"] else None
except FileNotFoundError:
    todo_list = []

print("@" * 120)
print("Welcome to the TO-DO LIST program!")

while True:
    print("\nMENU")
    print("1. SHOW TASKS")
    print("2. ADD TASK")
    print("3. DELETE TASK")
    print("4. MARK TASK AS DONE")
    print("5. SEARCH TASKS")
    print("6. EXIT")

    try:
        choice = int(input("Enter a choice between 1-6: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number. 🗽")
        continue

    if choice == 1:
        if not todo_list:
            print("📭 No tasks in the list. 🚀")
        else:
            print("\n📋 Your Tasks:")
            for i, item in enumerate(todo_list, 1):
                status = "✔️" if item["done"] else "❌"
                due = item["due"].strftime("%Y-%m-%d") if item["due"] else "No due date"
                print(f"{i}. {item['task']} | Priority: {item['priority']} | Due: {due} | Status: {status}")

    elif choice == 2:
        task = input("Enter task description: ")
        priority = input("Enter priority (High/Medium/Low): ")
        due_input = input("Enter due date (YYYY-MM-DD) or leave blank: ")
        try:
            due_date = datetime.strptime(due_input, "%Y-%m-%d") if due_input else None
        except ValueError:
            print("⚠️ Invalid date format. Skipping due date.")
            due_date = None
        todo_list.append({
            "task": task,
            "priority": priority,
            "due": due_date,
            "done": False
        })
        print(f"✅ Task '{task}' added.")

    elif choice == 3:
        if not todo_list:
            print("📭 No tasks to delete.")
            continue
        try:
            index = int(input("Enter task number to delete: "))
            if 0 < index <= len(todo_list):
                removed = todo_list.pop(index - 1)
                print(f"🗑️ Task '{removed['task']}' deleted.")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")

    elif choice == 4:
        if not todo_list:
            print("📭 No tasks to mark.")
            continue
        try:
            index = int(input("Enter task number to mark as done: "))
            if 0 < index <= len(todo_list):
                todo_list[index - 1]["done"] = True
                print(f"✅ Task '{todo_list[index - 1]['task']}' marked as completed.")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")

    elif choice == 5:
        keyword = input("Enter keyword to search: ").lower()
        results = [item for item in todo_list if keyword in item["task"].lower()]
        if results:
            print("\n🔍 Search Results:")
            for i, item in enumerate(results, 1):
                status = "✔️" if item["done"] else "❌"
                due = item["due"].strftime("%Y-%m-%d") if item["due"] else "No due date"
                print(f"{i}. {item['task']} | Priority: {item['priority']} | Due: {due} | Status: {status}")
        else:
            print("🔎 No matching tasks found.")

    elif choice == 6:
        # Save tasks to file
        with open("tasks.json", "w") as f:
            # Convert datetime objects to strings
            for item in todo_list:
                item["due"] = item["due"].strftime("%Y-%m-%d") if item["due"] else None
            json.dump(todo_list, f, indent=4)
        print("👋 Thank you for using the TO-DO LIST program!")
        break

    else:
        print("❌ Invalid choice! Please enter a number between 1 and 6.")
