from lib.music_library import *

"""
When music library initialises
There is an empty list
"""
def test_music_library_initialises_with_empty_list():
    library = MusicLibrary()
    assert library.tracks == []