def grammar_checker(text):
    correct_punc = set('?!.')
    is_string = isinstance(text, str)

    if is_string == False:
        raise Exception("Text must be a valid string")
    elif text == "":
        raise Exception("Text input must not be empty.")


    else:
        appropriate_punctuation = any((punc in correct_punc) for punc in text[-1])
        capitalisation = text[0].isupper()

        if appropriate_punctuation and capitalisation:
            return "Grammar check passed - well done!"
        else:
            return "Grammar check FAILED - try again!"
