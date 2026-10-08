class Insufficientfund(Exception):

    def __init__(self,msge):
        super().__init__(msge)


class Account:

    def __init__(self):
        self.balance = 0

    def set_balance(self,balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self,amount):
        print("balance money", self.balance, "money deposited in account", amount)
        self.balance += amount
        print("money after deposited",self.balance)


    def withdrawal(self,amount):
        if self.balance - amount >= 2000:
            self.balance -= amount
            print("balance money",self.balance,"withdrawal money",amount)

        else:
            raise Insufficientfund("money should be more than 2000 in account")



acc = Account()
acc.set_balance(5000)

try:
    acc.deposit(2000)
    acc.withdrawal(4000)
    acc.withdrawal(2000)

except Insufficientfund as e:
    print("exception",e)


acc.deposit(4000)
