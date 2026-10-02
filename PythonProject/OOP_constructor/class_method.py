class Shape():

    def area(self):
        print("shape area method")

    @classmethod
    def test(cls):
        print("shape test class method")


class Rectangle(Shape):

    def area(self):
        pass


Shape.test()
s= Shape()
s.area()

