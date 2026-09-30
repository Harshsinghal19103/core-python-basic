number = [
    ["a1", "a2", "a3", "a4", "a5"],
    ["b1", "b2", "b3", "b4", "b5"],
    ["c1", "c2", "c3", "c4", "c5"]
]
seat = int(input("number of seat you want:", ))
selected_seat = []

print("select seat of your choice:")
print(number)
for i in range(1, seat + 1):
    n = input("select seat:", )
    selected_seat.insert(i, n)

print(selected_seat)
