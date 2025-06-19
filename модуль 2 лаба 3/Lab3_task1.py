class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages
    
    def __repr__(self):
        return f"{super().__repr__()[:-1]}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
    
    def __repr__(self):
        return f"{super().__repr__()[:-1]}, duration={self.duration})"


# блоки проверки того, что написал

a = PaperBook("asd", "koio", 1)
print(a.__str__())

