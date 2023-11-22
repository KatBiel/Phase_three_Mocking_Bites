from lib.music_library import *
from unittest.mock import Mock

def test_tracks_empty_initially():
    library = MusicLibrary()
    assert library.tracks == [] 

def test_add_and_list_out():
    library = MusicLibrary()
    track_1 = Mock()
    track_2 = Mock()
    track_3 = Mock()
    library.add(track_1)
    library.add(track_2)
    library.add(track_3)
    assert library.tracks == [track_1, track_2, track_3]

def test_searches_by_keyword():
    library = MusicLibrary()
    not_matching_mock = Mock()
    not_matching_mock.matches.return_value = False
    matching_mock = Mock()
    matching_mock.matches.return_value = True
    library.add(matching_mock)
    library.add(not_matching_mock)
    assert library.search('hello') == [matching_mock]
    
    
# def test_searches_by_keyword():
#     library = MusicLibrary()
#     track_1 = FakeNotMatchingTrack()
#     track_2 = FakeMatchingTrack()
#     library.add(track_1)
#     library.add(track_2)
#     assert library.search('hello') == [track_2]
    
# class FakeMatchingTrack():
#     def matches(self, keyword):
#         return True
    
# class FakeNotMatchingTrack():
#     def matches(self, keyword):
#         return False