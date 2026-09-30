num = int(input("enter the number:",))
count = 0

for i in range(2, num):
    if num % i == 0:
        count = count + 1
        break

if count == 1:
    print("not prime number")
else:
    print("prime number")
