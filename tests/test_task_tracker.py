import pytest
from lib.task_tracker import *

def test_task_tracker_returns_confirmation_of_task_start():
    result = task_tracker("#TODO laundry")
    assert result == "This is a task"

def test_task_tracker_returns_confirmation_of_task_end():
    result = task_tracker("laundry #TODO")
    assert result == "This is a task"

def test_task_tracker_returns_confirmation_of_task_middle():
    result = task_tracker("take out #TODO trash")
    assert result == "This is a task"

def test_task_tracker_returns_confirmation_of_no_task():
    result = task_tracker("But why is this in your list?")
    assert result == "This is not a task"

def test_task_tracker_returns_confirmation_of_no_task_partial_match():
    result = task_tracker("#TODAYWASGREAT")
    assert result == "This is not a task"

def test_task_tracker_raises_error_for_empty_string():
    with pytest.raises(Exception) as e:
        task_tracker("")
    error_message = str(e.value)
    assert error_message == "Input value must not be empty"

