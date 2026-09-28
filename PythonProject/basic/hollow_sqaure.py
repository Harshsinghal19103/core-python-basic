# for i in range(1, 6):
#     for j in range(1, 6):
#         print("*", end='\t')
#
#     print(" ")


for i in range(0, 4):

    for j in range(0, 4):

        if i == 1 and j == 1 or i == 1 and j == 2 or i == 1 and j == 1 or i == 2 and j == 2 or i == 2 and j == 1:
            print(" ", end='\t')
        else:
            print("*", end="\t")

    print(" ")
