class Parents:

    def passion(self):
        print("follow parents footsteps")


class Eldest_child(Parents):
    pass


class Youngest_child(Parents):

    def passion(self):
        print("i will follow my dreams")


p = Eldest_child()
p.passion()

y = Youngest_child()
y.passion()

dream:Parents = Eldest_child()
dream.passion()