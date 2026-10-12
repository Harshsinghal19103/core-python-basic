class Parents:

    def hobby(self):
        print("find some hobby")

    def passion(self):
        print("follow parents footsteps")
        self.hobby()

    def passion(self):
        print("follow parents footsteps")


class Eldest_child(Parents):
    pass


class Youngest_child(Parents):

    def passion(self):
        print("i will follow my dreams")


class Middle_child(Parents):
    # pass

    def __init__(self):
        print("i will not ")

    def passion(self):
        print("i will follow my hobby")


class Youngest_child(Parents):

    def passion(self):
        print("i will follow my mother dreams")


p = Eldest_child()
p.passion()

y = Youngest_child()
y.passion()

dream: Parents = Eldest_child()

dream.passion()

dream.passion()

dream.passion()

dream.passion()

m = Middle_child()
m.passion()

y = Youngest_child()
y.passion()
