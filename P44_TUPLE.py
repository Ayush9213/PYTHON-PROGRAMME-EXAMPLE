#TO INPUT AND DISPLAY SUM OF ALL VALUES
L=[]
N=int(input("Enter no. of values:"))
for i in range (0,N):
    value=int(input("Enter value:"))
    L.append(value)
T= tuple(L)
SUM=0
for i in T:
    SUM=SUM+i
print("Sum of values:",SUM)
