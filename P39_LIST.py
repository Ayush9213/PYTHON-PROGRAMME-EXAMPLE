'''TO INPUT A LIST FROM THE USER AND DISPLYS
ITS MAXIMUM VALUE'''
L=[]
N=int(input("Enter no. of values:"))
for i in range (0,N):
    value=int(input("Enter value:"))
    L.append(value)
MAX = L[0]
for i in range(1,N):
    if L[i]>MAX:
        MAX=L[i]
print("Maximum value is:",MAX)
