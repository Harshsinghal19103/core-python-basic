# for i in range(1, 5):
#
#     for j in range(1, i + 1):
#         print('*', end='\t')
#
#     print(" ")


# for i in range(1, 5):
#
#     for j in range(4, i, -1):
#         print(' ', end='\t')
#
#     for k in range(1, i + 1):
#         print('*', end='\t')
#
#     print(" ")


# for i in range(1, 5):
#
#     for j in range(4, i - 1, -1):
#         print('*', end='\t')
#
#     print(" ")


for i in range(5, 0, -1):

    for j in range(i, 5, -1):
        print(' ', end='\t')

    for k in range(0, i, 1):
        print('*', end='\t')

    print(" ")
