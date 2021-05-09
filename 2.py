# Инкапсуляция
class Book:
    def __init__(self, page, author, year):
        self.page = page
        self._author = author
        self.__year = year

    __has_audio = True
    
    def HasAudio(self):
        self.__has_audio = True
    
    def NoAudio(self):
        self.__has_audio = False





       






