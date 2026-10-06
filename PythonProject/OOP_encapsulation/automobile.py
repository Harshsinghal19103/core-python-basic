class Automobile:
    GEARS = 6

    def __init__(self):
        self.__name = None
        self.__color = None
        self.__seat = 0
        self.__speed = 0
        self.__accelerate = 0
        self.__break = 0

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_seat(self):
        return self.__seat

    def set_seat(self, seat):
        self.__seat = seat

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def get_accelerate(self):
        if self.__speed >= 350:
            print("speed limit is crossed, slow down")
        elif self.__speed <= 100:
            print("too slow, speed up")
        else:
            print("speed is ok keep going")

    def get_breaks(self):
        if self.__speed == 0:
            print("vehicle is not moving")
        else:
            print("your vehicle is moving at speed:", self.__speed)

    def gear(self, no):
        if no >= Automobile.GEARS:
            print("vehicle at neutral")
        elif no == 6:
            self.__speed == 120
            print("your speed should be higher than 120 at gear 6", self.__speed)
        elif no == 5:
            self.__speed == 90
            print("your speed should be higher than 90 at gear 5")
        elif no == 4:
            self.__speed >= 60
            print("your speed should be higher than 60 at gear 4")
        elif no == 3:
            self.__speed >= 45
            print("your speed should be higher than 45 at gear 3")

        elif no == 2:
            self.__speed >= 20
            print("your speed should be higher than 20 at gear 2")

        elif no == 1:
            self.__speed >= 5
            print("your speed should be higher than 5 at gear 1")


c = Automobile()
c.set_name("wagon R")
c.set_color("blue")
c.set_seat(7)
c.set_speed(80)

print("name:", c.get_name())
print("color:", c.get_color())
print("seat:", c.get_seat())
print("speed:", c.get_speed())

c.get_accelerate()
c.get_breaks()

c.gear(1)
