class Shape:

    def execute(self):
        if self.validation():
            self.area()
        else:
            print("Validation failed")

    def validation(self):
        return False

    def area(self):
        print("shape method execute")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().area()
        super().area()

        self.length = length
        self.breadth = breadth

    def validation(self):
        if self.length > 0 and self.breadth > 0:
            return True
        else:
            return False

    def area(self):
        rectangle_area = self.length * self.breadth
        print("rectangle area:", rectangle_area)
        return rectangle_area


class Circle(Shape):
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def validation(self):
        if self.radius:
            return True
        else:
            return False

    def area(self):
        circle_area = self.PI * self.radius * self.radius
        print("circle area:", circle_area)
        return circle_area

class Triangle(Shape):
    pass

r = Rectangle(10 ,20)
r.execute()

c =Circle(8)
c.execute()

r = Rectangle(-6 ,20)
r.execute()
t = Triangle()
t.execute()
