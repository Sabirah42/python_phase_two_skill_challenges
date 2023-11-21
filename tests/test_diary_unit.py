import pytest
from lib.diary import *

def test_diary_initialises_with_empty_list():
    diary = Diary()
    assert diary.diary_entries == []

def test_diary_raises_exception_for_empty_list():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(2)
    assert str(e.value) == "No diary entries added"