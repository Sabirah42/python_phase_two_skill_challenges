class GrammarStats:
    def __init__(self):
        pass

    def check(self, text):
        correct_punc = set('?!.')
        
        appropriate_punctuation = any((punc in correct_punc) for punc in text[-1])
        capitalisation = text[0].isupper()

        if appropriate_punctuation and capitalisation:
            return True
        else:
            return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass