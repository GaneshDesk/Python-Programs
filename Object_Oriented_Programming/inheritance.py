#Inheritance is considered as reusabilty.
# A child class is inherites the property of base class.

class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, price,  period, publisher):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.pages = pages
        self.author = author


class Magzin(Periodical):
    def __init__(self, title, publisher, period, price):
        super().__init__(title, price,period,publisher)
        
class Newspaper(Periodical):
    def __init__(self, title, publisher, period, price):
        super().__init__(title, price,period,publisher)

b1 = Book("New World", "pike", 311, 29.0)
n1 = Newspaper("NY Time", "New York Times", "Daily", 6.0)
m1 = Magzin("New Magzine", "Times of india", "Monthly", 59.0)

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
