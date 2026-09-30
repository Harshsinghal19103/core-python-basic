class account:
    def __init__(self):
        self.__acc_name = None
        self.__acc_no = 0
        self.__money = 0
        self.__withdrawal = 0
        self.__deposit = 0
        self.__withdrawal_count = 0
        self.__deposit_count = 0

    def get_acc_name(self):
        return self.__acc_name

    def set_acc_name(self, acc_name):
        self.__acc_name = acc_name

    def get_acc_no(self):
        return self.__acc_no

    def set_acc_no(self, acc_no):
        self.__acc_no = acc_no

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

    def withdrawal(self, amt):
        if amt > self.__money:
            print("insufficent balance")
        elif amt > 20000:PythonProjectPythonProject
            print("you cannot withdraw money")
        else:
            self.__withdrawal_count > 5
            self.__withdrawal_count += 1
            self.__money = self.__money - amt
            print("your acc_balance is:", self.__money)
            print("your withdrawal remains:", 5 - self.__withdrawal_count)

    def deposit(self, amt):
        if amt > 100000:
            print("you cannot deposit more than 1 lakh")
        else:
            print("your acc balance before deposit:", self.__money)
            self.__deposit_count > 10
            self.__money += amt
            self.__deposit_count += 1
            print("your acc balance after deposit:", self.__money)
            print("your deposit remains:", 10 - self.__deposit_count)


a = account()
a.set_acc_name("harsh")
a.set_acc_no(462384623)
a.set_money(10000)

print("name:", a.get_acc_name())
print("account number:", a.get_acc_no())
print("money in account:", a.get_money())

a.withdrawal(5000)
a.deposit(4000)