import threading
from threading import *
import thresync
from thresync import *

class Racing(Thread):

   account : Account
   name = " "

   def __init__(self, account, name):
       super(Racing, self).__init__()
       self.account = account
       self.name = name

   def run(self):
       for i in range(5):
           self.account.deposit(100)
           print(self.name, self.account.get_balance())


acc = Account()

t1 = Racing(acc,"Ram")
t2 = Racing(acc, "Shaym")

t1.start()
t2.start()

