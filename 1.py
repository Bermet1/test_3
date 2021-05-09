# Наследование
class Book:

    def __init__(self, pages, author, year, country):
        self.pages = pages
        self.auther = author
        self.year = year
        self.country = country


class BookWutheringHeights(Book):
    audio = False

    def __init__(self, pages, author, year, country, language):
        self.language = language
        super().__init__(pages=pages, author=author, year=year, country=country)

    def has_audio(self):
        self.audio = True

    def no_audio(self):
        self.audio = False

books = BookWutheringHeights(pages = 325, author='Emily Bronte', year=1852, country="England", language="English")
print(books.pages)
print(books.audio)
books.has_audio()

# Public

