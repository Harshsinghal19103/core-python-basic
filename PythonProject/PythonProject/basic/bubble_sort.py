number = [21, 2, 31, 54, 7, 10]

for i in range(0, len(number)):

    for j in range(i + 1, len(number)):

        if number[i] > number[j]:
            temp = number[i]
            number[i] = number[j]
            number[j] = temp


print(number)
