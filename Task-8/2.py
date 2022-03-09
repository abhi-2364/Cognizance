# 2question TP CHECK IF ARRAYS ARE EQUAL
import numpy as np
A = np.array([1 ,0, 0, 0 ,1, 0])
B = np.array([0 ,0, 1, 1 ,0 ,1])
array_len=len(A)
for p in range(array_len):
    if A[p] == B[p] :       
        result=0
    else :
        result=1
if result==0:
    
    print(" A AND B ARRAYS ARE EQUAL ")
else :
    
    print(" A AND B ARRAYS ARE NOT EQUAL ")