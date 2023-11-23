from lib.diary import *
from unittest.mock import Mock

def test_creator():
    diary = Diary('Cool Contents')
    assert diary.read() == 'Cool Contents'