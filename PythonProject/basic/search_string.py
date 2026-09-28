name = "google"
n = "l"
count = 0

for i in name[::1]:
    if i == n:
        count = count + 1

print(count)
