
import json
import os

class ToDoList:
    def __init__(self, filename='to_do_list.json'):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()

    def update_task(self, task_number, new_task):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]['task'] = new_task
            self.save_tasks()
        else:
            print("Task number out ranged.")

    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            del self.tasks[task_number]
            self.save_tasks()
        else:
            print("Task number out ranged.")

    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]['completed'] = True
            self.save_tasks()
        else:
            print("Task number out ranged.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks):
                task_status = "Completed" if task['completed'] else "Pending"
                print(f"{idx + 1}. {task['task']} - {task_status}")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add a Task")
        print("2. Update the Task")
        print("3. Delete the added Task")
        print("4. Complete the Task")
        print("5. Show the Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            to_do_list.add_task(task)
        elif choice == '2':
            task_number = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            to_do_list.update_task(task_number, new_task)
        elif choice == '3':
            task_number = int(input("Enter the task number to delete: ")) - 1
            to_do_list.delete_task(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to complete: ")) - 1
            to_do_list.complete_task(task_number)
        elif choice == '5':
            to_do_list.show_tasks()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
