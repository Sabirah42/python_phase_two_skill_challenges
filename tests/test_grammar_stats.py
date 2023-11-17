from lib.grammar_stats import *

def test_check_returns_pass_message_for_question():
    log = GrammarStats()
    log.check("How are you?")

    expected_result = True
    actual_result = log.check("How are you?")

    assert expected_result == actual_result

def test_check_returns_fail_for_missing_punctuation():
    log = GrammarStats()
    log.check("How are you")

    expected_result = False
    actual_result = log.check("How are you")

    assert expected_result == actual_result

def test_check_returns_fail_for_incorrect_punctuation():
    log = GrammarStats()
    log.check("How are you@")

    expected_result = False
    actual_result = log.check("How are you@")

    assert expected_result == actual_result

def test_check_returns_fail_for_incorrect_capitalisation():
    log = GrammarStats()
    log.check("how are you?")

    expected_result = False
    actual_result = log.check("how are you?")

    assert expected_result == actual_result

def test_check_returns_fail_for_incorrect_grammar():
    log = GrammarStats()
    log.check("how are you")

    expected_result = False
    actual_result = log.check("how are you")

    assert expected_result == actual_result

def test_check_adds_to_passed_for_correct_grammar():
    log = GrammarStats()
    log.check("How are you?")

    expected_result = 1
    actual_result = log.passed

    assert expected_result == actual_result

def test_check_adds_to_failed_for_incorrect_grammar():
    log = GrammarStats()
    log.check("how are you")

    expected_result = 1
    actual_result = log.failed

    assert expected_result == actual_result

def test_percentage_good_returns_100_for_passes():
    log = GrammarStats()
    log.check("How are you?")
    
    expected_result = 100
    actual_result = log.percentage_good()

    assert expected_result == actual_result

def test_percentage_good_returns_50_for_pass_and_fail():
    log = GrammarStats()
    log.check("How are you?")
    log.check("How are you")
    
    expected_result = 50
    actual_result = log.percentage_good()

    assert expected_result == actual_result