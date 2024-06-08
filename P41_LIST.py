#TO PERFORM LINEAR SEARCH
L=[]
N=int(input("Enter no. of values:"))
for i in range (0,N):
    value=int(input("Enter value:"))
    L.append(value)
item=int(input("Enter value to be searched:"))
flag=0
for i in range (0,N):
    if L[i]==item:
        flag=1
        index=i
        break
if flag==1:
    print("Value found at index:",index)
else:
    print("Value not found")
