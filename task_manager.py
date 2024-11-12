

import json

class task1:
    def __init__(self, ID, task_tittle, complete=False):
        self.ID = ID
        self.task_tittle = task_tittle
        self.complete_status = complete

    def     To_dict(self):
        return {'ID': self.ID, 'task_tittle': self.task_tittle, 'complete': self.complete_status}

    @staticmethod
    def dict1(task_data):
        return task1(task_data['ID'], task_data['task_tittle'], task_data['complete'])

class TaskManager:
    def __init__(self, file_name='out_file.json'):
        self.file_name = file_name
        self.out_file = []
        self.load()

    def load(self):
        try:
            with open(self.file_name, 'r') as file:
                task_list = json.load(file)
                self.out_file = [task1.dict1(task) for task in task_list]
        except (FileNotFoundError, json.JSONDecodeError):
            self.out_file = []


    def save(self):
        with open(self.file_name, 'w') as file:
            json.dump([task.    To_dict() for task in self.out_file], file)
            
    def add(self, task_tittle):
        ID = len(self.out_file) + 1
        task = task1(ID, task_tittle)
        self.out_file.append(task)
        self.save()
        print(f"Task '{task_tittle}' added successfully.")

    def view(self):
        if not self.out_file:
            print("No tasks available.")
        else:
            for task in self.out_file:
                status = "Complete" if task.complete_status else "Pending"
                print(f"ID: {task.ID} | task_tittle: {task.task_tittle} | Status: {status}")

    def remove(self, ID):
        self.out_file = [task for task in self.out_file if task.ID != ID]
        self.save()
        print(f"Task ID {ID} deleted successfully.")

    def edit_status(self, ID):
        for task in self.out_file:
            if (task.ID == ID ):
                task.complete_status = True
                self.save()
                print(f"Task ID {ID,task.task_tittle} marked as complete.")
                
        print(f"No task found with ID {ID}.")

    def run(self):
        while True:
        
            abc = input("\n1 for add  task \n2 for view task\n3 for delete task\n4 edit status\n5 to stop\nChoose an option: ")

            if abc == '1':
                task_tittle = input(" give tittle name  ")
                self.add(task_tittle)
            elif abc == '2':
                self.view()
            elif abc == '3':
                try:
                    ID = int(input("enter ID to remove task "))
                    self.remove(ID)
                except ValueError:
                    print("enter valid ID")
            elif abc == '4':
                try:
                    ID = int(input("enter the ID to change status"))
                    self.edit_status(ID)
                except ValueError:
                    print("enter valid ID")
            elif abc == '5':
                print("complete the process")
                break
            else:
                print("\nenter in range off 1 to 5 ")

if __name__ == "__main__":
    task_manager_1 = TaskManager()
    task_manager_1.run()
