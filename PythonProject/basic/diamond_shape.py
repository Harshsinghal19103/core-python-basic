m = 4

for i in range(1, 6):

    for j in range(m, 0, -1):
        print("\t", end='')

    for k in range(1, (i * 2)):
        print("*", end="\t")

    print(' ')

    m = m - 1

n = 1

for i in range(4, 0, -1):

    for j in range(n, 0, -1):
        print("\t", end='')

    for k in range(1, (i * 2)):
        print("*", end="\t")

    print('')

    n = n + 1
