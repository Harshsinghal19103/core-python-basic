class Shape:

    def execute(self):
        print("shape method execute")
        self.area()

    def area(self):
        print("shape area execute")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        rectangle_area = self.length * self.breadth
        print("rectangle area:", rectangle_area)
        return rectangle_area


class Circle(Shape):
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = self.PI * self.radius * self.radius
        print("circle area:", circle_area)
        return circle_area


class Triangle(Shape):
    pass


r = Rectangle(10, 20)
r.execute()

c = Circle(8)
c.execute()

t = Triangle()
t.execute()
