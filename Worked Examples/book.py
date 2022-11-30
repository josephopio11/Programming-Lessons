# Book                                                CD
# Title of book                                       Title of CD
# Author of book                                      Artist of CD
# Unique library reference number                     Unique library reference number
# Whether it is on loan                               Whether it is on loan
# Date the book is due for return                     Date the CD is due for return
# Whether the book is requested by another borrower    The type of music on the CD (genre)


class LibraryItem:
    def __init__(self, title, library_ref):
        self.loaned = False
        self.date_to_return = ''
        self.requested = False
        self.title = title
        self.library_ref = library_ref

    def is_on_loan(self):
        loaning = self.is_on_loan
        return loaning

    def borrowing(self):
        self.loaned = True
        return self.loaned

    def returning(self):
        self.loaned = False
        return self.loaned


class Book(LibraryItem):
    def __init__(self, title, library_ref, author):
        super(Book, self).__init__()
        self.author = author

    def requested_by_someone(self):
        self.requested = True
        return self.requested

    def not_requested(self):
        self.requested = False
        return self.requested


new_book = Book()


class CD(LibraryItem):
    pass
