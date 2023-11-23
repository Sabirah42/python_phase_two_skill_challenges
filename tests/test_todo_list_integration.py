from lib.todo_list import *
from lib.todo import *

def test_todo_list_adds_todos():
    todo_list = TodoList()
    todo_1 = Todo("Do laundry")
    todo_2 = Todo("Do shopping")
    todo_list.add(todo_1)
    todo_list.add(todo_2)

    assert todo_list.tasks == [todo_1, todo_2]

def test_todo_list_returns_incomplete_todos():
    todo_list = TodoList()
    todo_1 = Todo("Do laundry")
    todo_2 = Todo("Do shopping")
    todo_list.add(todo_1)
    todo_list.add(todo_2)

    assert todo_list.incomplete() == [todo_1, todo_2]

def test_todo_list_returns_completed_todos():
    todo_list = TodoList()
    todo_1 = Todo("Do laundry")
    todo_2 = Todo("Do shopping")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_2.mark_complete()

    assert todo_list.complete() == [todo_2]

def test_todo_list_returns_incomplete_todos_when_mixed():
    todo_list = TodoList()
    todo_1 = Todo("Do laundry")
    todo_2 = Todo("Do shopping")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_2.mark_complete()

    assert todo_list.incomplete() == [todo_1]

def test_todo_list_marks_all_complete():
    todo_list = TodoList()
    todo_1 = Todo("Do laundry")
    todo_2 = Todo("Do shopping")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.give_up()

    assert todo_list.incomplete() == []
