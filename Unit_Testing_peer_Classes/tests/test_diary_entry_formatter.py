from lib.diary_entry_formatter import DiaryEntryFormatter
from unittest.mock import Mock

def test_formats_a_diary_entry():
    fake_diary_entry = Mock()
    
    # To set properties on the mock, we can just set them
    fake_diary_entry.title = "Hello"
    fake_diary_entry.contents = "Hello, world!"

    # And we've seen how to tell the mock to return a value for a method
    fake_diary_entry.word_count.return_value = 2

    formatter = DiaryEntryFormatter(fake_diary_entry)
    assert formatter.format() == "Hello (2 words): Hello, world!"