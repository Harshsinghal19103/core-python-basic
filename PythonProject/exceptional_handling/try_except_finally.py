print("before")

a = 10
b = 0

print("mid")

try:
    c = a / b
    print("result:",c)

except ZeroDivisionError as e:
    print("error:",e)

else:
    print("it is correct")

finally:
    print("it should work any way")

print("after")