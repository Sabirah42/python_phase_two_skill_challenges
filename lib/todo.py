class Todo:
    def __init__(self, task):
        self.task = task
        self.complete = False

        if self.task == '':
            raise Exception("Task cannot be empty")

    def mark_complete(self):
        self.complete = True