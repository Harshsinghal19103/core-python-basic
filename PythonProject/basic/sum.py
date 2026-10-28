# a=2
# b=3
# print(a+b)

number = [2, 4, 3, 8, 6]

for i in range(len(number)):

    for j in range(0, len(number) - 1):

        if number[i] > number[j]:
            temp = number[i]
            number[i] = number[j]
            number[j]= temp

print(number)

