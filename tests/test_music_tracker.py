import pytest
from lib.music_tracker import *

def test_music_tracker_initialises_with_list():
    tracker = MusicTracker()
    
    assert tracker.tracks == []

def test_music_tracker_adds_track():
    tracker = MusicTracker()
    tracker.add('Chop Suey')

    assert tracker.tracks == ['Chop Suey']

def test_music_tracker_adds_tracks_returns_history():
    tracker = MusicTracker()
    tracker.add('Chop Suey')
    tracker.add('Numb')

    assert tracker.history() == ['Chop Suey', 'Numb']

def test_music_tracker_raises_exception_for_empty_string():
    tracker = MusicTracker()

    with pytest.raises(Exception) as e:
        tracker.add('')
    error_message = str(e.value)
    
    assert error_message == "Track must be at least one character long"


