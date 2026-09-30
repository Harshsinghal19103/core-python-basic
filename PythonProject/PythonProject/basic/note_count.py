amount = 3098
note = [500, 200, 100, 50, 20, 10, 5, 2, 1]
count = 0

for i in note:
    count = amount // i
    print(i, '=', count)
    if count > 0:
        amount = amount % i

