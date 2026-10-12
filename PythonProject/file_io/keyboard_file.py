def Keyboardfile():
    file = open("../files/keyboard_file.txt", "w")
    text = input("Enter the message: ")

    while (text != "quit"):
        file.write(text)
        file.write("\n")
        text = input(" ")
    file.close()


Keyboardfile()
