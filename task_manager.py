

import json

class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'completed': self.completed}

    @staticmethod
    def from_dict(task_data):
        return Task(task_data['id'], task_data['title'], task_data['completed'])

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                task_list = json.load(file)
                self.tasks = [Task.from_dict(task) for task in task_list]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []


    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)
            
    def add_task(self, title):
        task_id = len(self.tasks) + 1
        task = Task(task_id, title)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                status = "Completed" if task.completed else "Pending"
                print(f"ID: {task.id} | Title: {task.title} | Status: {status}")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()
        print(f"Task ID {task_id} deleted successfully.")

    def complete_task(self, task_id):
        for task in self.tasks:
            if (task.id == task_id ):
                task.completed = True
                self.save_tasks()
                print(f"Task ID {task_id,task.title} marked as completed.")
                
        print(f"No task found with ID {task_id}.")

    def run(self):
        while True:
            print("\nTask Manager")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Mark Task as Complete")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                title = input("Enter task title: ")
                self.add_task(title)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    self.delete_task(task_id)
                except ValueError:
                    print("Invalid ID.")
            elif choice == '4':
                try:
                    task_id = int(input("Enter task ID to mark as complete: "))
                    self.complete_task(task_id)
                except ValueError:
                    print("Invalid ID.")
            elif choice == '5':
                print("Exiting Task Manager.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()
