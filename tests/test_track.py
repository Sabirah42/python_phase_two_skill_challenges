from lib.track import *

"""
When we create a new track
We can get the track's title and artist
"""
def test_track_initialises_and_gets_title_artist():
    track = Track("Always The Hard Way", "Terror")
    assert track.title == "Always The Hard Way"
    assert track.artist == "Terror"


"""
Given a track with a title and artist
Format returns a string TITLE by ARTIST
"""
def test_track_formats_tracks():
    track = Track("Always The Hard Way", "Terror")
    assert track.format() == "Always The Hard Way by Terror"
