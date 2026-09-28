n = 20
odd = 0
even = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even = (even + i)
    else:
        odd = (odd + i)

even = even // (n // 2)
odd = odd // (n // 2)

print(even)
print(odd)
