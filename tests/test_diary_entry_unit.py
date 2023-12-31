from lib.diary_entry import *

def test_diary_initialises_with_title_and_contents():
    diary = DiaryEntry("Day one", "Dear Diary...")

    actual_title = diary.title
    actual_contents = diary.contents

    expected_title = "Day one"
    expected_contents = "Dear Diary..."

    assert expected_title == actual_title
    assert expected_contents == actual_contents

def test_diary_returns_formatted_entry():
    diary = DiaryEntry("Day one", "Dear Diary...")

    expected_formatted_entry = "Day one: Dear Diary..."
    actual_formatted_entry = diary.format()

    assert expected_formatted_entry == actual_formatted_entry

def test_diary_returns_word_count():
    diary = DiaryEntry("Day one", "Dear Diary...")

    expected_word_count = 4
    actual_word_count = diary.count_words()

    assert expected_word_count == actual_word_count

def test_diary_returns_reading_time_one():
    diary = DiaryEntry("Day one", "Dear Diary...")

    expected_reading_time = 1
    actual_reading_time = diary.reading_time(4)

    assert expected_reading_time == actual_reading_time

def test_diary_returns_reading_time_two():
    diary = DiaryEntry("Day two", "Dear Diary, today was great!")

    expected_reading_time = 3
    actual_reading_time = diary.reading_time(2)

    assert expected_reading_time == actual_reading_time

def test_diary_returns_first_reading_chunk():
    diary = DiaryEntry("Day two", "Dear Diary, today was really great!")
    
    expected_chunk = "Day two: Dear Diary,"
    actual_chunk = diary.reading_chunk(2, 2)

    assert expected_chunk == actual_chunk

def test_diary_returns_second_reading_chunk():
    diary = DiaryEntry("Day two", "Dear Diary, today was really great!")
    
    assert diary.reading_chunk(2, 2) == "Day two: Dear Diary,"
    assert diary.reading_chunk(2, 2) == "today was really great!"

def test_diary_returns_to_start_of_diary():
    diary = DiaryEntry("Day two", "Dear Diary, today was really great!")
    
    assert diary.reading_chunk(2, 2) == "Day two: Dear Diary,"
    assert diary.reading_chunk(2, 2) == "today was really great!"
    assert diary.reading_chunk(2, 2) == "Day two: Dear Diary,"

def test_diary_returns_whole_reading_chunk_and_returns_to_start_of_diary():
    diary = DiaryEntry("Day two", "Dear Diary, today was really great!")
    
    assert diary.reading_chunk(2, 10) == "Day two: Dear Diary, today was really great!"
    assert diary.reading_chunk(2, 10) == "Day two: Dear Diary, today was really great!"

def test_diary_returns_entries_for_changed_wpm():
    diary = DiaryEntry("Day two", "Dear Diary, today was really great!")
    
    assert diary.reading_chunk(2, 2) == "Day two: Dear Diary,"
    assert diary.reading_chunk(2, 1) == "today was"
    assert diary.reading_chunk(2, 2) == "really great!"