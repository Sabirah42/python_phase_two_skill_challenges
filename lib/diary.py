import math

class Diary:
    def __init__(self):
        self.diary_entries = []

    def add(self, entry):
        self.diary_entries.append(entry)

    def all(self):
        return self.diary_entries

    def count_words(self):
        total = 0
        
        for entry in self.diary_entries:
            total += entry.count_words()

        return total

    def reading_time(self, wpm): 
        if self.diary_entries == []:
            raise Exception("No diary entries added")      
        return math.ceil(self.count_words()/wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.

        max_words = wpm * minutes

        readable_entries = []

        for entry in self.diary_entries:
            if entry.count_words() <= max_words:
                readable_entries.append(entry)
        return readable_entries[0]
