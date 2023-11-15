import pytest
from lib.grammar_checker import *

def test_grammar_checker_returns_pass_message_for_question():
    result = grammar_checker("How are you?")
    assert result == "Grammar check passed - well done!"

def test_grammar_checker_returns_pass_message_for_exclamation():
    result = grammar_checker("Hello World!")
    assert result == "Grammar check passed - well done!"

def test_grammar_checker_returns_pass_message_for_period():
    result = grammar_checker("Hello World.")
    assert result == "Grammar check passed - well done!"

def test_grammar_checker_returns_fail_for_missing_punctuation():
    result = grammar_checker("How are you")
    assert result == "Grammar check FAILED - try again!"

def test_grammar_checker_returns_fail_for_incorrect_punctuation():
    result = grammar_checker("How are you@")
    assert result == "Grammar check FAILED - try again!"

def test_grammar_checker_returns_fail_for_incorrect_capitalisation():
    result = grammar_checker("how are you?")
    assert result == "Grammar check FAILED - try again!"

def test_grammar_checker_returns_fail_for_incorrect_grammar():
    result = grammar_checker("how are you")
    assert result == "Grammar check FAILED - try again!"

def test_grammar_checker_raises_error_for_empty_string():
    with pytest.raises(Exception) as e:
        grammar_checker("")
    error_message = str(e.value)
    assert error_message == "Text input must not be empty."

def test_grammar_checker_raises_error_if_not_string_type():
    with pytest.raises(Exception) as e:
        grammar_checker(['Hello', 'how', 'are', 'you', '?'])
    error_message = str(e.value)
    assert error_message == "Text must be a valid string"

def test_grammar_checker_raises_error_if_None():
    with pytest.raises(Exception) as e:
        grammar_checker(None)
    error_message = str(e.value)
    assert error_message == "Text must be a valid string"