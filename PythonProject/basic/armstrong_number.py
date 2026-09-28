# num = int(input("enter the number:", ))
# rem = 0
# sum = 0
# n = num
#
# while n > 0:
#     rem = n % 10
#     sum = sum + (rem * rem * rem)
#     n = n // 10
#
# if sum == num:
#     print("it is armstrong number")
# else:
#     print("it is not armstrong number")


num = 0

def armstrong_number(num):
    n = num
    sum = 0
    while n > 0:
        rem = n % 10
        sum = sum + (rem * rem * rem)
        n = n // 10

    if num == sum:
        print("number is armstrong number")
    else:
        print("number is not armstrong number")


armstrong_number(170)
