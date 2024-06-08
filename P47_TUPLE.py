'''TO INPUT A TUPLE FROM THE USER AND DISPLYS
ITS MAXIMUM VALUE'''
L=[]
N=int(input("Enter no. of values:"))
for i in range (0,N):
    value=int(input("Enter value:"))
    L.append(value)
T= tuple(L)
MAX = T[0]
for i in range(1,N):
    if T[i]>MAX:
        MAX=T[i]
print("Maximum value is:",MAX)