'''TO INPUT A TUPLE FROM THE USER AND DISPLYS
ITS MINIMUM VALUE'''
L=[]
N=int(input("Enter no. of values:"))
for i in range (0,N):
    value=int(input("Enter value:"))
    L.append(value)
T= tuple(L)
MIN = T[0]
for i in range(1,N):
    if T[i]<MIN:
        MIN=T[i]
print("Minimum value is:",MIN)