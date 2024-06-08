'''TO INPUT A LIST FROM THE USER AND DISPLYS
ITS MINIMUM VALUE'''
L=[]
N=int(input("Enter no. of values:"))
for i in range (0,N):
    value=int(input("Enter value:"))
    L.append(value)
MIN = L[0]
for i in range(1,N):
    if L[i]<MIN:
        MIN=L[i]
print("Minimum value is:",MIN)
