#pickle
import pickle
class Employee:
    def __init__(self, eno, ename):
        self.eno = eno
        self.ename = ename

    def __str__(self):
        return "%s, %s" %(self.eno, self.ename)

e = Employee (1, 'Ankit',)

f = open('emp.dat','wb')
pickle.dump(e,f)
f.close()

