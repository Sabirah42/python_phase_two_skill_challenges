class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.stop_point = 0

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
        all_words = self.format().split()

        print(f'all words: {all_words}')
        print(f'stop point: {self.stop_point}')
        print(f'length of all words: {len(all_words)}')

        if self.stop_point >= len(all_words):
            self.stop_point = 0

        start_point = self.stop_point
        end_point = self.stop_point + chunk_length

        chunk_of_words = all_words[start_point:end_point]
        print(f'chunk of words: {chunk_of_words}')
        self.stop_point = end_point

        reading_chunk = " ".join(chunk_of_words)

        return reading_chunk
