class TaskManager():
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def complete(self, task):
        self.tasks.remove(task)