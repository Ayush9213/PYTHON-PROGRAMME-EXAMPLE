#TO INPUT LIST AND SUM THE VALUES OF EVEN INDEX
L=[]
N=int(input("Enter no. of values:"))
for i in range (0,N):
    value=int(input("Enter value:"))
    L.append(value)
sum=0
for i in range(0,N):
    if i%2==0:
        sum=sum+L[i]
        print(sum)
