class Person:

    def __init__(self):
        print("person constructor")

    def address(self):
        # self is instance method
        print("person address")


p = Person()
p.address()