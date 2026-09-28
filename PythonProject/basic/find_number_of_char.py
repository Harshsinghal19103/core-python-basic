name = "harsh singhal"
count = 0

for char in "abcdefghijklmnopqrstuvwxyz":

    for letters in name:
        if letters == char:
            print(letters, end=' ')

            count = count + 1
print(' ')
print(count)
