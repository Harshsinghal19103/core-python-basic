from abc import ABC, abstractmethod


class Shape(ABC):

    def test(self):
        print("shape test method")

    @abstractmethod
    def area(self):
        pass                 #to force child to do override method


class Rectangle(Shape):

    def area(self):
        print("rectangle area method")


r = Rectangle()
r.area()
r.test()