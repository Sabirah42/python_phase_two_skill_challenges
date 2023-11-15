import pytest
from lib.text_reader import *

def test_text_reader_returns_2_for_400():
    result = text_reader('one '*400)
    assert result == "It would take you 2 minutes to read this text."

def test_text_reader_returns_4_for_700():
    result = text_reader('one '*700)
    assert result == "It would take you 4 minutes to read this text."