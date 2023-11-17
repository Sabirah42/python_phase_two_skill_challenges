Task Manager Class Design Recipe

1. Describe the Problem
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

2. Design the Class Interface

class TaskManager():
    def __init__(self):
        # Parameters: none
        # Side effects: Initialises with a list

    def add(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns: Nothing
        # Side-effects: Saves the task to the self []

    def complete(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns: Nothing
        # Side-effects:
        #   Deletes given task

3. Create Examples as Tests

"""
Initialises with an empty list
"""
manager = TaskManager()
manager.tasks => []

"""
Given a task
Adds the task to tasks []
"""
manager = TaskManager()
manager.add('Do laundry')
manager.tasks => ['Do laundry']

"""
Given multiple tasks
Adds the tasks to tasks []
"""
manager = TaskManager()
manager.add('Do laundry')
manager.add('Take out trash')
manager.tasks => ['Do laundry', 'Take out trash']
"""

Given a task
Deletes this task from tasks []
"""
manager = TaskManager()
manager.add('Do laundry')
manager.add('Take out trash')
manager.complete('Take out trash')
manager.tasks => ['Do laundry']
"""
