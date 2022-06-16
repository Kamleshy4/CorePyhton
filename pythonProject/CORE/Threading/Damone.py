import threading
from threading import *

def hello(ram):
    for i in range(15):
        print('hello',i)
def hi (ram):
    for i in range(15):
      print('hiii', i)


t1 = threading.Thread(target = hello, args=('ram',))
t2 = threading.Thread(target = hi, args=('shaym',))

t1.start()
t2.start()