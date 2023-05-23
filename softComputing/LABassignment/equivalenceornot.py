import numpy as np
flag1=False
flag2=False
flag3=False
def takevalue():
    r,c=[int(i) for i in input("Enter the value of row and column of the relation\n").split(' ')]
    return r,c
    pass

row , col=takevalue()

if(row != col):
    print("relation must be a square matrix.");
else:
    print("Values:")
    r=np.array([[float(input()) for i in range(col)] for j in range(row)])
    
    def minimum(a,b):
        if(a>b):return b
        else:return a
        pass
    def checkreflexive():
        for i in range(row):
            for j in range(col):
                if(r[i][i]!=1.0):
                    print("Relation is not reflexive")
                    return False 
        return True
        pass
    def checksymmetric():
        for i in range(row):
            for j in range(col):
                if(r[i][j]!=r[j][i]):
                    print("Relation is not symmetric")
                    return False
        return True
    def checktransitive():
        for i in range(row):
            for j in range(col):
                for k in range(row):
                    if((r[i][k]>=minimum(r[i][j],r[j][k]))):
                        return True
        print("Relation is not transitive")
        return False
    if(checkreflexive() and checksymmetric() and checktransitive()):
        
        print("Fuzzy relation is equivalence..")
        
    else:
        print("Fuzzy relation is not equivalence...")