#TO INPUT THREE INTEGER FROM THE USER AND PRINT LARGER ONE
A = int(input("Enter first integer:"))
B = int(input("Enter second integer:"))
C = int(input("Enter third integer:"))
if A>B:
    if A>C:
        print("Largest no is:", A)
    else:
        print("Largest no is:", C)
elif B>C:
        print("Largest no is:", B)
else:
    print("Largest no is:", C)
        
        
