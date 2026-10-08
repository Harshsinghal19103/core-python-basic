print("before")

a = 10
b = 2

print("mid")

try:
    c = a / b
    print("result:",c)

except ZeroDivisionError as e:
    print("error:",e)

print("after")
