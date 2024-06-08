#TO FIND ROOTS OF QUADRATIC EQUATION
a = int(input("ENTER THE VALUE OF a:"))
b = int(input("ENTER THE VALUE OF b:"))
c = int(input("ENTER THE VALUE OF c:"))
d = b*b-4*a*c
if d == 0:
    print("Roots are real and equal.")
    root1 = -b/2*a
    root2 = -b/2*a
    print("ROOT 1", root1)
    print("ROOT 2", root2)
elif d>0 :
    print("Roots are real and unequal.")
    root1 = (-b+d**0.5)/2*a
    root2 = (-b-d**0.5)/2*a
    print("ROOT 1", root1)
    print("ROOT 2", root2)
else :
    print("Roots are complex and imaginary.")
    
