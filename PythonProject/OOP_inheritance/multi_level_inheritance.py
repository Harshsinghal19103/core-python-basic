class School:
    def __init__(self, name):
        self.__name = name

    def getname(self):
            return self.__name


class classes(School):
    def __init__(self, name, room_number, lab):
        self.__room_number = room_number
        self.__lab = lab
        super().__init__(name)

    def getroom_number(self):
        return self.__room_number

    def getlab(self):
        return self.__lab


class classroom(classes):
    def __init__(self, name, room_number, lab, teacher, student):
        self.__teacher = teacher
        self.__student = student
        super().__init__(name, room_number, lab)

    def getteacher(self):
        return self.__teacher

    def getstudent(self):
        return self.__student


c = classroom("rays", 102, 2, "uday sir", "harsh")
print("name:",c.getname())
print("room number:",c.getroom_number())
print("lab:",c.getlab())
print("teacher:",c.getteacher())
print("student:",c.getstudent())
