import pytest
from lib.diary import *
from lib.diary_entry import *

"""
When we add a diary entry
We get the entry back in the diary entries list
"""

def test_diary_adds_entry_and_lists_it():
    diary = Diary()
    entry_1 = DiaryEntry("Day One", "Day one was great!")
    diary.add(entry_1)
    assert diary.all() == [entry_1]

"""
When we add multiple diary entries
We get all entries back in the diary entries list
"""

def test_diary_adds_multiple_entries_and_lists_them():
    diary = Diary()
    entry_1 = DiaryEntry("Day One", "Day one was great!")
    entry_2 = DiaryEntry("Day Two", "Day two was also great!")
    diary.add(entry_1)
    diary.add(entry_2)

    assert diary.all() == [entry_1, entry_2]

"""
When we add multiple diary entries
We can get the sum of all words in diary entries list
"""

def test_diary_counts_total_words_in_entry():
    diary = Diary()
    entry_1 = DiaryEntry("Day One", "Day one was great!")
    entry_2 = DiaryEntry("Day Two", "Day two was also great!")
    diary.add(entry_1)
    diary.add(entry_2)

    assert diary.count_words() == 13

"""
When we add two diary entries with a total word count of 13
And we call reading_time with a wpm of 2
We get the integer 7
"""

def test_diary_returns_7_reading_time_for_14():
    diary = Diary()
    entry_1 = DiaryEntry("Day One", "Day one was pretty great!")
    entry_2 = DiaryEntry("Day Two", "Day two was also great!")
    diary.add(entry_1)
    diary.add(entry_2)

    assert diary.reading_time(2) == 7

def test_diary_returns_7_reading_time_for_13():
    diary = Diary()
    entry_1 = DiaryEntry("Day One", "Day one was great!")
    entry_2 = DiaryEntry("Day Two", "Day two was also great!")
    diary.add(entry_1)
    diary.add(entry_2)

    assert diary.reading_time(2) == 7

"""
When we add two diary entries, one short and one long
And we call find_best_entry_for_reading_time with 5 wpm and 2 minutes
We get back the shorter diary entry
"""

def test_diary_returns_shorter_entry_for_5():
    diary = Diary()
    entry_1 = DiaryEntry("Day One", "One " * 50)
    entry_2 = DiaryEntry("Day Two", "Two " * 5)
    diary.add(entry_1)
    diary.add(entry_2)

    assert diary.find_best_entry_for_reading_time(5, 2) == entry_2

"""
When we add two diary entries, one short and one long
And we call find_best_entry_for_reading_time with 100 wpm and 2 minutes
We get back the longer diary entry
"""

def test_diary_returns_longer_entry_for_100():
    diary = Diary()
    entry_1 = DiaryEntry("Day One", "One " * 50)
    entry_2 = DiaryEntry("Day Two", "Two " * 5)
    diary.add(entry_1)
    diary.add(entry_2)

    assert diary.find_best_entry_for_reading_time(100, 2) == entry_1

"""
When we add two diary entries, neither of which is readable in the given time
And we call find_best_entry_for_reading_time with 1 wpm and 2 minutes
We get back an empty list
"""
def test_diary_returns_empty_list():
    diary = Diary()
    entry_1 = DiaryEntry("Day One", "One " * 50)
    entry_2 = DiaryEntry("Day Two", "Two " * 10)
    diary.add(entry_1)
    diary.add(entry_2)

    assert diary.find_best_entry_for_reading_time(1, 2) == None

"""
When we add three diary entries, all readable within the given time
And we call find_best_entry_for_reading_time
We get back the longest possible diary entry
"""    

def test_diary_returns_longest_possible_entry_for_200():
    diary = Diary()
    entry_1 = DiaryEntry("Day One", "One " * 50)
    entry_2 = DiaryEntry("Day Two", "Two " * 5)
    entry_3 = DiaryEntry("Day Three", "Three " * 100)
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)

    print(f'entry 1: {entry_1}')
    print(f'entry 2: {entry_2}')
    print(f'entry 3: {entry_3}')


    assert diary.find_best_entry_for_reading_time(200, 2) == entry_3

"""
When no diary entries have been added
And we call find_best_entry_for_reading_time
We get an error meessage
"""    

def test_diary_returns_longest_possible_entry_for_200():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(200, 2)
    error_message = str(e.value)
    assert error_message == "No diary entries added"
