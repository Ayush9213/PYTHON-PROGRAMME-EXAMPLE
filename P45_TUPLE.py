"""#TO INPUT A TUPLE AND DISPLAY SUM OF ALL
THE VALUES PRESENT AT THE EVEN INDEX""" 
L=[]
N=int(input("Enter no. of values:"))
for i in range (0,N):
    value=int(input("Enter value:"))
    L.append(value)
T= tuple(L)
SUM=0
for i in range(0,N):
    if i%2==0:
        SUM=SUM+T[i]
print("Sum of values:",SUM)
