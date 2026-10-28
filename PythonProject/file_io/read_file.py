def read_file():

    file = open("../files/hello.txt","r")
    text = file.read()   # read all data
    print(text)
    file.close()   #close a file

read_file()