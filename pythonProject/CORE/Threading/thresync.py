import threading
import time



class Account:

    balance = 0

    def __init__(self):
       self.lock = threading.Lock()

    def get_balance(self):

        return self.balance

    def set_balance(self, amount):

         self.balance = amount

    def deposit(self, amount):
       self.lock.acquire()
       bal = self.get_balance()
       self.set_balance(bal + amount)
       self.lock.release()