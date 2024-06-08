#TO INPUT A LIST AND REVERSE THE LIST
L=[]
N=int(input("Enter no. of values:"))
for i in range (0,N):
    value=int(input("Enter value:"))
    L.append(value)
j=N-1
for i in range(0,N//2):
    L[i],L[j]=L[j],L[i]
    j=j-1
print(L)
