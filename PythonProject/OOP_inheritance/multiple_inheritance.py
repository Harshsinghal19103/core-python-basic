class add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getaddition(self):
        return self.a + self.b


class sub:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getsubtraction(self):
        return self.a - self.b


class mul:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getmultiplication(self):
        return self.a * self.b


class result(add, sub, mul):
    def __init__(self, a, b):
        super().__init__(a, b)


r = result(90, 50)
print("add:", r.getaddition())
print("sub:", r.getsubtraction())
print("sub:", r.getmultiplication())
