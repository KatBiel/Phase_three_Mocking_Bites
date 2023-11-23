from lib.diary_entry import DiaryEntry
from unittest.mock import Mock

def test_constructor():
    entry = DiaryEntry('Cool Title', 'Cool Contents')
    assert entry.title == 'Cool Title'
    assert entry.contents == 'Cool Contents'

def test_word_count():
    entry = DiaryEntry('Cool Title', 'Cool Contents')
    assert entry.word_count() == 2