# _discount attribute is consider interal to the class.
# property with double underscore is hidden by interpreter.
#__secret attribute indicate this is a sectret attribute .This attribute is not access by using 
# object of class . This can access using name of class as underscore name_of_class.

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is secret attribute"  # __secret

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount


# create object
b1 = Book("abc", "robert", 1225, 39.95)
b2 = Book("xyz", "pike", 234, 29.95)

#print class property
print(b1)
print(b1.title)

# getprice of book 1
print(b1.getprice())

# tryto set discount
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

#try to access hidden property
# print(b1.__secret)       #AttributeError: 'Book' object has no attribute '__secret'

print(b1._Book__secret)  # print secret of Book class