# a = 0
# b = 1
#
# for i in range(1, 6):
#     a, b = b, a + b
#
# print(a,b)


def fibonacci(a, b):
    for i in range(1, 7):
        a, b = b, a + b

    print(a,b)

fibonacci(1,1)



