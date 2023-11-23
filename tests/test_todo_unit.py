import pytest
from lib.todo import *

def test_todo_initialises_with_task():
    todo = Todo("Do laundry")
    assert todo.task == "Do laundry"

def test_todo_initialises_with_false_completion():
    todo = Todo("Do laundry")
    assert todo.complete == False

def test_todo_marks_task_as_complete():
    todo = Todo("Do laundry")
    todo.mark_complete()
    assert todo.complete == True

def test_todo_raises_error_for_empty_string():
    with pytest.raises(Exception) as e:
        Todo("")
    error_message = str(e.value)
    assert error_message == "Task cannot be empty"