# Instance Methods: work on specific object.
# Class Methods: work on entire class.
# Static Methods: they don't modify the state of entire class or specific instance of class.


class Book:
    # Property define at the class level are shared by all instance
    BOOK_TYPE = ("HARDCOVER", "PACKERBACK", "EBOOK")

    # double underscore properties are hidden from other classes.
    __booklist = None

    # Create class method
    @classmethod
    def getbooktype(cls):
        return cls.BOOK_TYPE

    # Create static methods
    @staticmethod
    def getbooklist():    # if booklist attribute is None then create new list
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist    # return if it is exits

    # instance method receive a specific object instance as an argument
    # and operate on data specific to object instance.

    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPE):
            raise ValueError(f"{booktype} is not valid book type")
        else:
            self.booktype = booktype


# Access class attribute
print("Book Type:", Book.getbooktype())


# Create Book instance
b1 = Book("Title1", "HARDCOVER")
b2 = Book("Title2", "PACKERBACK")

# use static method to access singleton object
thebook = Book.getbooklist()
thebook.append(b1)
thebook.append(b2)
print(thebook)
