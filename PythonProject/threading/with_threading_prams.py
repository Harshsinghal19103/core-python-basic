import threading


def hello(name):
    for i in range(1, 21):
        print('hello',name, i)


def hi(name):
    for i in range(1, 21):
        print('hi',name,i)

t1 = threading.Thread(target=hello,args=('abc',))
t2 = threading.Thread(target=hi,args=('xyz',))

t1.start()
t2.start()