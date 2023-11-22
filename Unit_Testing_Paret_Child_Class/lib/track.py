class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


    def matches(self, keyword):
        return keyword.lower() in self.title.lower() or keyword.lower() in self.artist.lower()

    
    # def matches(self, keyword):
    #     if keyword.lower() in self.title.lower():
    #         return True
    #     else:
    #         if keyword.lower() in self.artist.lower():
    #             return True
