class person:
    def __init__(self):
        self.__name = None
        self.__age = 0
        self.__dob = None
        self.__address = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        self.__dob = dob

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address


p = person()
p.set_name("harsh")
p.set_age(23)
p.set_dob("05-06-2003")
p.set_address("sage university campus")

print("name:", p.get_name())
print("age:", p.get_age())
print("dob:", p.get_dob())
print("address:", p.get_address())
