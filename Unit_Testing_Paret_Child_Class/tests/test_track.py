from lib.track import *

def test_creator():
    track = Track('Photosyntesis', 'Carbon Based Lifeforms')
    assert track.title == 'Photosyntesis' 
    assert track.artist == 'Carbon Based Lifeforms'

def test_matches():
    track = Track('Photosyntesis', 'Carbon Based Lifeforms')
    assert track.matches('Photosyntesis') == True