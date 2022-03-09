# 1question
from numpy import *
x=array([])
y=int(input('First Number:'))
z=int(input('Last Number:'))
for c in range(y,z):
    x=append(x,c)
    for c in range(5):
        x=append(x,0)
x=append(x,z)
print(x)