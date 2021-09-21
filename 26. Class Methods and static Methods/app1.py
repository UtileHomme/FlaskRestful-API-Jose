class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight} gm>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight + 100)


# book = Book("harry potter", "hardcover", 1500)

book = Book.hardcover("Harry Potter", 1500)
light = Book.hardcover("Python 101", 500)
print(Book.TYPES)
print(book.name)
print(book)
print(light)
