"""
Abstract class contain abstract method .
Abstract method is a method which hava only decleration of method (without defination).
we connot create instance of Abstract class.
the class which inherites this abstract class that class should implement this abstract methods.
"""
from abc import ABC ,abstractmethod  # import abstractmethod 

class GraphicsShape:
    def __init__(self):
        super().__init__()
    @abstractmethod
    def calArea(self):
        pass


class Circle(GraphicsShape):
    def __init__(self, radius):
        self.radius = radius

    def calArea(self):
        return 3.14 *(self.radius **2)

class Square(GraphicsShape):
    def __init__(self, side):
        self.side = side

    def calArea(self):
        return self.side * self.side    

# we cannt create object of abstract class
#g= GraphicsShape()

c= Circle(10)
print(c.calArea())

s=Square(5)
print(s.calArea())