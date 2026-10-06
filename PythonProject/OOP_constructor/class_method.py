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

<<<<<<< HEAD
r = Rectangle()
r.test()
r.area()

=======
>>>>>>> 2535e577d67d43feaf59af1876ab2ad81b8368f6
