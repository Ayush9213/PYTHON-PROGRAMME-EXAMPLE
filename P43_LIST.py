#RIGHT SHIFTING OF A LIST
L=[]
N=int(input("Enter no. of values:"))
for i in range (0,N):
    value=int(input("Enter value:"))
    L.append(value)
item=L[N-1]
for i in range(N-1,0,-1):
    L[i]=L[i-1]
L[0]=item
print(L)
