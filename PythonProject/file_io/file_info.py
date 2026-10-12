def Fileinfo():

    fo = open("../files/hello.txt","r")

    print("file name:",fo.name)
    print("mode of opening:", fo.mode)
    print("is file closed:", fo.closed)

    fo.close()
    print("is file closed:", fo.closed)


Fileinfo()


