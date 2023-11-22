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
        if self.diary_entries == []:
            raise Exception("No diary entries added")
            
        max_words = wpm * minutes

        most_readable = None
        longest_entry_count = 0

        for entry in self.diary_entries:
            if entry.count_words() <= max_words and entry.count_words() > longest_entry_count:
                most_readable = entry
                longest_entry_count = entry.count_words()

        return most_readable