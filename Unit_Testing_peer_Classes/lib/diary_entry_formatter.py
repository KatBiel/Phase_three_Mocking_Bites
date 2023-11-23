class DiaryEntryFormatter:
    def __init__(self, diary_entry):
        self.diary_entry = diary_entry

    def format(self):
        title = self.diary_entry.title
        contents = self.diary_entry.contents
        word_count = self.diary_entry.word_count()
        return f'{title} ({word_count} words): {contents}'