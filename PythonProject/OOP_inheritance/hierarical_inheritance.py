class Shape:
    def __init__(self, color, border):
        self.color = color
        self.border = border

    def get_color(self):
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

c = circle(3.5, "blue", 15)

print("circle")
print(c.radius)
print(c.color)
print(c.border)
print("rectangle")

s = circle(3.5, "blue", 15)

print(s.radius)
print(s.color)
print(s.border)

print(r.width)
print(r.length)
print(r.color)
print(r.border)
