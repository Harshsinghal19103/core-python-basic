def Writefile():

    file = open("../files/hii.txt","w")   #if file is not there it create hii.txt file on it own

    file.write("hi brock\n")
    file.write("welcome to gaming world")
    file.close()

Writefile()