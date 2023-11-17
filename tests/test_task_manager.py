from lib.task_manager import *

def test_taskmanager_initialises_with_empty_list():
    manager = TaskManager()

    assert manager.tasks == []

def test_taskmanager_adds_task():
    manager = TaskManager()

    manager.add('Do laundry')
    assert manager.tasks == ['Do laundry']

def test_taskmanager_adds_multiple_tasks():
    manager = TaskManager()

    manager.add('Do laundry')
    manager.add('Take out trash')
    assert manager.tasks == ['Do laundry', 'Take out trash']

def test_taskmanager_deletes_task():
    manager = TaskManager()

    manager.add('Do laundry')
    manager.add('Take out trash')
    manager.complete('Take out trash')

    assert manager.tasks == ['Do laundry']