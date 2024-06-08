#TO WRITE MENU DRIVER PROGRAMME TO CLACULATE AREAS
print("AREA MENU")
print("1. Area of square")
print("2. Area of rectangle")
print("3. Area of circle")
choice = int(input("Enter your choice:"))
if choice == 1:
    A = int(input("Enter side:"))
    print("Area of square:",A*A)
elif choice == 2:
    L = int(input("Enter length:"))
    B = int(input("Enter breadth:"))
    print("Area of rectangle:",L*B)
elif choice == 3:
    R= int(input("Enter radius:"))
    print("Area of circle is:",3.14*R**2)
else :
    print("Wrong choice entered")
