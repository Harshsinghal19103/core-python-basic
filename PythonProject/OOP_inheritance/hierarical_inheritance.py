class Shape:
    def __init__(self, color, border):
        self.color = color
        self.border = border

<<<<<<< HEAD
    def color(self):
=======
<<<<<<< HEAD
    def color(self):
=======
<<<<<<< HEAD
    def color(self):
=======
    def get_color(self):
>>>>>>> 1295fc64fe3d7fab5f3e522978d319dcdf50b206
>>>>>>> 5e05695f7ba3765ab6736ae671bf3142800198d0
>>>>>>> 92efe15a2df1c79dd2d0580f69f9c03ab3c1a932
        return self.color

    def get_border(self):
        return self.border


class Rectangle(Shape):
    def __init__(self, length, width, color, border):
        self.length = length
        self.width = width
        super().__init__(color, border)

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width


class circle(Shape):
    def __init__(self, radius, color, border):
        self.radius = radius
        super().__init__(color, border)

    def get_radius(self):
        return self.radius


r = Rectangle(40, 30, "red", 20)
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 5e05695f7ba3765ab6736ae671bf3142800198d0
>>>>>>> 92efe15a2df1c79dd2d0580f69f9c03ab3c1a932
c = circle(3.5,"blue",15)

print("circle")
print(c.radius)
print(c.color)
print(c.border)
print("rectangle")
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
s = circle(3.5,"blue",15)

print(s.radius)
print(s.color)
print(s.border)
>>>>>>> 1295fc64fe3d7fab5f3e522978d319dcdf50b206
>>>>>>> 5e05695f7ba3765ab6736ae671bf3142800198d0
>>>>>>> 92efe15a2df1c79dd2d0580f69f9c03ab3c1a932
print(r.width)
print(r.length)
print(r.color)
print(r.border)
