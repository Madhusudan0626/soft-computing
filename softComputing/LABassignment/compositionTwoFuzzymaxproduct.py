# Composition of two crisp relation using max product method

import numpy as np

def maxproduct(x,y):
    z=[]
    for a in x:
        for b in y.T:
            z.append(max(np.multiply(a,b)))
    z=np.array(z).reshape(x.shape[0],y.shape[1])
    print(z)
    pass
    pass

def takevalue():
    r,c=[int(i) for i in input("Enter the value of row and column of the relation\n").split(' ')]
    return r,c
    pass

row1,col1=takevalue()
print("Values : ")
r1=np.array([[float(input()) for i in range(col1)] for j in range(row1)])
print("Relation 1 : ")
print(r1)

row2,col2=takevalue()
print("Values : ")
r2=np.array([[float(input()) for i in range(col2)] for j in range(row2)])
print("Relation 2 : ")
print(r2)

if(col1==row2):
    print("Composition of two crisp relation using max product method : ")
    maxproduct(r1,r2)
else:
    print("Composition is not done check your matrices..")