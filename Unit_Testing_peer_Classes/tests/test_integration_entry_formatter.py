from lib.diary_entry_formatter import DiaryEntryFormatter
from lib.diary_entry import DiaryEntry
from unittest.mock import Mock
import pytest


def test_formats_a_diary_entry():
    entry = DiaryEntry('Cool Title', 'Cool Contents')

    formatter = DiaryEntryFormatter(entry)
    assert formatter.format() == "Cool Title (2 words): Cool Contents"