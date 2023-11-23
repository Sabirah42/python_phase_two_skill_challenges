class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, todo):
        self.tasks.append(todo)
    
    def incomplete(self):
        incomplete_tasks = []

        for task in self.tasks:
            if task.complete == False:
                incomplete_tasks.append(task)
        return incomplete_tasks

    def complete(self):
        completed_tasks = []

        for task in self.tasks:
            if task.complete == True:
                completed_tasks.append(task)
        return completed_tasks

    def give_up(self):
        for task in self.tasks:
            task.complete = True

