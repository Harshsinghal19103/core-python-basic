try:
    number = int(input("enter the number:"))

    if number >= 10:
        print("valid user")
    else:
        raise Exception("invalid user")
except Exception as e:
    print("exception:", e)


