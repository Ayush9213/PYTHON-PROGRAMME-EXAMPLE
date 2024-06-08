"""#TO INPUT A TUPLE AND DISPLAY SUM OF ALL
THE VALUES WHICH ARE ENDING WITH 2""" 
L=[]
N=int(input("Enter no. of values:"))
for i in range (0,N):
    value=int(input("Enter value:"))
    L.append(value)
T= tuple(L)
SUM=0
for i in T:
    if i%10==0:
        SUM=SUM+i
print("Sum of values:",SUM)
