import pickle
import objectSerialsation

d ={}
f = open('emp.dat','rb')
d = pickle.load(f)
print(d)

