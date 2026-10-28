def seek_and_tell():
    file = open("../files/seek_and_tell.txt", "r")
    print(file.tell())   # tell the position of cursor
    print(file.seek(4))  #to move the cursor how many character(4)
    str = file.read(4)   #read the charcters where the cursor is
    print(str)
    print(file.tell())
    file.close()       #close the file
seek_and_tell()