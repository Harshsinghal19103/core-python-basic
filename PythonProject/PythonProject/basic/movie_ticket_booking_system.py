def ticket_booking_system(seat):
    price = 1
    print("book ticket seat for movie")

    while seat == True:
        seat = int(input("how many seat you want:", ))
        print("no of seat you selected:", seat)
        print(" ")
        print("conform no of seat you selected")
        print("1.yes")
        print("2.no")
        n = int(input("choose:", ))

        if n == 1:
            print("no of seat conformed:", seat)
        elif n == 2:
            seat = int(input("enter again no of seat:", ))

        if seat >= 5:
            price = seat * 160
            print("price of the movie ticket:", price)
        elif seat >= 3:
            price = seat * 180
            print("price of the movie ticket:", price)
        elif seat >= 1:
            price = seat * 200
            print("price of the movie ticket:", price)

        print(" ")
        print("do you want popcorn")
        print("1.yes")
        print("2.no")
        n = int(input("choose:", ))

        if n == 1:
            print(" ")
            print("choose your combo")
            print("1.large popcorn size: 400")
            print("2.medium popcorn size: 250")
            print("3.large popcorn size: 150")
            n = int(input("enter the combo number: "))

            if n == 1:
                amount = price + 400
                print(" ")
                print("your total amount is:", amount)

            elif n == 2:
                amount = price + 250
                print(" ")
                print("your total amount is:", amount)

            elif n == 3:
                amount = price + 150
                print(" ")
                print("your total amount is:", amount)

        elif n == 2:
            amount = price
            print(" ")
            print("your total amount is:", amount)


ticket_booking_system(1)
