list = [34, 24, 64, 80, 13, 43, 90]

highest = 0
second_highest = 0
smallest = list[0]

for i in list:
    if i > highest:
        second_highest = highest
        highest = i

    elif i > second_highest and i != highest:
        second_highest = i

for i in list:
    if i < smallest:
        smallest = i

print(highest)
print(second_highest)
print(smallest)
