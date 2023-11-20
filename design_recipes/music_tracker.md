Music Tracker Class Design Recipe

1. Describe the Problem
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

2. Design the Class Interface
class MusicTracker():
    def __init__():
        # Parameters: None
        # Side effects: initialises with a list

    def add():
        # Parameters: 'track' - string representing a single track
        # Returns: Nothing
        # Side effects: Adds track to initialised list

    def history():
        # Parameters: None
        # Returns: List of strings/tracks
        # Side effects: None

3. Create Examples as Tests
"""
Initialises with a list
"""
tracker = MusicTracker()
tracker.tracks => []

"""
Given a track
Adds track to tracks
"""
tracker = MusicTracker()
tracker.add('Chop Suey')
tracker.tracks => ['Chop Suey']
"""

Given two tracks
Adds both tracks to tracks
"""
tracker = MusicTracker()
tracker.add('Chop Suey')
tracker.add('Numb')
tracker.history => ['Chop Suey', 'Numb']

"""
Given an empty string
Raises exception
"""
tracker = MusicTracker()
tracker.add('') => raises error message "Track must be at least one character long"