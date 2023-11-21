from lib.music_library import *
from lib.track import *


"""
When we add a track
We get the track back in the track list
"""
def test_music_library_adds_track_and_lists_it():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    library.add(track_1)
    assert library.tracks == [track_1]

"""
When we add multiple tracks
We get the tracks back in the track list
"""
def test_music_library_adds_muliple_tracks_and_lists_them():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]

"""
When we add two tracks
And we search for a word in the title
We get the matching track back
"""
def test_music_library_returns_track_1_from_full_search():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("Always The Hard Way") == [track_1]

"""
When we add two tracks
And we search for a small part of a word in the title
We get the matching track back
"""
def test_music_library_returns_track_2_from_part_search():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("lace") == [track_2]

"""
When we add two tracks
And we search for a word not in any track title
We get an empty list back
"""
def test_music_library_returns_empty_list_from_search():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("zzz") == []

