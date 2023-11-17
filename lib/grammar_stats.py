class GrammarStats:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, text):
        correct_punc = set('?!.')
        
        appropriate_punctuation = any((punc in correct_punc) for punc in text[-1])
        capitalisation = text[0].isupper()

        if appropriate_punctuation and capitalisation:
            self.passed += 1
            return True
        else:
            self.failed += 1
            return False

    def percentage_good(self):
        ## needs to log when True and log when False (will need to amend 'check')
        ## calculates percentage from these nums
        total = self.passed + self.failed
        return self.passed / total * 100
