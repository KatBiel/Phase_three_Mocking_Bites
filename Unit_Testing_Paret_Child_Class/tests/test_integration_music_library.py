from lib.music_library import *
from lib.track import *

def test_add_single_entry():
    library = MusicLibrary()
    track_1 = Track('Photosyntesis', 'Carbon Based Lifeforms')
    library.add(track_1)
    assert library.tracks == [track_1]

def test_add_multiple_entries():
    library = MusicLibrary()
    track_1 = Track('Photosyntesis', 'Carbon Based Lifeforms')
    track_2 = Track('Grains', 'Bonobo')
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]

def test_searches_for_track_by_full_title():
    library = MusicLibrary()
    track_1 = Track('Photosyntesis', 'Carbon Based Lifeforms')
    track_2 = Track('Grains', 'Bonobo')
    library.add(track_1)
    library.add(track_2)
    assert library.search('Grains') == [track_2]

