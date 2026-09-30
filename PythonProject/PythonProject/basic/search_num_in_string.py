name = "harsh0560"
count = 0

for i in name[::-1]:
    if i % 1 == 0:
        count = count + 1

if count >= 1:
    print("string has number")
else:
    print("string does not have any number")
