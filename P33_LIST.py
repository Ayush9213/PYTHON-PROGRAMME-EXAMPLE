#TO INPUT A LIST FROM USER AND DISPLAY ALL THE EVEN VALUES
L=[]
N=int(input("Enter no. of values:"))
for i in range (0,N):
    value=int(input("Enter value:"))
    L.append(value)
for i in L:
    if i%2==0:
        print(i)
