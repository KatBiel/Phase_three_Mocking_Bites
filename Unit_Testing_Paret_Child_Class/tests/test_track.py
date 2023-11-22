from lib.track import *

# def test_creator():
#     track = Track('Photosyntesis', 'Carbon Based Lifeforms')
#     assert track.title == 'Photosyntesis' 
#     assert track.artist == 'Carbon Based Lifeforms'

def test_matches_title():
    track = Track('Photosyntesis', 'Carbon Based Lifeforms')
    assert track.matches('Photosyntesis') == True

def test_matches_for_partial_title():
    track = Track('Seeker ...and on', 'Carbon Based Lifeforms')
    assert track.matches('seeker') == True

def test_matches_artist():
    track = Track('Photosyntesis', 'Carbon Based Lifeforms')
    assert track.matches('Carbon Based Lifeforms') == True

def test_matches_for_partial_artist():
    track = Track('Seeker ...and on', 'Carbon Based Lifeforms')
    assert track.matches('Lifeforms') == True