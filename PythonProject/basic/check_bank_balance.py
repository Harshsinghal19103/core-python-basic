def upi_app(n):
    amount = 10000
    if n == 1:
        print(" ")
        deposit_money = int(input("enter the amount to deposit:", ))
        print("money before deposited in account:", amount)
        print("money deposited:", deposit_money)
        amount = amount + deposit_money
        print("money in account after deposited:", amount)

    elif n == 2:
        print(" ")
        withdraw_money = int(input("enter the amount to withdraw:", ))
        print("money before withdraw in account:", amount)
        print("money withdraw:", withdraw_money)
        amount = amount - withdraw_money
        print("money in account after withdraw:", amount)

    elif n == 3:
        print(" ")
        print("bank balance:", amount)


print("what do you want to do")
print("1:deposit money")
print("2:withdraw money")
print("3:check bank balance")

upi_app(n=int(input("enter the number:", )))
print(" ")
print("system exited")
