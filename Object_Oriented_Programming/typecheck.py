# In python every class is subclass of object class. i.e object class is parent class of all classes.


class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


# Create some instance of the classes.

b1 = Book("the cacher")
b2 = Book("the Graps")
n1 = Newspaper("Times Of India")
n2 = Newspaper("Economics Time")


# use type() to inspect object type
print(type(b1))
print(type(n1))

# compare two types together
print(type(b1) == type(b2))
print(type(b1) == type(n2))

# Use isinstance to compare a specific instance to known type
print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
print(isinstance(n2, Book))
print(isinstance(n2, object))
