class ToDoList:

    todo = {}

    def add_task(self, name, description):
        self.todo[name] = description

    def add_new_task(self):
        answer = input("\nDo you want to add a new task? (Y/N)")
        if answer.upper() == 'Y':
            new_task_name = input("Enter the task name:\n")
            new_task_description = input("Enter the task description:\n")
            self.add_task(new_task_name, new_task_description)
        else:
            print("Thank you! Bye bye!")
            print('*' * 50)

    def finish_task(self, name):
        if name in self.todo:
            self.todo.pop(name)
            print(f"Task {name} is finished")
            print('*' * 50)

    def print_todo_list_details(self):
        if self.todo:
            print("Details of the ToDo List:")
            for task in self.todo:
                print(f"{task}: {self.todo[task]}")
            print('*' * 50)
        else:
            print("\nThere are no more tasks in the ToDoList")
            self.add_new_task()

    def print_todo_list(self):
        if self.todo:
            print("Your ToDo List:")
            for task in self.todo:
                print(task)
            print('*' * 50)
        else:
            print("\nThere are no more tasks in the ToDoList")
            self.add_new_task()

    def print_task_details(self, name):
        if name in self.todo:
            print(f"The task you asked for details:\n {name}: {self.todo[name]}")
            print('*' * 50)
        else:
            answer = input(f"The task \'{name}\' is not in the ToDo List, do you want to add it?(Y/N)\t")
            if answer.upper() == 'Y':
                task_description = input("Please enter the description of the task:\n")
                self.add_task(name, task_description)
            else:
                print("Thank you! Bye bye!")
                print('*' * 50)
