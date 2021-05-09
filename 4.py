# Абстракция 

from abc import ABC, abstractmethod

class Book(ABC):

    @abstractmethod
    def name(self):
        print("Горе от ума")

class NewBook(Book):
    def name(self):
        super().name()
        print("Чума")

book1 = NewBook()
book1.name()
