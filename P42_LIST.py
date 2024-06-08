#LEFT SHIFTING OF A LIST
L=[]
N=int(input("Enter no. of values:"))
for i in range (0,N):
    value=int(input("Enter value:"))
    L.append(value)
item=L[0]
for i in range(0,N-1):
    L[i]=L[i+1]
L[N-1]=item
print(L)
