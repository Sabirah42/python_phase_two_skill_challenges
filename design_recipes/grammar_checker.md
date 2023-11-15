Grammar Checker Function Design Recipe

1. Describe the Problem
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

2. Design the Function Signature
def grammar_checker(text)
"""Checks that text starts with a capital letter AND ends with an appropriate punctuation mark.

Parameters:
    text: a string containing words (e.g. 'how are you")

Returns:
    Boolean dependng on whether text grammar is correct or incorrect

Side effects:
    Print statement if correct: "Grammar check passed - well done!"
    Print statement if incorrect: "Grammar check FAILED - try again!"

 3. Create Examples as Tests

"""
Given text that starts with a capital letter and ends with appropriate punctuation
It returns a pass message
"""
grammar_checker("How are you?") => "Grammar check passed - well done!"

"""

Given text that starts with a capital letter and ends with appropriate punctuation
It returns a pass message
"""
grammar_checker("Hello World!") => "Grammar check passed - well done!"

"""
Given text that starts with a capital letter and ends with appropriate punctuation
It returns a pass message
"""
grammar_checker("Hello World.") => "Grammar check passed - well done!"

"""

Given text that starts with a capital letter and does not end with any punctuation
It returns a failed message
"""
grammar_checker("How are you") => "Grammar check FAILED - try again!"

Given text that starts with a capital letter and does not end with appropriate punctuation
It returns a failed message
"""

grammar_checker("How are you@") => "Grammar check FAILED - try again!"
"""

Given text that does not start with a capital letter and does end with appropriate punctuation
It returns a failed message
"""

grammar_checker("how are you?") => "Grammar check FAILED - try again!"
"""

Given text that does not start with a capital letter and does not end with appropriate punctuation
It returns a failed message
"""

grammar_checker("how are you") => "Grammar check FAILED - try again!"
"""

Given an empty string for text
It raises an error message
"""
grammar_checker("") => "Text input must not be empty."
"""

Given any input that is not a string
It raises an error message
"""
grammar_checker(['Hello', 'how', 'are', 'you', '?']) => "Text must be a valid string"
"""

Given any input that is None value
It raises an error message
"""
grammar_checker(None) => "Text must be a valid string"
"""
