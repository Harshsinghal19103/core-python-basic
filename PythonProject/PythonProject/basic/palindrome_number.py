num = 151
rem = 0
sum = 0
n = num

while n > 0:
    rem = n % 10
    sum = (sum * 10) + rem
    n = n // 10

if sum == num:
    print("it is palindrome number")
else:
    print("it is not palindrome number")