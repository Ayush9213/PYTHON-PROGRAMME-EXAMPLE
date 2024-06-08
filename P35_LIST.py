#TO DISPLAY ALL THE VALUES WHICH ARE ENDED WITH 0
L=[]
N=int(input("Enter no. of values:"))
for i in range (0,N):
    value=int(input("Enter value:"))
    L.append(value)
for i in L:
    if i%10==0:
        print(i)
