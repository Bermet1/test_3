# Полиморфизм
class Book:
    def __init__(self, pages, author, year):
        self.pages = pages
        self.author = author
        self.year = year

    def info(self):
        print(f"Автор книги: {self.author}. Год написания: {self.year}")

    def color(self):
        print("Green")

class NewBook(Book):
    def __init__(self, pages, author, year):
        super().__init__(pages=pages, author=author, year=year)
    
    def info(self):
        print(f"Автор книги: {self.author}. Год написания: {self.year}")

    def color(self):
        print("Red")

