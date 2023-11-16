class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        return f'{self.title}: {self.contents}'

    def count_words(self):
        ## take formatted entry
        ## count words len(.split)
        ## return
        return len(self.format().split())

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        
        ## take self.count_words/wpm
        ## change type to int?
        ## return
        return int(self.count_words()/wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        
        ## take wpm * minutes
        ## then return spliced diary entry
        chunk_length = wpm * minutes
        split_entry = (self.format().split())[0:chunk_length]
        reading_chunk = " ".join(split_entry)

        return reading_chunk
