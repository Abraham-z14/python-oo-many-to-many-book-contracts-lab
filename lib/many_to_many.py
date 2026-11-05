class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [
            contract
            for contract in Contract.all
            if contract.book == self
        ]

    def authors(self):
        return [
            contract.author
            for contract in self.contracts()
        ]


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [
            contract
            for contract in Contract.all
            if contract.author == self
        ]

    def books(self):
        return [
            contract.book
            for contract in self.contracts()
        ]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(
            contract.royalties
            for contract in self.contracts()
        )


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception("author must be an Author")

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if isinstance(value, Book):
            self._book = value
        else:
            raise Exception("book must be a Book")

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str):
            self._date = value
        else:
            raise Exception("date must be a string")

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if isinstance(value, int):
            self._royalties = value
        else:
            raise Exception("royalties must be an integer")

    @classmethod
    def contracts_by_date(cls, date):
        return [
            contract
            for contract in cls.all
            if contract.date == date
        ]