num = int(input("enter the number:",))
rem = 0
sum = 0
n = num

while n > 0:
    rem = n % 10
    sum = (sum * 10) + rem
    n = n // 10

print(sum)
