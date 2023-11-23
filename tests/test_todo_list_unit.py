from lib.todo_list import *

def test_initialises_with_empty_list():
    todo_list = TodoList()

    assert todo_list.tasks == []
