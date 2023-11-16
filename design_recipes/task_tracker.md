Task Tracker Function Design Recipe

1. Describe the Problem
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

2. Design the Function Signature

def task_tracker(text):
"""checks whether text contains string '#TODO'

Parameters:
    text: string

Returns: 
    if True returns "This is a task"
    if False returns "This is not a task"

Side-effects:
    Prints whether or not text includes a task
"""

3. Create Examples as Tests
"""
Given a string that contains a task
It returns confirmation of task
"""
task_tracker("#TODO laundry") => "This is a task"

task_tracker("laundry #TODO") => "This is a task"

task_tracker("take out #TODO trash") => "This is a task"
"""

Given a string that does not contain a task
It returns confirmation of no task
"""

task_tracker("But why is this in your list?") => "This is not a task"

task_tracker("#TODAYWASGREAT") => "This is not a task"
"""

Given an empty string
It raises an error
"""
task_tracker("") => "Input value must not be empty"
"""

Given a None value
It raises an error
"""
task_tracker(None) => "Input value must not be empty"
"""

Given a value that is not a string
It raises an error
"""
task_tracker([1, 2, 3, 4]) => "Input value must be a string"
"""

