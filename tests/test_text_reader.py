import pytest
from lib.text_reader import *

def test_text_reader_returns_2_for_400():
    result = text_reader('one '*400)
    assert result == "It would take you 2 minutes to read this text."

def test_text_reader_returns_4_for_700():
    result = text_reader('one '*700)
    assert result == "It would take you 4 minutes to read this text."

def test_text_reader_returns_less_than_1_for_150():
    result = text_reader('one '*150)
    assert result == "It would take you less than 1 minute to read this text."

def test_text_reader_returns_0_for_empty():
    result = text_reader('')
    assert result == "It would take you 0 minutes to read this text."

def test_text_reader_throws_error_for_list():
    with pytest.raises(Exception) as e:
        text_reader(['house'])
    error_message = str(e.value)
    assert error_message == "Input value must be a string"