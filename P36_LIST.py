#TO INPUT A LIST AND COUNT THE NO. OF EVEN AND ODD VALUES
L=[]
N=int(input("Enter no. of values:"))
for i in range (0,N):
    value=int(input("Enter value:"))
    L.append(value)
count1=count2=0
for i in L:
    if i%2==0:
        count1+=1
    else:
        count2+=1
    print("No. of even values:",count1)
    print("No. of odd values:",count2)
