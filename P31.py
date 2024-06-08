#TO FIND THE SUM OF FIRST N NATURAL NUMBERS
N = int(input("Enter the value of N:"))
SUM = 0
for i in range (1,N+1):
    SUM = SUM+i
    print("SUM IS:",SUM)
